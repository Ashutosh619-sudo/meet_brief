from django.urls import path
from . import views

urlpatterns = [
    path('upload-caption/', views.Caption.as_view(), name='upload-caption'),
    path('meetings/', views.MeetingsListCreate.as_view(), name='create-list'),
    path('meetings/<int:pk>/', views.MeetingsRetreiveUpdate.as_view(), name='retreive-update')

]