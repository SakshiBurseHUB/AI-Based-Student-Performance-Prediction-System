from django.shortcuts import render, redirect
from .models import Student

from src.ml.predict import predict_performance


def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html', {
        'students': students
    })


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST['student_id'],
            name=request.POST['name'],
            attendance=request.POST['attendance'],
            study_hours=request.POST['study_hours'],
            previous_marks=request.POST['previous_marks'],
            assignment_marks=request.POST['assignment_marks'],
            internal_marks=request.POST['internal_marks'],
        )

        return redirect('students:student_list')

    return render(request, 'students/student_form.html')


def predict_student_performance(request):
    prediction = None
    message = None

    if request.method == 'POST':
        attendance = float(request.POST['attendance'])
        study_hours = float(request.POST['study_hours'])
        previous_marks = float(request.POST['previous_marks'])
        assignment_marks = float(request.POST['assignment_marks'])
        internal_marks = float(request.POST['internal_marks'])

        prediction = predict_performance(
            attendance,
            study_hours,
            previous_marks,
            assignment_marks,
            internal_marks
        )

        if prediction == 'High':
            message = 'The student is performing well and maintaining good academic progress.'
        elif prediction == 'Medium':
            message = 'The student may need additional academic support and regular monitoring.'
        else:
            message = 'The student needs attention and academic support to improve performance.'

    return render(request, 'students/predict.html', {
        'prediction': prediction,
        'message': message
    })