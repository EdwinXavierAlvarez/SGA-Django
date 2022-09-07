from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, DeleteView
from django.views.generic import View, ListView
from django.urls import reverse_lazy

from applications.administrativos.models import Administrativo
from applications.core.models import Persona
from .forms import AgregarAdministrativoForm

from applications.core.utils import bad_json, calcular_username, generar_usuario

from sga.settings import ADMINISTRATIVOS_GROUP_ID, EMAIL_DOMAIN, EMAIL_INSTITUCIONAL_AUTOMATICO, NACIONALIDAD_ECUADOR_ID, PAIS_ECUADOR_ID

# Create your views here.
class AdministrativosView(LoginRequiredMixin,ListView):

    model = Administrativo
    template_name = 'administrativos/index.html'
    context_object_name = 'data'

    # def get(self, request):
    #     data = {}
    #     data["title"] = "Administrativos"
    #     data["libros"] = Administrativo
    #     return render(request, self.template_name, data)


class AdministrativoDeleteView(LoginRequiredMixin, DeleteView):
    model = Administrativo
    template_name = 'modals/deleteModal.html'
    success_url = reverse_lazy('administrativos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = reverse_lazy('eliminar_administrativo', kwargs={'pk': self.object.id})
        return context

class AdministrativosAgregarFormView(LoginRequiredMixin, FormView):
    template_name = 'administrativos/agregar_administrativo.html'
    form_class = AgregarAdministrativoForm
    success_url = reverse_lazy('administrativos')
    def form_valid(self, form):
        cedula = form.cleaned_data['cedula']
        pasaporte = form.cleaned_data['pasaporte']
        if not cedula and not pasaporte:
            return bad_json(mensaje="Debe ingresar la cédula o el pasaporte")
        if cedula:
            if Persona.objects.filter(cedula=cedula).exists():
                return bad_json(mensaje= "Ya existe una persona con la cédula ingresada")
        if pasaporte:
            if Persona.objects.filter(pasaporte=pasaporte).exists():
                return bad_json(mensaje= "Ya existe una persona con el pasaporte ingresado")
        
        personaadmin = Persona(
            cedula = cedula,
            pasaporte = pasaporte,
            nombres = form.cleaned_data['nombres'],
            apellido1 = form.cleaned_data['apellido1'],
            apellido2 = form.cleaned_data['apellido2'],

            pais_procedencia = form.cleaned_data['pais_procedencia'],
            nacionalidad = form.cleaned_data['nacionalidad'],

            provincia_procedencia = form.cleaned_data['provincia_procedencia'],
            canton_procedencia = form.cleaned_data['canton_procedencia'],
            parroquia_procedencia = form.cleaned_data['parroquia_procedencia'],

            provincia_procedencia_select = form.cleaned_data['provincia_procedencia_select'],
            canton_procedencia_select = form.cleaned_data['canton_procedencia_select'],
            parroquia_procedencia_select = form.cleaned_data['parroquia_procedencia_select'],

            fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
            estado_civil = form.cleaned_data['estado_civil'],

            provincia_residencia = form.cleaned_data['provincia'],
            canton_residencia = form.cleaned_data['canton'],
            parroquia_residencia = form.cleaned_data['parroquia'],

            sector_residencia = form.cleaned_data['sector_residencia'],
            direccion_residencia = form.cleaned_data['direccion_residencia'],
            num_direccion = form.cleaned_data['num_direccion'],
            telefono_movil = form.cleaned_data['telefono_movil'],
            telefono_fijo = form.cleaned_data['telefono_fijo'],
            email = form.cleaned_data['email'],
            sexo = form.cleaned_data['sexo'],
            orientacion_sexual = form.cleaned_data['orientacion_sexual'],
        )
        personaadmin.save()
        
        username = calcular_username(personaadmin)
        
        generar_usuario(personaadmin, username, ADMINISTRATIVOS_GROUP_ID)

        if EMAIL_INSTITUCIONAL_AUTOMATICO:
            personaadmin.email_institucional = username + '@' + EMAIL_DOMAIN
        else:
            personaadmin.email_institucional = form.cleaned_data['email_institucional']

        personaadmin.save()

        administrativo = Administrativo(
            persona = personaadmin,
            contrato = "",
            fecha_ingreso = datetime.now().date(),
            activo = True
        )
        administrativo.save()
        personaadmin.crear_perfil(administrativo=administrativo)
        
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(AdministrativosAgregarFormView, self).get_context_data(**kwargs)
        context['pais_ecuador_id'] = PAIS_ECUADOR_ID
        context['nacionalidad_ecuador_id'] = NACIONALIDAD_ECUADOR_ID
        return context