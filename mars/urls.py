from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:rover_name>/', views.get_mars_photo)
]
