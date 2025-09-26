from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # CRUD: Patients
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient_delete'),

    # CRUD: Doctors
    path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
    path('doctors/create/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor_delete'),

    # CRUD: Appointments
    path('appointments/', views.AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/create/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),

    # CRUD: Bills
    path('bills/', views.BillListView.as_view(), name='bill_list'),
    path('bills/create/', views.BillCreateView.as_view(), name='bill_create'),
    path('bills/<int:pk>/update/', views.BillUpdateView.as_view(), name='bill_update'),
    path('bills/<int:pk>/delete/', views.BillDeleteView.as_view(), name='bill_delete'),
]
