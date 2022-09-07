# from re import template
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('administracion/', views.AdministracionView.as_view(), name='administracion'),
    path('administracion/actualizar_tablas/', views.ActualizarTablasView.as_view(), name='actualizar_tablas'), 
]
