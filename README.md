# ML + FastAPI (Plantilla lista para usar)

Proyecto mínimo funcional que cumple con: análisis/entrenamiento, serialización del modelo (`model/model.pkl`) y una API con FastAPI que expone `/predict` y `/health`.

## Estructura
```
ml_fastapi_template/
├─ app/
│  └─ main.py
├─ model/
│  └─ model.pkl
├─ tests/
│  └─ test_app.py
├─ requirements.txt
├─ train.py
├─ example_request.json
├─ Dockerfile
└─ README.md
```

## 1) Crear entorno e instalar dependencias
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## 2) (Opcional) Re-entrenar el modelo
El repo ya incluye `model/model.pkl` entrenado con **Iris** (clasificación). Si quieres regenerarlo:
```bash
python train.py
```

## 3) Ejecutar la API
```bash
uvicorn app.main:app --reload
```
Visita la documentación interactiva en:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 4) Ejemplo de request
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d @example_request.json
```

**`example_request.json`**
```json
{
  "features": [[5.1, 3.5, 1.4, 0.2], [6.7, 3.1, 4.7, 1.5]],
  "return_proba": true
}
```

## 5) Pruebas rápidas
```bash
pytest -q
```

## 6) Docker (listo para Cloud Run/Render/Fly.io)
Construir y ejecutar localmente:
```bash
docker build -t iris-api .
docker run -p 8080:8080 iris-api
```
La API quedará en `http://127.0.0.1:8080`.

### Despliegue rápido a Google Cloud Run (referencia)
1. Autentícate e inicializa proyecto:
   ```bash
   gcloud auth login
   gcloud config set project TU_PROYECTO
   ```
2. Construye e impuja la imagen:
   ```bash
   gcloud builds submit --tag gcr.io/TU_PROYECTO/iris-api
   ```
3. Despliega:
   ```bash
   gcloud run deploy iris-api --image gcr.io/TU_PROYECTO/iris-api --platform managed --allow-unauthenticated --region us-central1 --port 8080
   ```

### Despliegue en Render (referencia)
- Crea un nuevo **Web Service**, conecta tu repo, selecciona **Docker**.
- Comando de inicio: `uvicorn app.main:app --host 0.0.0.0 --port 8080`

### Despliegue en Fly.io (referencia)
```bash
flyctl launch --name iris-api --now
# Ajusta el puerto 8080 en la config si es necesario
```

## 7) Qué entregar
- Repo público en GitHub con: código, `model.pkl`, `requirements.txt`, `README.md` y captura de la API corriendo local.
- (Plus) URL pública si despliegas en la nube.