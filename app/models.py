from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100, unique=True)
    student_phone = models.CharField(max_length=15, unique=True)
    student_address = models.TextField()
    student_dob = models.DateField()
    student_image = models.ImageField(upload_to='images/')
    student_course = models.CharField(max_length=100)
    student_enrollment_date = models.DateField()
    student_document = models.FileField(upload_to='documents/')
    student_status = models.BooleanField(default=True)

   
