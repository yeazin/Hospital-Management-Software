from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Degree, Doctor_Profile, Employee_Profile, Patient, Package, Department
from .forms import Employee_Profile_Forms, Degree_Form, Doctor_Profile_Forms,Patient_Form, Package_Form, Department_Form
# for pff import 
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View


# HomeView 
class HomeView(View):
    def get(self, request,*args, **kwargs):
        context ={}
        return render (request, 'home/index.html', context)
        



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
    return render (request, 'home/login.html', context)

# Admin dashboard Views 
@login_required
def DashboardView(request):
    if request.user.is_authenticated:
        user = request.user
        # query 
        doctor = Doctor_Profile.objects.all().order_by('-id')[:4]
        user = User.objects.all().order_by('-id')[:4]
        employee = Employee_Profile.objects.all().order_by('-id')[:4]
        patient = Patient.objects.all().order_by('-id')[:4]
        #count
        doctor_count = Doctor_Profile.objects.all().count()
        user_count   = User.objects.all().count()
        employee_count  = Employee_Profile.objects.all().count()
        patient_count   = Patient.objects.all().count()
    else:
        return redirect('login')
    context = {
        'user':user,
        'doctor_count':doctor_count,
        'user_count': user_count,
        'employee_count':employee_count,
        'patient_count':patient_count,
        'doctor':doctor,
        'user':user,
        'employee':employee,
        'patient':patient
                }
                
    return render(request, 'home/dashboard.html', context)


def Logout_User(request):
    logout(request)
    return redirect('/')


 
# packages views - create-update-single-list-delete-pdf

# Create Package functions 
@login_required
def PackageCreateView(request):
    if request.user.is_authenticated:
        form = Package_Form()
        if request.method == "POST":
            form = Package_Form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('packagelist')
            else:
                form = Package_Form()
    else:
        return redirect('login')
    context = {'form':form}
    return render(request, 'package/create_package.html', context)

# for showing list of packages
@login_required
def PackageListView(request):
    packages = Package.objects.all().order_by('-id') 
    
    context = {'packages': packages}
    return render (request, 'package/package_list.html', context)




# pdf views

def PackagePdfView(request, pk):
    template_path = 'pdf/packagepdf.html'
    p = Package.objects.get(id=pk)
    context = {'p': p}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# Employee Views - create-update-delete-single-list

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
    return render (request, 'employee/create_employee.html', context)

#Employee list view 
@login_required


############################### User views functions ########################

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
    return render  ( request, 'user/create_user.html', context)

# Users list Views
@login_required
def UserListView(request):
    if request.user.is_authenticated:
        users = User.objects.all().order_by('-id')
    else:
        return redirect ('login')
    context={'users':users}
    return render(request,'user/userlist.html', context)


### use delete views
@login_required

def UserDeleteView(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        user.delete()
        return redirect('userlist')
    context = {'user':user}
    return render(request,'user/delete_user.html', context)

# Doctor views - create-update-delete-list-single
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
    return render(request, 'doctor/create_doctor.html', context)

# Doctor List View

@login_required
def DoctorListView(request):
    list = Doctor_Profile.objects.all().order_by('-id')

    context = {'list':list}
    return render(request, 'doctor/doctor_list.html', context)

# Doctor Single View
@login_required
def DoctorSingleView(request,pk):
    doctor =  Doctor_Profile.objects.get(id=pk)

    context = {'doctor':doctor }
    return render (request, 'doctor/doctor.html', context )

# doctor delete View
@login_required
def DoctorDeleteView(request, pk):
    doctor = Doctor_Profile.objects.get(id=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect ('doctorlist')
    context= {'doctor':doctor}
    return render (request, 'doctor/delete_doctor.html', context)


# Degree views -create-update-delete-single-list
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
    return render(request, 'degree/create_degree.html', context )

# for showing degree list 
@login_required
def DegreeListView(request):
    degree = Degree.objects.all().order_by('-id')
    context = {'degree':degree}
    return render (request, 'degree/degreelist.html', context)

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
    return render (request, 'degree/degree_edit.html', context)


# for deleting Degree
@login_required
def DeleteDegreeView(request, pk):
    degree = Degree.objects.get(id=pk)
    if request.method == "POST":
        degree.delete()
        return redirect ('degreelist')
    context = {'degree':degree}
    return render (request, 'degree/delete_degree.html', context)


# Patient Views

# for creating Patient 
@login_required

def PatientCreateView(request):
    if request.user.is_authenticated:
        form = Patient_Form()
        if request.method == "POST":
            form = Patient_Form(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('patient_list')
    else:
        return redirect('login')
    
    context = {'form':form}
    return render(request, 'patient/create_patient.html', context)

# for showing list of Patient
@login_required
def PatientListView(request):
    plist = Patient.objects.all().order_by('-id')

    context = {'plist': plist}
    return render (request,'patient/patient_list.html', context)

# for deleting Patient 
@login_required
def PatientDeleteView(request, pk):
    patient = Patient.objects.get(id=pk)

    if request.method == "POST":
        patient.delete()
        return redirect ('patient_list')

    context = {"patient":patient}
    return render (request,'patient/delete_patient.html', context )

# for editing Patiend 

@login_required
def PatientEditView(request, pk):
    p = Patient.objects.get(id=pk)
    form = Patient_Form(instance=p)

    if request.method == "POST":
        form = Patient_Form(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('patient_list')

    context = {"form":form}
    return render (request, 'patient/edit_patient.html', context )

#for showing single Patient

@login_required
def PatientSingleView(request, pk):
    p = Patient.objects.get(id = pk )
    context = {"p":p}
    return render (request,'patient/patient.html', context)



    





    










        
