from django.shortcuts import redirect,render, HttpResponse
from app.models import Staff_Notification,Staff,Staff_Leave,Staff_Feedback, Student,Subject,Session_Year,Attendance,Attendance_report,StudentResult
from django.contrib import messages


def HOME(request):
    return render(request,"Staff/home.html")

def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

    notification = Staff_Notification.objects.filter(staff_id = staff_id)

    context = {
        "notifications":notification
    }
    return render(request,"staff/notifications.html",context)

def STAFF_NOTIFICATION_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()

    return redirect("notifications")

def APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id 

    staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

    context = {
        "staff_leave_history":staff_leave_history
    }

    return render(request,"staff/apply_leave.html",context)

def APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        date = request.POST.get("leave_date")
        message = request.POST.get("message")
        staff = Staff.objects.get(admin = request.user.id)
        leave = Staff_Leave(
            staff_id=staff,
            leave_date = date,
            message=message
        )

        leave.save() 
        messages.success(request,"Leave Applied successfully")

    return redirect("staff_apply_leave")

def STAFF_FEEDBACK(request):
    staff = Staff.objects.get(admin = request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id = staff)

    context = {
        "feedback_history":feedback_history
    }

    return render(request,"staff/feedback.html",context)

def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get("message")
        staff = Staff.objects.get(admin = request.user.id)
        fb = Staff_Feedback(
            staff_id = staff,
            feedback = feedback,
            feedback_reply = " "
        )
        fb.save()
    return redirect("staff_feedback")


def STAFF_TAKE_ATTENDANCE(request):
    staff = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff=staff)
    session = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject_id")
            session_id = request.POST.get("session_id")

            get_subject = Subject.objects.get(id= subject_id)
            get_session = Session_Year.objects.get(id = session_id)

            subject = Subject.objects.get(id=subject_id)
            course_id = subject.course.id
            students = Student.objects.filter(course_id = course_id)
    

    context = {
        "subject":subject,
        "session_year":session,
        "get_subject":get_subject,
        "get_session":get_session,
        "action":action,
        "students":students
    }
    return  render(request,"staff/take_attendance.html",context)

def STAFF_Save_ATTENDANCE(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        session_id = request.POST.get("session_id")
        attendance_date = request.POST.get("date")
        student_id = request.POST.getlist("student_id")
        get_subject = Subject.objects.get(id= subject_id)
        get_session = Session_Year.objects.get(id = session_id)

        attendance = Attendance(
            subject_id = get_subject,
            attendance_date=attendance_date,
            session_year_id = get_session,
        )
        attendance.save()
        for i in student_id:
            student = Student.objects.get(id=int(i))
            attendance_report = Attendance_report(
                student_id=student,
                attendance_id=attendance
            )
            attendance_report.save()

    return redirect("staff_take_attendance")

def STAFF_view_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id = staff_id)
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

    return render(request,"staff/view_attendance.html",context)

def STAFF_add_result(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id = staff_id)
    session = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject=None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session_Year.objects.get(id = session_id)
            course_id = get_subject.course.id  
            students = Student.objects.filter(course_id=course_id)

            
    context = {
        "session_year":session,
        "action":action,
        "get_subject":get_subject,
        "get_session":get_session,
        "subjects":subject,
        "students":students
    }
    return render(request,"staff/add_result.html",context)

def STAFF_save_result(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        print("\n"*4)
        print(subject_id)
        print("\n"*4)
        student_id = request.POST.get('student_id')
        assignment_marks = request.POST.get('assignment_marks')
        exam_marks = request.POST.get('exam_marks')
        get_subject = Subject.objects.get(id = subject_id)
        get_student = Student.objects.get(id = student_id)

        check_exist = StudentResult.objects.filter(subject_id = get_subject, student_id = get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(subject_id=get_subject,student_id=get_student) 
            result.assignment_mark = assignment_marks
            result.exam_mark = exam_marks
            if assignment_marks + exam_marks >= 50:
                result.status = "pass"
            else:
                result.status = "fail"
            result.save()
            messages.success(request,"Result Updated Successfully")
        else:
            result = StudentResult(subject_id=get_subject,
                                   student_id=get_student,
                                   assignment_mark = assignment_marks,
                                   exam_mark = exam_marks
                                )
            if assignment_marks + exam_marks >= 50:
                result.status = "pass"
            else:
                result.status = "fail"
            result.save()
            messages.success(request,"Result Added Successfully")

    return redirect('staff_add_result')