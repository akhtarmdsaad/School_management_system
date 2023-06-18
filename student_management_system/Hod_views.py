from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from app.models import Attendance, Attendance_report, Course,Session_Year,CustomUser, Staff,Student, Subject, Staff_Notification,Staff_Leave,Staff_Feedback,Student_Notification,Student_Feedback
from app.models import Student_Leave
from django.contrib import messages


@login_required(login_url="/")
def home(request):
    stu_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    male_student = Student.objects.filter(gender="Male").count()
    female_student = Student.objects.filter(gender="Female").count()

    
    context = {
        "stu_count":stu_count,
        "staff_count":staff_count,
        "course_count":course_count,
        "subject_count":subject_count,
        "male_student":male_student,
        "female_student":female_student
    }

    return render(request,"hod/home.html",context)

@login_required(login_url="/")
def ADD_STUDENT(request):

    courses = Course.objects.all()
    sessions = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        course_id = request.POST.get("course_id")
        session_year_id = request.POST.get("session_year_id")
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email is already Taken.")
            return redirect("add_student")
        elif CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"Email is already Taken.")
            return redirect("add_student")
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()


            course = Course.objects.get(pk=course_id)
            session_year = Session_Year.objects.get(pk=session_year_id)

            student = Student(
                admin = user,
                address = address, 
                course_id = course,
                session_year_id = session_year,
                gender = gender
            )
            student.save()

            messages.success(request,f"{user.first_name} Added Successfully")

    
    
    context = {
        "courses":courses,
        "sessions":sessions,
    }
    return render(request,"hod/add_student.html",context)

@login_required(login_url="/")
def VIEW_STUDENT(request):
    students = Student.objects.all()

    context = {
        "students":students
    }

    return render(request,"hod/view_student.html",context)

@login_required(login_url="/")
def EDIT_STUDENT(request,id=None):
    if id is None:
        return HttpResponse("No id Specified") 
    student = Student.objects.filter(id=id)[0]

    courses = Course.objects.all()
    sessions = Session_Year.objects.all()

    context = {
        "user":student,
        "courses":courses,
        "sessions":sessions,
    }
    # print("Yha tak aa gaya, id:",id,student)
    return render(request,"hod/edit_student.html",context)

@login_required(login_url="/")
def UPDATE_STUDENT(request):
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        id = request.POST.get("student_id")
        course_id = request.POST.get("course_id")
        session_year_id = request.POST.get("session_year_id")

        user = CustomUser.objects.get(id=id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password:
            user.set_password(password)
        if profile_pic:
            user.profile_pic = profile_pic
        

        staff = Staff.objects.filter(id=id)[0]
        staff.address = address
        staff.gender = gender

        context = {
            "user":staff,
        }
        
        student = Student.objects.filter(id=id)[0]

        courses = Course.objects.all()
        sessions = Session_Year.objects.all()

        context = {
            "user":student,
            "courses":courses,
            "sessions":sessions,
        }

        return (request,"hod/edit_student.html",context)
    return redirect("view_student")

@login_required(login_url="/")
def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(pk=admin)
    student.delete()
    messages.success(request,"Data Successfully deleted")
    return redirect("view_student")

@login_required(login_url="/")
def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course = Course.objects.create(name = course_name)
        messages.success(request,"Course added successfully")
        return redirect("add_course")
    return render(request,"hod/add_course.html")

@login_required(login_url="/")
def VIEW_COURSE(request):
    courses = Course.objects.all()
    context = {"courses":courses}
    return  render(request,"hod/view_course.html",context)

@login_required(login_url="/")
def EDIT_COURSE(request, id=None):
    course = Course.objects.get(pk=id)
    return render(request,"hod/edit_course.html",{
        "course":course
    })

@login_required(login_url="/")
def UPDATE_COURSE(request):
    if request.method=="POST":
        course_name = request.POST.get("course_name")
        course_id = request.POST.get("course_id")

        
        course = Course.objects.get(pk=course_id)
        course.name = course_name
        course.save()
        messages.success(request,"Course Updated Successfully")

        return redirect("view_course")
    return render(request,"hod/edit_course.html")

@login_required(login_url="/")
def DELETE_COURSE(request,id=None):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,"Course deleted successfully")
    return redirect("view_course")

@login_required(login_url="/")
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email is already Taken.")
            return redirect("add_staff")
        elif CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"Email is already Taken.")
            return redirect("add_staff")
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()
            
            staff = Staff(
                admin = user,
                address = address, 
                gender = gender
            )
            staff.save()
            messages.success(request,f"{user.first_name} Added Successfully")


    return render(request,"hod/add_staff.html")

@login_required(login_url="/")
def VIEW_STAFF(request):
    staffs = Staff.objects.all()
    return render(request,"hod/view_staff.html",{
        "staffs":staffs
    })

@login_required(login_url="/")
def EDIT_STAFF(request,id=None):
    if id is None:
        return HttpResponse("No id Specified") 
    student = Staff.objects.filter(id=id)[0]


    context = {
        "user":student,
    }
    return render(request,"hod/edit_staff.html",context)

@login_required(login_url="/")
def DELETE_STAFF(request, admin):
    staff = CustomUser.objects.get(pk=admin)
    staff.delete()
    messages.success(request,"Data Successfully deleted")
    return redirect("view_staff")

@login_required(login_url="/")
def UPDATE_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        id = request.POST.get("staff_id")

        user = CustomUser.objects.get(id=id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password:
            user.set_password(password)
        if profile_pic:
            user.profile_pic = profile_pic
        

        staff = Staff.objects.filter(id=id)[0]
        staff.address = address
        staff.gender = gender

        context = {
            "user":staff,
        }

        return (request,"hod/edit_staff.html",context)
    return redirect("view_staff")

@login_required(login_url="/")
def ADD_SUBJECT(request):
        
    course = Course.objects.all()
    staff = Staff.objects.all()
    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")

        course = Course.objects.get(pk=course_id)
        staff = Staff.objects.get(pk=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff = staff
        )

        subject.save()
        messages.success(request,"Subject added successfully")
        return redirect("add_subject")

    context = {
        "courses":course,"staffs":staff
    }
    return render(request,"Hod/add_subject.html",context)

@login_required(login_url="/")
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        "subject":subject
    }
    return render(request,"Hod/view_subject.html",context)

@login_required(login_url="/")
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(pk=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        "subject":subject,
        "courses":course,
        "staffs":staff

    }
    return render(request,"Hod/edit_subject.html",context)

@login_required(login_url="/")
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")

        course = Course.objects.get(pk=course_id)
        staff = Staff.objects.get(pk=staff_id)
        
        subject = Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff=staff
        )

        subject.save()
        messages.success(request,"Subject Updated Successfully")

        return redirect("view_subject")
    return redirect("view_subject")

@login_required(login_url="/")
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,"Subject Deleted Successfully")

    return redirect("view_subject")

@login_required(login_url="/")
def ADD_SESSION(request):
    if request.method == "POST":
        start = request.POST.get("session_year_start")
        end = request.POST.get("session_year_end")

        session = Session_Year(session_start=start, session_end = end)

        session.save()
        messages.success(request,"Session Created Successfully")

        return  redirect("add_session")
    return  render(request,"Hod/add_session.html")

@login_required(login_url="/")
def VIEW_SESSION(request):
    session = Session_Year.objects.all()
    context = {
        "session":session
    }
    return  render(request,"Hod/view_session.html",context)

@login_required(login_url="/")
def EDIT_SESSION(request,id):

    session = Session_Year.objects.get(id=id)
    context = {
        "session":session
    }

    return render(request,"Hod/edit_session.html",context)

@login_required(login_url="/")
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get("session_id")
        start = request.POST.get("session_year_start")
        end = request.POST.get("session_year_end")

        session = Session_Year(
            id = session_id,
            session_start = start,
            session_end = end
        )

        session.save()
        messages.success(request,"Session Updated Successfully")
    return  redirect("view_session")

@login_required(login_url="/")
def DELETE_SESSION(request, id):
    session = Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request,"Session deleted successfully")

    return redirect("view_session")

@login_required(login_url="/")
def SEND_STAFF_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[:5]

    context = {
        "staffs":staff,
        "see_notification":see_notification
    }
    return render(request,'Hod/staff_notification.html',context)

def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        message = request.POST.get("message")
        staff = Staff.objects.get(admin = staff_id)

        notification = Staff_Notification(
            staff_id = staff,
            message = message
        )
        notification.save()
        messages.success(request,"Notification Sent Successfully")
    return redirect("send_staff_notification")

def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()

    context = {
        "staff_leave":staff_leave
    }
    return render(request,"hod/staff_leave.html",context)

def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    # messages.success(request,"Approved")
    return redirect("staff_leave_view")

def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    # messages.success(request,"Disapproved")
    return redirect("staff_leave_view")

def STAFF_FEEDBACK(request):
    staff = Staff.objects.all()
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by("-id")[:5]
    
    context = {
        "staffs":staff,
        "feedback":feedback,
        "feedback_history":feedback_history
    }
    return render(request,"Hod/staff_feedback.html",context)
 
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get("feedback_id")
        reply = request.POST.get("reply")

        feedback = Staff_Feedback.objects.get(id = feedback_id)

        feedback.feedback_reply = reply 
        feedback.save()

    return redirect("hod_staff_feedback")

def SEND_STUDENT_NOTIFICATION(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()
    context = {
        "student":student,
        "see_notification":notification
    }
    return render(request,"hod/student_notifications.html",context)

def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == "POST":
        message = request.POST.get("message")
        student_id = request.POST.get("student_id")
        student = Student.objects.get(admin=student_id)

        stu_notf = Student_Notification(
            message = message,
            student_id = student
        )
        # print(message,student,"\n*"*4)
        messages.success(request,"Student Notification Sent Successfully")
        stu_notf.save()
    return redirect("send_student_notification")

def Student_FEEDBACK(request):
    student = Student.objects.all()
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by("-id")[:5]
    
    context = {
        "students":student,
        "feedback":feedback,
        "feedback_history":feedback_history
    }
    return render(request,"Hod/student_feedback.html",context)

def Student_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get("feedback_id")
        reply = request.POST.get("reply")

        feedback = Student_Feedback.objects.get(id = feedback_id)

        feedback.feedback_reply = reply 
        feedback.save()

    return redirect("hod_student_feedback")

def Student_LEAVE_VIEW(request):
    student_leave = Student_Leave.objects.all()

    context = {
        "student_leave":student_leave
    }
    return render(request,"hod/student_leave.html",context)

def Student_APPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    # messages.success(request,"Approved")
    return redirect("student_leave_view")

def Student_DISAPPROVE_LEAVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    # messages.success(request,"Disapproved")
    return redirect("student_leave_view")

def VIEW_ATTENDANCE(request):
    subject = Subject.objects.all()
    session = Session_Year.objects.all()

    action = request.GET.get('action')
    get_subject=None
    get_session = None
    date = None
    attendance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            date = request.POST.get('date')
            
            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session_Year.objects.get(id = session_id)
            attendance = Attendance.objects.filter(subject_id=get_subject, attendance_date = date, session_year_id=get_session)
            for i in attendance:
                attendance_id = i.id 
                attendance_report = Attendance_report.objects.filter(attendance_id=attendance_id)


    context = {
        "subject":subject,
        "session_year":session,
        "action":action,
        "get_subject":get_subject,
        "get_session":get_session,
        "date":date,
        "attendance_report":attendance_report
    }

    return render(request,"hod/view_attendance.html",context)