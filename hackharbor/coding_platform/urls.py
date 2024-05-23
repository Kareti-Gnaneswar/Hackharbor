from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('career/', views.career, name='career'),
    path('Login/', views.Login, name='Login'),
    path('signup/', views.signup, name='signup'),
    path('Learning/', views.Learning, name='Learning'),
    path('contest/', views.contest, name='contest'),
    path('hiring/', views.hiring, name='hiring'),
]