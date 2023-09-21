from django.urls import path
from . import views

urlpatterns = [
    path('up-down-caption/', views.DownUpCaption.as_view(), name='down-up-caption'),
    path('meetings/', views.MeetingsListCreate.as_view(), name='create-list'),
    path('meetings/<int:pk>/', views.MeetingsRetreiveUpdate.as_view(), name='retreive-update')

]