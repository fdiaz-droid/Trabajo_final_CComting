# Trabajo Final – FastAPI + ML (Iris Demo)

**Repo:** https://github.com/fdiaz-droid/Trabajo_final_CComting

## Integrantes
- Frank Díaz
- Braian Escobar

---

## Descripción
API en **FastAPI** que sirve un modelo de **clasificación** entrenado con el dataset **Iris**.  
El endpoint `/predict` recibe vectores de **4 features numéricas** (largo/ancho de sépalo y pétalo) y devuelve la **clase** más probable: `setosa`, `versicolor` o `virginica`.

> Este proyecto funciona como **plantilla**: puedes reemplazar el dataset/algoritmo en `train.py` y mantener la misma API.

## Estructura

```

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

.venv\Scripts\activate

pip install -r requirements.txt
```

## 3) Ejecutar la API
```bash
uvicorn app.main:app --reload
```
Link local:
http://127.0.0.1:8000/docs


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
