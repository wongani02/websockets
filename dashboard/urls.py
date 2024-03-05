from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<slug:slug>/', views.dashboard, name='dashboard'),
]