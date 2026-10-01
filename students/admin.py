from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'name',
        'attendance',
        'study_hours',
        'previous_marks',
        'assignment_marks',
        'internal_marks',
        'created_at',
    )

    search_fields = ('student_id', 'name')