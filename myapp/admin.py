from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Exam, GivenExam, Mcq,Answer,Subjective,SubAnswer,RegisteredExam,StudentLog

admin.site.register(CustomUser)
admin.site.register(Exam)
admin.site.register(Mcq)
admin.site.register(Answer)
admin.site.register(Subjective)
admin.site.register(SubAnswer)
admin.site.register(RegisteredExam)
admin.site.register(GivenExam)
admin.site.register(StudentLog)
# Register your models here.
