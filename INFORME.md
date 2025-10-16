# Informe – Trabajo Final (FastAPI + ML)

## Integrantes
- Frank Díaz
- Braian Escobar

## 1. Datos
- Fuente: Iris (scikit-learn)
- Variables: 4 numéricas (sepal_length, sepal_width, petal_length, petal_width)
- Target: especie (`setosa`, `versicolor`, `virginica`)

## 2. Preparación
- Sin nulos. Normalización con `StandardScaler` en el pipeline.

## 3. Modelo
- Pipeline: `StandardScaler` + `LogisticRegression` (multiclase, softmax)
- Justificación: baseline simple, reproducible y rápido para demo/despliegue.

## 4. Validación y Métricas (test)
- Split 80/20, `random_state=42`, `stratify=y`
- **Accuracy**: 0.9333
- Ver `evidencias/metricas_test.txt` y `evidencias/matriz_confusion.png`.

## 5. API FastAPI
- Endpoints: `GET /health`, `POST /predict`
- Entrada: N×4 floats (mismo orden del entrenamiento)
- Salida: `predictions` y (opcional) `proba`
- Evidencias: ver capturas en `Evidencias/` (o `evidencias/` según tu carpeta).

## 6. Decisiones/Supuestos
- Consistencia del orden de features entre entrenamiento e inferencia.
- Mapeo de índices a texto usando `target_names` en el artefacto.

## 7. Limitaciones y Próximos Pasos
- Dataset demo; para caso real cambiar datos/objetivo y validar con métricas acordes.
- Probar RF/XGBoost, k-fold y tuning.

## 8. Repositorio
- Público: https://github.com/fdiaz-droid/Trabajo_final_CComting
- Contiene código, `model.pkl`, `requirements.txt`, `README.md` y evidencias.