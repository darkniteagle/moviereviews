from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/', views.signupaccount, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccout'),
    path('login/', views.loginaccount, name='loginaccount'),
]