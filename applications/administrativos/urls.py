from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdministrativosView.as_view(), name='administrativos'),
    path('agregar/', views.AdministrativosAgregarFormView.as_view(), name='agregar_administrativo'),
    path('eliminar/<int:pk>/', views.AdministrativoDeleteView.as_view(), name='eliminar_administrativo'),
]
