from tkinter import CASCADE
from unittest.main import MODULE_EXAMPLES
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    # isStaff=models.BooleanField(default=True)
    mobile=models.CharField(max_length=10)
    isVerified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6)
    institution=models.CharField(max_length=30)
    std=models.IntegerField(null=True)
    referal=models.CharField(max_length=30,null=True,blank=True)

    objects= UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

class Exam(models.Model):
    EXAM_CHOICES = (
    ('mcq','MCQ'),
    ('Subjective', 'SUBJECTIVE'),)
    total_questions=models.IntegerField(null=True)
    exam_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30, null=True)
    duration=models.CharField(max_length=30, default='00:30:00')
    exam_type=models.CharField(max_length=10,choices=EXAM_CHOICES)
    
    def __str__(self):
        return str(self.exam_id)


class Mcq(models.Model):
    Exam=models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
    qno=models.IntegerField(unique=True,primary_key=True,default=0)
    question=models.CharField(max_length=50)
    option1=models.CharField(max_length=30)
    option2=models.CharField(max_length=30)
    option3=models.CharField(max_length=30)
    option4=models.CharField(max_length=30)

class Answer(models.Model):
    Exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
    student=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qno=models.ForeignKey(Mcq,on_delete=models.CASCADE)
    ans=models.CharField(max_length=30)

class Subjective(models.Model):
    exam =models.ForeignKey(Exam, on_delete=models.CASCADE)
    qno=models.IntegerField(unique=True,primary_key=True,default=0)
    question=models.CharField(max_length=50)


class SubAnswer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    qno=models.ForeignKey(Mcq,on_delete=models.CASCADE)
    ans=models.FileField(null=True)

class RegisteredExam(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)

class GivenExam(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)

class StudentLog(models.Model):
    studentEmail=models.EmailField(null=True)
    examId=models.IntegerField(null=True)
    img=models.CharField(max_length=3000,null=True)