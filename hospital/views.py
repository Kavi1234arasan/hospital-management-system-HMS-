from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Patient, Doctor, Appointment, Bill, Profile
from .forms import RegistrationForm, PatientForm, DoctorForm, AppointmentForm, BillForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']
            profile = user.profile  # created by signal
            profile.role = role
            profile.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def dashboard(request):
    role = request.user.profile.role if hasattr(request.user, 'profile') else 'PATIENT'
    context = {
        'role': role,
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'appointment_count': Appointment.objects.count(),
        'bill_count': Bill.objects.count(),
    }
    template = {
        'ADMIN': 'dashboards/admin_dashboard.html',
        'DOCTOR': 'dashboards/doctor_dashboard.html',
        'PATIENT': 'dashboards/patient_dashboard.html',
    }.get(role, 'dashboards/patient_dashboard.html')
    return render(request, template, context)

# CRUD Classes
class PatientListView(ListView):
    model = Patient
    template_name = 'patients/list.html'
    context_object_name = 'patients'

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/confirm_delete.html'
    success_url = reverse_lazy('patient_list')

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/list.html'
    context_object_name = 'doctors'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctors/confirm_delete.html'
    success_url = reverse_lazy('doctor_list')

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/list.html'
    context_object_name = 'appointments'

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/confirm_delete.html'
    success_url = reverse_lazy('appointment_list')

class BillListView(ListView):
    model = Bill
    template_name = 'bills/list.html'
    context_object_name = 'bills'

class BillCreateView(CreateView):
    model = Bill
    form_class = BillForm
    template_name = 'bills/form.html'
    success_url = reverse_lazy('bill_list')

class BillUpdateView(UpdateView):
    model = Bill
    form_class = BillForm
    template_name = 'bills/form.html'
    success_url = reverse_lazy('bill_list')

class BillDeleteView(DeleteView):
    model = Bill
    template_name = 'bills/confirm_delete.html'
    success_url = reverse_lazy('bill_list')



    # hospital/views.py
from django.views.generic import ListView
from .models import Doctor

class DoctorListView(ListView):
    model = Doctor
    template_name = 'hospital/doctor_list.html'  # Must match the path
    context_object_name = 'doctors'

