from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Cargar modelo al iniciar la API
modelo = joblib.load("./modelos/modelo_diabetes.pkl")

# Columnas esperadas (orden consistente con el entrenamiento)
cols_binarias   = ['HighBP','HighChol','Smoker','Stroke','HeartDiseaseorAttack',
                   'PhysActivity','Fruits','Veggies','NoDocbcCost','DiffWalk','Sex']
cols_continuas  = ['BMI','MentHlth','PhysHlth']
cols_ordinales  = ['Age','Education','Income','GenHlth']
todas = cols_binarias + cols_continuas + cols_ordinales

# Definir formato de entrada (ejemplo simple: un paciente)
class Paciente(BaseModel):
    HighBP: int
    HighChol: int
    Smoker: int
    Stroke: int
    HeartDiseaseorAttack: int
    PhysActivity: int
    Fruits: int
    Veggies: int
    NoDocbcCost: int
    DiffWalk: int
    Sex: int
    BMI: float
    MentHlth: float
    PhysHlth: float
    Age: int
    Education: int
    Income: int
    GenHlth: int

# Inicializar API
app = FastAPI(title="Predicción de Diabetes")

# Función de presentación (la misma que definimos antes)
def presentar_prediccion(prob, thr=0.55, zona_inferior=0.45, zona_superior=0.60):
    if zona_inferior <= prob <= zona_superior:
        return {
            "resultado": "INCIERTO",
            "riesgo": "Riesgo moderado",
            "accion": "Recomendado ampliar información o repetir medición/chequeo."
        }
    else:
        etiqueta = "DIABÉTICO" if prob >= thr else "NO DIABÉTICO"
        if prob < 0.30:
            return {"resultado": etiqueta, "riesgo": "Riesgo bajo",
                    "accion": "Mantener hábitos saludables y seguimiento rutinario."}
        elif prob < 0.60:
            return {"resultado": etiqueta, "riesgo": "Riesgo moderado",
                    "accion": "Considerar chequeo preventivo con profesional."}
        else:
            return {"resultado": etiqueta, "riesgo": "Riesgo alto",
                    "accion": "Recomendado evaluación clínica prioritaria."}

# Endpoint para predicción
@app.post("/pred_diabetes")
def predict(paciente: Paciente):
    df = pd.DataFrame([paciente.dict()])[todas]
    proba = modelo.predict_proba(df)[0, 1]
    return presentar_prediccion(proba)
