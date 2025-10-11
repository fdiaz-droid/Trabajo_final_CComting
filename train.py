
"""
Entrena un modelo simple (Iris) y guarda model/model.pkl
"""
import os, joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

def main():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, multi_class="auto"))
    ])
    pipe.fit(X_train, y_train)

    artifact = {"model": pipe, "target_names": iris.target_names.tolist()}
    os.makedirs("model", exist_ok=True)
    joblib.dump(artifact, os.path.join("model", "model.pkl"))
    print("Modelo entrenado y guardado en model/model.pkl")

if __name__ == "__main__":
    main()
