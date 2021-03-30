from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




# Income model

class IncomeModel(models.Model):
    name   =   models.CharField(max_length=200, blank=False, null=True, verbose_name='Income Name')
    amount =   models.IntegerField(verbose_name='Amount')
    date    =   models.DateField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Income Detail'

# Expenses Model 

class ExpenseModel(models.Model):
    name    =   models.CharField(max_length=200, blank=False, null=True, verbose_name='Expenses Name')
    amount  =   models.IntegerField(verbose_name='Amount')
    date    =   models.DateField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Expense Detail"

# Home rent model

class HomeRent(models.Model):
    month       =   models.DateField(auto_now_add=False, verbose_name='Month`s Name')
    paid_by     =   models.CharField(max_length=200, blank=False, null=True, verbose_name='Paid By')
    paid_to     =   models.CharField(max_length=200, blank=True, null=True, verbose_name='Paid To')
    amount      =   models.IntegerField(verbose_name='Total Amount')
    is_paid     =   models.BooleanField(default=False, verbose_name='Paid or Not')
    
    def __str__(self):
        return self.paid_by

    class Meta:
        verbose_name = "Rent Cost Per Month"

# Employee Model

class Employee_Profile(models.Model):
    status      =   (
        ('active', 'active'),
        ('pending','pending'),
        ('rejected','rejected')
    )
    user        =   models.ForeignKey(User, on_delete = models.DO_NOTHING)
    name        =   models.CharField(max_length=100, blank=False)
    email       =   models.EmailField(null=True, blank=True)
    address     =   models.TextField(max_length=300, blank=True)
    contact     =   models.CharField(max_length=11, blank=False)
    status      =   models.CharField(max_length=8,choices=status)
    is_deleted  =   models.BooleanField(default=False)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
    
    class Meta:     
        verbose_name_plural = 'Employee Profiles'

    def __str__(self):
        return self.name 

# Employee Salary 
class EmployeeSalary(models.Model):
    employee        =   models.ForeignKey(Employee_Profile, on_delete=models.DO_NOTHING, verbose_name='Employee')
    salary          =   models.IntegerField(verbose_name='Salary Payable')
    date            =   models.DateField(verbose_name='Salaray Date', blank=True)
    is_paid         =   models.BooleanField(default=False, verbose_name='paid Salary')

    def __str__(self):
        return f"{self.employee} | {self.salary}" 

    class Meta:
        verbose_name = 'Employee Salary'

# Degree Model
class Degree(models.Model):
    name        =   models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

# Doctor Department Model
class Department(models.Model):
    name        =   models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.name 


# doctor profile model 

class Doctor_Profile(models.Model):
    user        =   models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name        =   models.CharField(max_length=200, blank=False)
    designation =   models.CharField(max_length=200, verbose_name='Designation',blank=True, null=True)
    email       =   models.EmailField(null=True,blank=True)
    address     =   models.TextField(max_length=300, blank=True)
    department  =   models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, related_name='department')
    degree      =   models.ManyToManyField(Degree, related_name='degree')
    #appointment =   models.ForeignKey(add,on_delete=models.DO_NOTHING, null=True, verbose_name='Appoinments')
    contact     =   models.CharField(max_length=11,blank=False)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
    is_approved =   models.BooleanField(default=False, verbose_name='Approve status')

    class Meta:
        verbose_name_plural =  "Doctor`s Profile"
        
    def __str__(self):
        return self.name 


# Doctor Salary
class DoctorSalary(models.Model):
    doctor      =   models.ForeignKey(Doctor_Profile, on_delete=models.DO_NOTHING, verbose_name='Doctor')
    salary      =   models.IntegerField(verbose_name='Salary Payable')
    date        =   models.DateField(blank=True,verbose_name='Salary Date')
    is_paid     =   models.BooleanField(default=False, verbose_name='Paid Salary')

    def __str__(self):
        return f"{self.doctor} | {self.salary}" 
    
    class Meta:
        verbose_name = 'Doctor Salary'

    
# Package class Model

class Package(models.Model):
    name        =   models.CharField(max_length=200,verbose_name='Package Name')
    detail      =   models.TextField(max_length=400, blank=True, verbose_name='Package details')
    price       =   models.IntegerField(verbose_name='Package Price', default="00")
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =" Packages "


# Patient Model  
class Patient(models.Model):
    gender = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    patient_name        =   models.CharField(max_length=200, blank=False, verbose_name='Patient Name')
    gender              =   models.CharField(max_length=10, choices=gender, blank=False, default='Male')
    age                 =   models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)], blank=False, null=True)
    month               =   models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(0)], blank=True, null=True)
    admit_date          =   models.DateTimeField(auto_now_add=True,verbose_name='Admition Date')
    bed_no              =   models.CharField(max_length=20, verbose_name='Bed No.')
    address             =   models.TextField(max_length=300, blank=True)
    phone               =   models.CharField(max_length=11, blank=True)
    problem             =   models.TextField(max_length=300, blank=True)
    assign_doctor       =   models.ForeignKey(Doctor_Profile, on_delete=models.DO_NOTHING, related_name='doctor')
    patient_father_name =   models.CharField(max_length=100, verbose_name='Father`s Name')
    patient_mother_name =   models.CharField(max_length=100, verbose_name='Mother`s Name')
    guardian_name       =   models.CharField(max_length=100, blank=True, verbose_name='Guardian Name')
    guardian_phone_no   =   models.CharField(max_length=11, blank=True, verbose_name='Guardian`s Phone Number')
    is_leave            =   models.BooleanField(default=False, verbose_name='Leave Patient')

    def __str__(self):
        return self.patient_name 

    class Meta:
        verbose_name_plural = "Patients"

# Doctor Appointment Model
class Appointment(models.Model):
    status = (
        ('New Visit','New Visit'),
        ('Renew Visit', 'Renew Visit')
    )
    doctor      =   models.ForeignKey(Doctor_Profile, on_delete=models.DO_NOTHING, verbose_name='Doctor Name')
    patient     =   models.ForeignKey(Patient, on_delete=models.DO_NOTHING, verbose_name='Patient Name', null=True)
    visit_type  =   models.CharField(max_length=20,blank=False,null=True,verbose_name='Visit Type', choices=status)
    ref         =   models.CharField(max_length=100,blank=True, null=True, verbose_name='Reference By')
    date        =   models.DateTimeField(auto_now_add=False, verbose_name='Appointment Date')
    visit       =   models.BooleanField(default=False, verbose_name='Finished Appointment')

    def __str__(self):
        return f"{self.doctor} | {self.date}"

    
        


