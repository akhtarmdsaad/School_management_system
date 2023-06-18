from django.contrib import admin
from .models import CustomUser, Session_Year, Course, Staff, Student, Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Student_Notification,Student_Feedback 
from app.models import Student_Leave,Attendance,Attendance_report,StudentResult
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ["username","user_type"]

# Register your models here.
admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Student_Notification)
admin.site.register(Staff_Leave)
admin.site.register(Student_Leave)
admin.site.register(Staff_Feedback)
admin.site.register(Student_Feedback)
admin.site.register(Attendance_report)
admin.site.register(Attendance)
admin.site.register(StudentResult)
