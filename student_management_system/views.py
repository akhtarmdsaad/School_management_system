from django.http import HttpResponse
from django.shortcuts import redirect,render
from app.emailbackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Course,Session_Year

def BASE(request):
    return render(request,"base.html")

def LOGIN(request):
    return render(request,"login.html")

def PROFILE(request):
    user = CustomUser.objects.get(pk=request.user.id)
    context = {
        "user":user
    }
    return render(request,"profile.html",context)

def PROFILE_UPDATE(request):
    if request.method=="POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            custom_user = CustomUser.objects.get(pk=request.user.id)

            custom_user.first_name = first_name
            custom_user.last_name = last_name
            if password:
                custom_user.set_password(password)
            custom_user.profile_pic = profile_pic
            custom_user.save()
            messages.success(request,"Your Profile updated Successfully !!")

            return redirect("profile")
        except:
            messages.error(request,"Profile Updation Failed !!")

    return render(request,"profile.html")

def doLogin(request):
    print("14 Logged in")
    if request.method == "POST":
        user = EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        print("User:",user)
        print("\n\n")
        if user!=None:
            login(request,user)
            user_type = user.user_type
            print("19 Logged in")
            if user_type == "1":
                return redirect("hod_home")
            elif user_type == "2":
                return redirect("staff_home")
            elif user_type == "3":
                return redirect("student_home")
            else: 
                messages.error(request,"Email and Password are invalid!")
                return redirect("login")
        else:
            messages.error(request,"Email and Password are invalid!")
            return redirect("login")
    else:
        messages.error(request,"Request made must be POST to login")
        return redirect("login")

def doLogout(request):
    logout(request)
    return redirect("login")

