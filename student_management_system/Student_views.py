from django.shortcuts import redirect, render, HttpResponse
from app.models import Attendance, Attendance_report, Student_Notification, Student, Student_Feedback, Student_Leave, Subject,StudentResult
from django.contrib import messages


def HOME(request):
    return render(request, "student/home.html")


def NOTIFICATIONS(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

    notification = Student_Notification.objects.filter(student_id=student_id)

    context = {
        "notifications": notification
    }
    return render(request, "student/notifications.html", context)


def STUDENT_NOTIFICATION_AS_DONE(request, status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect("student_notifications")


def Student_FEEDBACK(request):
    student = Student.objects.get(admin=request.user.id)

    feedback_history = Student_Feedback.objects.filter(student_id=student)

    context = {
        "feedback_history": feedback_history
    }

    return render(request, "student/feedback.html", context)


def Student_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get("message")
        student = Student.objects.get(admin=request.user.id)
        fb = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply=" "
        )
        fb.save()
    return redirect("student_feedback")


def APPLY_LEAVE(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

    student_leave_history = Student_Leave.objects.filter(student_id=student_id)

    context = {
        "student_leave_history": student_leave_history
    }

    return render(request, "student/apply_leave.html", context)


def APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        date = request.POST.get("leave_date")
        message = request.POST.get("message")
        student = Student.objects.get(admin=request.user.id)
        leave = Student_Leave(
            student_id=student,
            leave_date=date,
            message=message
        )

        leave.save()
        messages.success(request, "Leave Applied successfully")

    return redirect("student_apply_leave")


def Student_view_ATTENDANCE(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course=student.course_id)
    action = request.GET.get('action')
    at_report = None
    get_subject = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get("subject_id")
            print(subject_id)
            get_subject = Subject.objects.get(id = subject_id)
            print(get_subject)
            attendance = Attendance.objects.get(subject_id = get_subject)
            at_report = Attendance_report.objects.filter(student_id = student, attendance_id = attendance)
    context = {
        "subjects": subjects,
        "action": action,
        "get_subject":get_subject,
        "attendance_report":at_report
    }
    return render(request, "student/view_attendance.html", context)

def Student_view_result(request):
    student = Student.objects.get(admin=request.user.id)
    result = StudentResult.objects.filter(student_id = student)
    mark = 0
    for i in result:
        assignment_mark = i.assignment_mark 
        exam_mark = i.exam_mark

        mark = assignment_mark + exam_mark 

    context = {
        "result":result,
        "mark":mark
    }
    return render(request,"student/view_result.html",context)