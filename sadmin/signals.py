from .models import Appointment, Doctor_Patient_Count
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Appointment)

def Add_Patient_to_Doctor(sender,instance,created,**kwargs):
    if created:

        Doctor_Patient_Count.objects.create( doctor = instance)

    
    

