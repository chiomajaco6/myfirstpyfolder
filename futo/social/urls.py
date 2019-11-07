from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'social-home'),
    path('about/', views.about, name = 'social-about'),
]
