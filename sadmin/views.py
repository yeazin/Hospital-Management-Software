from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Employee_Profile_Forms, Degree_Form, Doctor_Profile_Forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Degree, Doctor_Profile, Employee_Profile


# HomeView 
def HomeView(request):

        
    context ={}
    return render (request, 'index.html', context)


# User Login View 
def LoginView(request):
    if request.user.is_authenticated:
        return redirect ('dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password = password)
            if user is not None:
                login (request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Sorry Usernme or Password didn`t Match')
    context ={}
    return render (request, 'login.html', context)

# Admin dashboard Views 
@login_required
def DashboardView(request):
    if request.user.is_authenticated:
        user = request.user
    context = {'user':user}
    return render(request, 'dashboard.html', context)


def Logout_User(request):
    logout(request)
    return redirect('/')


# Employee Create View 
@login_required
def EmployeeCreate(request):
    if request.user.is_authenticated:
        forms = Employee_Profile_Forms()
        if request.method == "POST":
            forms  = Employee_Profile_Forms(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect ('dashboard')
    else:
        return redirect('login')
    context = {'forms':forms }
    return render (request, 'create_employee.html', context)

# User create View
@login_required
def CreateUserView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.all().filter(username= username)
            if user :
                messages.info(request,'Username already Exits !')
                return redirect ('user_create')
            else:
                create_user = {
                    'username':username,
                    'email': email,
                    'password':make_password(password)
                }
                user = User(**create_user)
                user.save()
                return redirect ('userlist')


    else:
        return redirect('login')
    context = {}
    return render  ( request, 'create_user.html', context)

# Users list Views
@login_required
def UserListView(request):
    if request.user.is_authenticated:
        users = User.objects.all().order_by('-id')
    else:
        return redirect ('login')
    context={'users':users}
    return render(request,'userlist.html', context)


### use delete views
@login_required

def UserDeleteView(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        user.delete()
        return redirect('userlist')
    context = {'user':user}
    return render(request,'delete_user.html', context)



# doctor create View

@login_required
def DoctorCreateView(request):
    if request.user.is_authenticated:
        forms = Doctor_Profile_Forms()
        if request.method == "POST":
            forms = Doctor_Profile_Forms(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect ('doctorlist')
    else:
        return redirect ('login')

    context = {'forms':forms}
    return render(request, 'create_doctor.html', context)

# Creating Degree
@login_required
def DegreeCreateView(request):
    if request.user.is_authenticated:
        forms = Degree_Form()
        if request.method == "POST":
            forms = Degree_Form(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect ('degreelist')
    else:
        return redirect('login')
    
    context = {'forms': forms}
    return render(request, 'create_degree.html', context )

# for showing degree list 
@login_required
def DegreeListView(request):
    degree = Degree.objects.all().order_by('-id')
    context = {'degree':degree}
    return render (request, 'degreelist.html', context)

# degree edit view
@login_required 
def DegreeEdit(request, pk ):
    degree = Degree.objects.get(id=pk)
    form = Degree_Form(instance=degree)

    if request.method == "POST":
        form = Degree_Form (request.POST, instance=degree)
        if form.is_valid():
            form.save()
            return redirect ('degreelist')

    context = {'form':form}
    return render (request, 'degree_edit.html', context)


# for deleting Degree
@login_required
def DeleteDegreeView(request, pk):
    degree = Degree.objects.get(id=pk)
    if request.method == "POST":
        degree.delete()
        return redirect ('degreelist')
    context = {'degree':degree}
    return render (request, 'delete_degree.html', context)





        
