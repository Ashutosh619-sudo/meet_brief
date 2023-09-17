from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.UserCreate.as_view(), name='create-user'),

]