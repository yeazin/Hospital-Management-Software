
from django.urls import path, include
from . import views 

urlpatterns = [
   path('', views.HomeView, name='home'),
   path('dashboard/', views.DashboardView, name= 'dashboard' ),
   path('logout/', views.Logout_User, name='logout'),
   path('login/', views.LoginView, name ='login'),
   path('create_employee/', views.EmployeeCreate, name ='create'),
   path('create_user/', views.CreateUserView, name ='user_create'),
   path('userlist/', views.UserListView, name='userlist'),
   path('delete_user/<str:pk>', views.UserDeleteView, name='delete_user'),
   path('create_doctor/', views.DoctorCreateView, name='doctor_create'),
   path('create_degree/', views.DegreeCreateView, name='degree_create'),
   path('degreelist/', views.DegreeListView, name='degreelist'),
   path('edit_degree/<str:pk>', views.DegreeEdit, name='edit_degree'),
   path('delete_degree/<str:pk>', views.DeleteDegreeView, name="delete_degree")


]