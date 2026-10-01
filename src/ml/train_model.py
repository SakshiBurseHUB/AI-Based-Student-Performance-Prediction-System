import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from src.ml.data_preprocessing import prepare_data


DATASET_PATH = 'datasets/student_performance.csv'
MODEL_DIR = 'src/ml/models'
MODEL_PATH = os.path.join(MODEL_DIR, 'student_performance_model.pkl')


def train_model():
    X_train, X_test, y_train, y_test = prepare_data(DATASET_PATH)

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions, zero_division=0))

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print(f"\nModel saved to: {MODEL_PATH}")


if __name__ == '__main__':
    train_model()