from django import forms
from .models import Employee_Profile, Doctor_Profile, Degree


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
        fields = ['user', 'name','contact','address','degree']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            
            

        }

class Degree_Form(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }



