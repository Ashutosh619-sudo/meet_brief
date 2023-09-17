from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='create-user'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login')

]