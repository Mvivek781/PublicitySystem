from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Events

# Create your views here.
def home(request):
    return render(request,"publicity/PMMS.html")

def register(request):
    if request.method=="POST":
        name=request.POST['fullname']
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if(password==cpassword):
            if User.objects.filter(username=uname).exists():
                messages.warning(request,'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,email=email,password=password,first_name=name)
                user.save()

                messages.success(request, 'Sucessfully Registerd')
                return render(request,'login/login.html')
        else:
            messages.warning(request, 'Passwords are not matching')
            return redirect('register')
    return render(request,"publicity/SignUp.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return main(request)
        else:
            messages.error(request,'Invalid Credintials')
            return redirect('login')
    return render(request,"publicity/Login.html")

def aboutus(request):
    return render(request,"publicity/aboutus.html")

def main(request):
    Ev=Events.objects.all()
    print(Ev)
    return render(request,"publicity/main.html",{"event":Ev})

def uservisit(request):
    if request.method=="POST":
        iname=request.POST['iname']
        return render(request, "publicity/uservisit.html", {"iname": iname})
    else:
        return render(request,"publicity/uservisit.html")


def contactus(request):
    return render(request,"publicity/contact.html")

def rating(request):
    return render(request,"publicity/rating.html")

def payment(request):
    return render(request,"publicity/payment.html")