# Predicción de Diabetes con Machine Learning  

Este proyecto forma parte de un Trabajo Fin de Máster (TFM) y tiene como objetivo desarrollar, evaluar y productizar un modelo de *machine learning* capaz de predecir la probabilidad de que un paciente padezca diabetes a partir de indicadores clínicos y hábitos de salud.  

## Proceso del Proyecto  

1. Análisis exploratorio de datos (EDA)  
   - Limpieza, transformación y selección de variables relevantes.  
   - Identificación de outliers, balanceo de clases y preparación del dataset.  

2. Entrenamiento y validación de modelos  
   - Se probaron distintos algoritmos de clasificación: Logistic Regression, Random Forest, Extra Trees, HistGradientBoosting, Gradient Boosting, SVM, entre otros.  
   - Se evaluaron métricas como PR-AUC (Average Precision), F1, Recall, Precision, Accuracy y ROC-AUC.  
   - Se priorizó PR-AUC como criterio principal por la naturaleza desbalanceada de los datos.  

3. Selección y Fine-Tuning  
   - El Gradient Boosting (GB) fue el mejor modelo en validación cruzada (CV).  
   - Se realizaron dos fases de fine-tuning:  
     - Grid Search inicial.  
     - Búsqueda fina alrededor de los hiperparámetros óptimos previos.  
   - Se comparó con técnicas de ensamble como Soft Voting y Stacking.  

4. Interpretabilidad y explicabilidad  
   - Se analizaron métricas derivadas de la matriz de confusión para cada modelo.  
   - Se estudiaron las curvas Precision-Recall y ROC.  
   - Se justificó la elección del modelo final desde un punto de vista práctico y de interpretabilidad.  

5. Productización  
   - El modelo final se integró en un pipeline de preprocesamiento + modelo y se exportó con joblib.  
   - Se desarrolló una API con FastAPI (app.py) que:  
     - Recibe datos de un paciente en formato JSON.  
     - Devuelve la predicción (diabético/no diabético) con un nivel de riesgo y una recomendación de acción.  
   - Se creó un contenedor Docker para facilitar la despliegue y portabilidad del sistema.  

##  Ejecución  

### 1. Clonar el repositorio  
git clone https://github.com/marciospain/master-ucm-tfm.git
cd master-ucm-tfm/app_pred_diabetes

### 2. Construir la imagen Docker  
docker build -t marciospain/master-ucm-tfm:latest .

### 3. Subir la imagen a Docker Hub  
docker push marciospain/master-ucm-tfm:latest

### 4. Ejecutar el contenedor  
docker run -d -p 8000:8000 marciospain/master-ucm-tfm:latest

La API quedará disponible en:  
http://{{url}}/pred_diabetes  

## Ejemplo de petición  

POST /pred_diabetes

{
  "HighBP": 1,
  "HighChol": 0,
  "Smoker": 0,
  "Stroke": 0,
  "HeartDiseaseorAttack": 0,
  "PhysActivity": 1,
  "Fruits": 1,
  "Veggies": 1,
  "NoDocbcCost": 0,
  "DiffWalk": 0,
  "Sex": 1,
  "BMI": 27.5,
  "MentHlth": 3,
  "PhysHlth": 5,
  "Age": 7,
  "Education": 4,
  "Income": 5,
  "GenHlth": 3
}

## Futuras Extensiones  

Aunque este proyecto se centra en la productización vía API, se podrían desarrollar frontends como:  
- Aplicación móvil para autodiagnóstico preventivo.  
- Formulario web en clínicas o sistemas de salud.  
- Integración con dashboards médicos para soporte a profesionales.  

##  Recursos  

- GitHub: https://github.com/marciospain/master-ucm-tfm  
- DockerHub: https://hub.docker.com/r/marciospain/master-ucm-tfm  
- Anexos: Notebooks, código Python y documentación incluidos en el repositorio.  

