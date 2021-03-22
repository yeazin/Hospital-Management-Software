from django import forms
from .models import Employee_Profile, Doctor_Profile, Degree,Patient,Package, Department

# Employee forms
class Employee_Profile_Forms(forms.ModelForm):
    class Meta:
        model = Employee_Profile
        fields = ['user','name', 'email','address','contact','status']
        widgets = {
            'user': forms.Select(attrs = {'class':'form-control'}),
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'email':forms.EmailInput(attrs= {'class':'form-control'}),
            'address':forms.Textarea(attrs= {'class':'form-control'}),
            'contact':forms.TextInput(attrs= {'class':'form-control'}),
            'status':forms.Select(attrs= {'class':'form-control'}),
            

        }


class Doctor_Profile_Forms(forms.ModelForm):
    class Meta:
        model = Doctor_Profile
        fields = ['user', 'name','contact','address','degree','department']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            
            

        }

# Degree forms

class Degree_Form(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

# Patient Forms

class Patient_Form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
        'patient_name',
        'gender',
        'age',
        'month',
        'bed_no',
        'address',
        'phone',
        'problem',
        'assign_doctor',
        'patient_father_name',
        'patient_mother_name',
        'guardian_name',
        'guardian_phone_no'
        ]
        widgets = {
            'patient_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Type the name of Patient'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Select Gender'}),
            'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Type Age'}),
            'month':forms.NumberInput(attrs={'class':'form-control','placeholder':'Type months'}),
            'bed_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Type Bed No'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Type Address'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Type Phone Number'}),
            'problem':forms.Textarea(attrs={'class':'form-control','placeholder':'Tell about your problem'}),
            'assign_doctor':forms.Select(attrs={'class':'form-control','placeholder':'Doctor'}),
            'patient_father_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Type Patient`s Father`s Name'}),
            'patient_mother_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Type Patient`s Mother`s Name'}),
            'guardian_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Type Guardian Name'}),
            'guardian_phone_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Type Guardian Phone Number'}),




        }

# package form 

class Package_Form(forms.ModelForm):
    class Meta:
        model = Package

        #price = forms.IntegerField()
        #price.widget.attrs.update({'class':'form-control','placeholder':'Package Price'})
        fields = ['name', 'detail','price']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Package Name'}),
            'detail':forms.Textarea(attrs={'class':'form-control','placeholder':'Package Details'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Package Details'})
            
        }

# Department Form

class Department_Form(forms.ModelForm):
    class Meta:
        model = Department
        name = forms.CharField()
        name.widget.attrs.update({'class':'form-control','placeholder':'Department Name'})
        fields = ['name']



