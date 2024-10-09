from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.registration, name="registration"),
    path('logout/', views.logout, name='logout')
]
