from django.contrib import admin
from .models import State, Drug, Prescriber, Prescriber_Drug, Specialty, Credential, Prescriber_Credential

# Register your models here.
admin.site.register(State)
admin.site.register(Drug)
admin.site.register(Prescriber)      
admin.site.register(Prescriber_Drug) 
admin.site.register(Prescriber_Credential) 
admin.site.register(Specialty) 
admin.site.register(Credential) 
