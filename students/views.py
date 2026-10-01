from django.shortcuts import render, redirect
from .models import Student


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