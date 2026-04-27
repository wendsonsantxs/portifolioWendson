from django.urls import path
from . import views
from portifolio import *

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
]