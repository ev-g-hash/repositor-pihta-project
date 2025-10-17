from django.urls import path
from main_app import views


urlpatterns = [
    path('', views.index), 
    path('aboutas/', views.aboutas),
]