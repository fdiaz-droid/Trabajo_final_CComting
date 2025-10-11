
from fastapi import FastAPI
from pydantic import BaseModel, Field, conlist
from typing import List, Optional
import joblib
import numpy as np
import os



app = FastAPI(title="Iris Classifier API", version="1.0.0")

# Load model artifact once at startup
ARTIFACT_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model.pkl")
_artifact = joblib.load(ARTIFACT_PATH)
_model = _artifact["model"]
_target_names = _artifact["target_names"]

class PredictRequest(BaseModel):
    features: List[conlist(float, min_length=4, max_length=4)] = Field(
        ..., description="List of 4 features"
    )
    return_proba: bool = False

class PredictResponse(BaseModel):
    predictions: List[str]
    proba: Optional[List[List[float]]] = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    X = np.array(req.features, dtype=float)
    y_pred_idx = _model.predict(X).tolist()
    y_pred = [_target_names[i] for i in y_pred_idx]
    proba = _model.predict_proba(X).tolist() if req.return_proba else None
    return {"predictions": y_pred, "proba": proba}
