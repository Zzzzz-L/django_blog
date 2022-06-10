# 引入path
from django.urls import path
# 引入views
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.RegisterView, name='register'), ]
