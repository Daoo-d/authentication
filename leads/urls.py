from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_lead,name='add_lead')
]
