from django.urls import path
from .views import CustomUserCreateView, CustomUserDetailView, ProfileCreateView, ProfileDetailView

urlpatterns = [
    path('customusers/', CustomUserCreateView.as_view()),
    path('customusers/<pk>/', CustomUserDetailView.as_view()),
    path('profile/', ProfileCreateView.as_view()),
    path('profile/<pk>/', ProfileDetailView.as_view()),
]