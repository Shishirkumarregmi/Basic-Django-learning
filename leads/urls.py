from .views import  lead_list,lead_detail,lead_create
from django.urls import path

urlpatterns = [
    path('', lead_list,name='Home'),
    path('<int:pk>/', lead_detail,name='Details'),
    path('create/', lead_create,name='Create'),
]
