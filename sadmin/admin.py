from django.contrib import admin
from .models import Employee_Profile, Degree, Doctor_Profile, Patient


class Employee_Profile_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status','contact')
    ordering = ['-created_at']
    search_fields = ('name','email')

admin.site.register(Employee_Profile, Employee_Profile_Admin)

admin.site.register(Degree)

class Doctor_Profile_Admin(admin.ModelAdmin):
    list_display = ('name', 'email','contact','created_at')
    ordering = ['-created_at']
    search_fields = ('name', 'email', 'contact')

admin.site.register(Doctor_Profile, Doctor_Profile_Admin)

class Patient_Admin(admin.ModelAdmin):
    list_display = ('patient_name','gender','admit_date','bed_no','phone')
    ordering = ['-admit_date']
    search_fields = ('patient_name', 'bed_no','phone','gender')

admin.site.register(Patient, Patient_Admin)