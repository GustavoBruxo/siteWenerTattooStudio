from django.urls import path
from .views import *

urlpatterns = [
    path('agenda/', agenda, name='agenda'),
    path('criar_agenda/', criar_agenda, name='criar_agenda'),
]
