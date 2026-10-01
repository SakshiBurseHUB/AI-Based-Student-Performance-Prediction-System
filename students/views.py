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

def dashboard(request):
    students = Student.objects.all()

    total_students = students.count()
    high_students = 0
    medium_students = 0
    low_students = 0

    for student in students:
        prediction = predict_performance(
            student.attendance,
            student.study_hours,
            student.previous_marks,
            student.assignment_marks,
            student.internal_marks
        )

        if prediction == 'High':
            high_students += 1
        elif prediction == 'Medium':
            medium_students += 1
        elif prediction == 'Low':
            low_students += 1

    return render(request, 'students/dashboard.html', {
        'students': students,
        'total_students': total_students,
        'high_students': high_students,
        'medium_students': medium_students,
        'low_students': low_students,
    })