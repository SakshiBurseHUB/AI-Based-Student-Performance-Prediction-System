import joblib

MODEL_PATH = 'src/ml/models/student_performance_model.pkl'


def predict_performance(
    attendance,
    study_hours,
    previous_marks,
    assignment_marks,
    internal_marks
):
    model = joblib.load(MODEL_PATH)

    data = [[
        attendance,
        study_hours,
        previous_marks,
        assignment_marks,
        internal_marks
    ]]

    prediction = model.predict(data)[0]

    return prediction


if __name__ == '__main__':
    result = predict_performance(
        85,
        5,
        80,
        82,
        79
    )

    print('Predicted Performance:', result)