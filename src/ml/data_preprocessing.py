import pandas as pd
from sklearn.model_selection import train_test_split


FEATURES = [
    'attendance',
    'study_hours',
    'previous_marks',
    'assignment_marks',
    'internal_marks'
]

TARGET = 'performance'


def load_data(file_path):
    return pd.read_csv(file_path)


def prepare_data(file_path):
    df = load_data(file_path)

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test