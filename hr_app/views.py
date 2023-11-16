from django.shortcuts import render,redirect
from .models import Person
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url="/login")
def home(request):
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'base.html',context ) #ชื่อไฟล์ที่จะแสดง

@login_required(login_url="/login")
def add(request): #ชื่อฟังชั่น
    if request.method == 'POST':
        p_firstname = request.POST['firstname']
        p_lastname = request.POST['lastname']
        p_startOfWork = request.POST['startOfWork']
        p_endOfWork = request.POST['endOfWork']
        p_idLine = request.POST['idLine']
        p_position = request.POST['position']
        p_salary = request.POST['salary']
        p_status = request.POST['status']
        p_picture = request.FILES['picture']

        person = Person(
            p_firstname=p_firstname,
            p_lastname=p_lastname,
            p_startOfWork=p_startOfWork,
            p_endOfWork=p_endOfWork,
            p_idLine=p_idLine,
            p_position=p_position,
            p_salary=p_salary,
            p_status=p_status,
            p_picture=p_picture
        )
        person.save()
        return redirect('/list')
    return render(request,'add.html') #ชื่อไฟล์ที่จะแสดง

@login_required(login_url="/login")
def list(request): #ชื่อฟังชั่น
    person_qry = Person.objects.all()
    context = {'person':person_qry}
    return render(request,'list.html',context ) #ชื่อไฟล์ที่จะแสดง


def manage(request):
    return render(request,'manage.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/list')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
            pass
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request,'login.html')
