from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/<pk>/', views.profile, name='profile'),
    path('api/',include('card.api.urls')),
]