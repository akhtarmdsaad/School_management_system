"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from  django.conf.urls.static import static

from . import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #Login
    path('', views.LOGIN,name='login'),
    path('doLogin/', views.doLogin,name='doLogin'),
    path('doLogout/', views.doLogout,name='doLogout'),

    #profile update
    path('profile/',views.PROFILE,name="profile"),
    path('profile/update',views.PROFILE_UPDATE, name="profile_update"),

    

    #HOD panel url
    path('Hod/Home/',Hod_views.home,name="hod_home"),
    path('Hod/Student/ADD',Hod_views.ADD_STUDENT,name="add_student"),
    path('Hod/Student/VIEW',Hod_views.VIEW_STUDENT,name="view_student"),
    path('Hod/Student/UPDATE',Hod_views.UPDATE_STUDENT,name="update_student"),
    path('Hod/Student/EDIT/<str:id>',Hod_views.EDIT_STUDENT,name="edit_student"),
    path('Hod/Student/DELETE/<str:admin>',Hod_views.DELETE_STUDENT,name="delete_student"),

    path('Hod/Staff/ADD',Hod_views.ADD_STAFF,name="add_staff"),
    path('Hod/Staff/VIEW',Hod_views.VIEW_STAFF,name="view_staff"),
    path('Hod/Staff/EDIT/<str:id>',Hod_views.EDIT_STAFF,name="edit_staff"),
    path('Hod/Student/DELETE/<str:admin>',Hod_views.DELETE_STAFF,name="delete_staff"),
    path('Hod/Staff/UPDATE',Hod_views.UPDATE_STAFF,name="update_staff"),
    
    path('Hod/Course/ADD',Hod_views.ADD_COURSE,name="add_course"),
    path('Hod/Course/VIEW',Hod_views.VIEW_COURSE,name="view_course"),
    path('Hod/Course/EDIT/<str:id>',Hod_views.EDIT_COURSE,name="edit_course"),
    path('Hod/Course/UPDATE',Hod_views.UPDATE_COURSE,name="update_course"),
    path('Hod/Course/DELETE/<str:id>',Hod_views.DELETE_COURSE,name="delete_course"),

    path('Hod/Subject/ADD',Hod_views.ADD_SUBJECT,name="add_subject"),
    path('Hod/Subject/VIEW',Hod_views.VIEW_SUBJECT,name="view_subject"),
    path('Hod/Subject/EDIT/<str:id>',Hod_views.EDIT_SUBJECT,name="edit_subject"),
    path('Hod/Subject/UPDATE',Hod_views.UPDATE_SUBJECT,name="update_subject"),
    path('Hod/Subject/DELETE/<str:id>',Hod_views.DELETE_SUBJECT,name="delete_subject"),

    path('Hod/Session/ADD',Hod_views.ADD_SESSION,name="add_session"),
    path('Hod/Session/VIEW',Hod_views.VIEW_SESSION,name="view_session"),
    path('Hod/Session/EDIT/<str:id>',Hod_views.EDIT_SESSION,name="edit_session"),
    path('Hod/Session/UPDATE',Hod_views.UPDATE_SESSION,name="update_session"),
    path('Hod/Session/DELETE/<str:id>',Hod_views.DELETE_SESSION,name="delete_session"),

    path('Hod/Staff/Send_Notification',Hod_views.SEND_STAFF_NOTIFICATION, name = "send_staff_notification"),
    path('Hod/Staff/Save_Notification',Hod_views.SAVE_STAFF_NOTIFICATION, name = "save_staff_notification"),
    path('Hod/Student/Send_Notification',Hod_views.SEND_STUDENT_NOTIFICATION, name = "send_student_notification"),
    path('Hod/Student/Save_Notification',Hod_views.SAVE_STUDENT_NOTIFICATION, name = "save_student_notification"),

    path('Hod/Staff/Leave_view',Hod_views.STAFF_LEAVE_VIEW, name = "staff_leave_view"),
    path('Hod/Staff/Approve_leave/<str:id>',Hod_views.STAFF_APPROVE_LEAVE, name = "staff_approve_leave"),
    path('Hod/Staff/disapprove_leave/<str:id>',Hod_views.STAFF_DISAPPROVE_LEAVE, name = "staff_disapprove_leave"),
    
    path('Hod/Staff/Feedback',Hod_views.STAFF_FEEDBACK, name = "hod_staff_feedback"),
    path('Hod/Staff/Feedback_save',Hod_views.STAFF_FEEDBACK_SAVE, name = "hod_staff_feedback_save"),

    path('Hod/Student/Feedback',Hod_views.Student_FEEDBACK, name = "hod_student_feedback"),
    path('Hod/Student/Feedback_save',Hod_views.Student_FEEDBACK_SAVE, name = "hod_student_feedback_save"),

    path('Hod/Student/Leave_view',Hod_views.Student_LEAVE_VIEW, name = "student_leave_view"),
    path('Hod/Student/Approve_leave/<str:id>',Hod_views.Student_APPROVE_LEAVE, name = "student_approve_leave"),
    path('Hod/Student/disapprove_leave/<str:id>',Hod_views.Student_DISAPPROVE_LEAVE, name = "student_disapprove_leave"),

    path('Hod/View_attendance',Hod_views.VIEW_ATTENDANCE, name = "hod_view_attendance"),

    #This is Staff urls 
    path("Staff/Home",Staff_views.HOME, name = "staff_home"),
    path("Staff/Notifications",Staff_views.NOTIFICATIONS, name = "notifications"),
    path("Staff/mark_as_done/<str:status>",Staff_views.STAFF_NOTIFICATION_AS_DONE, name = "staff_notification_mark_as_done"),
    path("Staff/apply_leave",Staff_views.APPLY_LEAVE, name = "staff_apply_leave"),
    path("Staff/apply_leave_save",Staff_views.APPLY_LEAVE_SAVE, name = "staff_apply_leave_save"),
    path("Staff/Feedback",Staff_views.STAFF_FEEDBACK, name = "staff_feedback"),
    path("Staff/Feedback_save",Staff_views.STAFF_FEEDBACK_SAVE, name = "staff_feedback_save"),

    path("Staff/Take_Attendance",Staff_views.STAFF_TAKE_ATTENDANCE,name = "staff_take_attendance"),
    path("Staff/Save_Attendance",Staff_views.STAFF_Save_ATTENDANCE,name = "staff_Save_attendance"),

    path("Staff/view_Attendance",Staff_views.STAFF_view_ATTENDANCE,name = "staff_view_attendance"),
    
    path("Staff/Add/Result",Staff_views.STAFF_add_result,name = "staff_add_result"),
    path("Staff/Save/Result",Staff_views.STAFF_save_result,name = "staff_save_result"),

    #student urls
    path("Student/home",Student_views.HOME,name="student_home"),
    path("Student/Notifications",Student_views.NOTIFICATIONS, name = "student_notifications"),
    path("Student/mark_as_done/<str:status>",Student_views.STUDENT_NOTIFICATION_AS_DONE, name = "student_notification_mark_as_done"),
    path("Student/Feedback",Student_views.Student_FEEDBACK, name = "student_feedback"),
    path("Student/Feedback_save",Student_views.Student_FEEDBACK_SAVE, name = "student_feedback_save"),
    path("Student/apply_leave",Student_views.APPLY_LEAVE, name = "student_apply_leave"),
    path("Student/apply_leave_save",Student_views.APPLY_LEAVE_SAVE, name = "student_apply_leave_save"),
     
    path("Student/view_Attendance",Student_views.Student_view_ATTENDANCE,name = "student_view_attendance"),
    path("Student/view_result",Student_views.Student_view_result,name = "student_view_result"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
