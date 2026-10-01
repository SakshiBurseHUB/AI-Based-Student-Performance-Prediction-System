from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    attendance = models.FloatField()
    study_hours = models.FloatField()
    previous_marks = models.FloatField()
    assignment_marks = models.FloatField()
    internal_marks = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} - {self.name}"