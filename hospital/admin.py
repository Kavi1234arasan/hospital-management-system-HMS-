from django.contrib import admin

# Register your models here.

from .models import Patient, Doctor, Appointment, Bill, Profile

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Bill)
admin.site.register(Profile)
