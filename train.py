
"""
Entrena un modelo simple (Iris) y guarda model/model.pkl
"""
import os, joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

os.makedirs("model", exist_ok=True)
os.makedirs("Evidencias", exist_ok=True)

# --- datos ---
iris = load_iris()
X, y = iris.data, iris.target
target_names = iris.target_names.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- modelo ---
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000))   # ← sin multi_class
])
pipe.fit(X_train, y_train)

# --- evaluación ---
y_pred = pipe.predict(X_test)
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=target_names)
print("\n=== MÉTRICAS (TEST) ===")
print(f"Accuracy: {acc:.4f}")
print(report)

# guarda reporte
with open("Evidencias/metricas_test.txt", "w", encoding="utf-8") as f:
    f.write(f"Accuracy: {acc:.4f}\n\n{report}")

# matriz de confusión (sin matplotlib)
cm = confusion_matrix(y_test, y_pred)
np.savetxt("Evidencias/matriz_confusion.csv", cm, fmt="%d", delimiter=",")