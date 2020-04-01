from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from Application.views import application
from Application.views import home
from django.core.mail import send_mail
from random import sample

def register(request):
    if request.method == "POST":
        ufname = request.POST['first-name']
        ulname = request.POST['last-name']
        uemail = request.POST['email']
        uname = request.POST['username']
        upass = request.POST['password']
        ucpass = request.POST['confirm-password']
        if upass == ucpass:
            try:
                user = User.objects.get(username=uname)
                return render(request, 'register.html', {"messgae": "Username you used already exists!"})
            except User.DoesNotExist:
                u = User.objects.create_user(first_name= ufname, last_name=ulname, email=uemail, username=uname, password=upass)
                u.save()
                send_mail("Welcome To Notely", "Thank you for using our service", "sanketvy7@gmail.com", [uemail])
                return render(request, 'register.html', {"messgae": "You have been successfully registered"})
        else:
            return render(request, 'register.html', {"messgae": "Your password doesn't match"})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        uname= request.POST['username']
        upass = request.POST['password']
        user = auth.authenticate(username=uname, password=upass)
        if user is not None:
            auth.login(request, user)
            return redirect('application')
        else:
            return render(request, 'login.html', {"message": "Your username or password is incorrect"})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect(home)


def forgot(request):
    if request.method == "POST":
        uemail = request.POST['email']
        u = User.objects.get(email=uemail)
        pstring = "abcdefghijklmnopqrstuvwxyz1234567890@$"
        password = sample(pstring, 10)
        passw = "".join(password)
        uname = u.first_name
        u.set_password(passw)
        u.save()
        message = "Hello " + uname + ",\n As per your request, we have changed your password. Your new password is : "+passw + ".\n You can login and change your account password from your Dashboard"
        send_mail("Password Reset- NoteDown", message, "sanketvy7@gmail.com", [uemail, ])
        return render(request, 'login.html', {"message": "Your new password is emailed to your registered mobile number"})
    else:
        return render(request, 'reset.html')


def change(request):
    if request.method == "POST":
        cpass = request.POST['current-password']
        npass = request.POST['new-password']
        cnpass = request.POST['confirm-new-password']
        loged_user = request.user
        u = auth.authenticate(username=loged_user, password=cpass)
        if u is not None:
            if npass == cnpass:
                u.set_password(cnpass)
                u.save()
                return render(request, 'login.html', {"message": "Your password successfully changed!"})
            else:
                return render(request, 'change.html', {"message": "Your new passwords didn't matched"})
        else:
            return render(request, 'change.html', {"message": "Your current Password didn't matched"})
    else:
        name = request.user
        name = name.first_name
        return render(request, 'change.html', {"name":name})