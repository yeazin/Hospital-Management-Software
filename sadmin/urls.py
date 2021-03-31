from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views 

urlpatterns = [
   path('', views.HomeView.as_view(), name='home'),
   path('dashboard/', views.DashboardView, name= 'dashboard' ),
   path('logout/', views.Logout_User, name='logout'),
   path('login/', views.LoginView, name ='login'),
   # User Path
   path('create_user/', views.CreateUserView, name ='user_create'),
   path('userlist/', views.UserListView, name='userlist'),
   path('delete_user/<str:pk>', views.UserDeleteView, name='delete_user'),
   # Doctors Path 
   path('create_doctor/', views.DoctorCreateView, name='doctor_create'),
   path('doctor_list/', views.DoctorListView, name='doctorlist' ),
   path('doctor/<str:pk>',views.DoctorSingleView, name="doctor" ),
   path('create_degree/', views.DegreeCreateView, name='degree_create'),
   path('delete_doctor/<str:pk>', views.DoctorDeleteView, name="delete_doctor"),
   # Degree Path
   path('degreelist/', views.DegreeListView, name='degreelist'),
   path('edit_degree/<str:pk>', views.DegreeEdit, name='edit_degree'),
   path('delete_degree/<str:pk>', views.DeleteDegreeView, name="delete_degree"),
   # Patient Path
   path('create_patient/', views.PatientCreateView, name='create_patient'),
   path('patient_list/', views.PatientListView, name='patient_list'),
   path('delete_patient/<str:pk>', views.PatientDeleteView, name='delete_patient'),
   path('edit_patient/<str:pk>', views.PatientEditView, name = 'edit_patient'),
   path('patient/<str:pk>', views.PatientSingleView, name = 'patient'),
   # Employee Path 
   path('create_employee/', views.EmployeeCreate, name ='create'),
   # packages Path
   path('create_package/', login_required(login_url='login')(views.PackageCreateView.as_view()), name='create_package'),
   path('package_list/',login_required(login_url='login') (views.PackageListView.as_view()), name = 'packagelist'),
   # pdf view path
   path('package_list/<str:pk>', views.PackagePdfView, name='pdf'),


   


]