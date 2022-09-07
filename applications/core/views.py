from wsgiref.util import shift_path_info
from django.shortcuts import render

from django.views.generic import View, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from applications.core.forms import ActualizarTablasForm
from applications.core.models import Canton, DiagnosticoPsicologico, Discapacidad, FormaTrabajo, Genero, ListaEnfermedades, Nacionalidad, NacionalidadIndigena, \
    OrientacionSexual, Pais, ParentescoPersona, Parroquia, PersonaEducacion, PersonaEstadoCivil, \
    PersonaProfesion, Provincia, Raza, Sexo, TipoContrato, TipoLicencia, TipoNombramiento, TipoParroquia, TipoRelacionLaboral, \
    TipoSangre, Zona

from applications.core.utils import null_safe_float_to_int, null_safe_string, reset_model

# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    context_object_name = 'home_info'

    def get_queryset(self):
        return 

class AdministracionView(LoginRequiredMixin, View):
    template_name = 'core/administracion.html'
    context_object_name = 'actualizar_tablasbd_info'
    data = {}

    def get(self, request):
        return render(request, self.template_name, self.data)


import pandas
class ActualizarTablasView(LoginRequiredMixin, FormView):
    template_name = 'core/actualizar_tablas_form.html'
    form_class = ActualizarTablasForm
    success_url = '/administracion'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES['archivo']

        if form.is_valid():
            df_sheet_all = pandas.read_excel(file, sheet_name=None)
            for sheet_name, df_sheet in df_sheet_all.items():
                if sheet_name == 'sexo':
                    reset_model(Sexo)
                    for index, row in df_sheet.iterrows():  
                        Sexo.objects.create(nombre=row['nombre'])

                if sheet_name == 'genero':
                    reset_model(Genero)
                    for index, row in df_sheet.iterrows():  
                        Genero.objects.create(nombre=row['nombre'])

                if sheet_name == 'orientacionsexual':
                    reset_model(OrientacionSexual)
                    for index, row in df_sheet.iterrows():  
                        OrientacionSexual.objects.create(nombre=row['nombre'])
                
                if sheet_name == 'nacionalidad':
                    reset_model(Nacionalidad)
                    for index, row in df_sheet.iterrows():  
                        a =Nacionalidad.objects.create(
                            nombre_masculino=row['nombre_masculino'],
                            nombre_femenino=row['nombre_femenino'],
                            nombre=row['nombre'],
                        )
                
                if sheet_name == 'pais':
                    reset_model(Pais)
                    for index, row in df_sheet.iterrows():
                        Pais.objects.create(
                            nombre=row['nombre'],
                            codigo_sniese=row['codigo_sniese'],
                            nacionalidad_id=null_safe_float_to_int(row['nacionalidad_id']),
                        )
                
                if sheet_name == 'zona':
                    reset_model(Zona)
                    for index, row in df_sheet.iterrows():
                        Zona.objects.create(
                            nombre=row['nombre'],
                            codigo_sniese=row['codigo_sniese'],
                        )
                if sheet_name == 'provincia':
                    reset_model(Provincia)
                    for index, row in df_sheet.iterrows():
                        Provincia.objects.create(
                            nombre=row['nombre'],
                            alias=row['alias'],
                            zona_id=null_safe_float_to_int(row['zona_id']),
                            codigo_sniese=row['codigo_sniese'],
                        )

                if sheet_name == 'canton':
                    reset_model(Canton)
                    for index, row in df_sheet.iterrows():
                        a = Canton(
                            nombre=row['nombre'],
                            alias=row['alias'],
                            provincia_id=null_safe_float_to_int(row['provincia_id']),
                            codigo_sniese=null_safe_string(row['codigo_sniese']),
                        )
                        a.id = row['id']
                        a.save()

                if sheet_name == 'tipoparroquia':
                    reset_model(TipoParroquia)
                    for index, row in df_sheet.iterrows():
                        TipoParroquia.objects.create(nombre=row['nombre'])

                if sheet_name == 'parroquia':
                    reset_model(Parroquia)
                    for index, row in df_sheet.iterrows():
                        a = Parroquia(
                            nombre=row['nombre'],
                            alias=row['alias'],
                            canton_id=null_safe_float_to_int(row['canton_id']),
                            tipoparroquia_id=null_safe_float_to_int(row['tipoparroquia_id']),
                        )
                        a.id = row['id']
                        a.save()
                
                if sheet_name == 'tiposangre':
                    reset_model(TipoSangre)
                    for index, row in df_sheet.iterrows():
                        TipoSangre.objects.create(sangre=row['sangre'])
                
                if sheet_name == 'personaestadocivil':
                    reset_model(PersonaEstadoCivil)
                    for index, row in df_sheet.iterrows():
                        PersonaEstadoCivil.objects.create(nombre=row['nombre'])
                
                if sheet_name == 'tipolicencia':
                    reset_model(TipoLicencia)
                    for index, row in df_sheet.iterrows():
                        TipoLicencia.objects.create(nombre=row['nombre'])

                if sheet_name == 'raza':
                    reset_model(Raza)
                    for index, row in df_sheet.iterrows():
                        Raza.objects.create(nombre=row['nombre'], codigo_sniese=row['codigo_sniese'])
                
                if sheet_name == 'nacionalidadindigena':
                    reset_model(NacionalidadIndigena)
                    for index, row in df_sheet.iterrows():
                        NacionalidadIndigena.objects.create(nombre=row['nombre'])
                
                if sheet_name == 'discapacidad':
                    reset_model(Discapacidad)
                    for index, row in df_sheet.iterrows():
                        Discapacidad.objects.create(nombre=row['nombre'])

                if sheet_name == 'parentescopersona':
                    reset_model(ParentescoPersona)
                    for index, row in df_sheet.iterrows():
                        ParentescoPersona.objects.create(nombre=row['nombre'])

                if sheet_name == 'personaeducacion':
                    reset_model(PersonaEducacion)
                    for index, row in df_sheet.iterrows():
                        PersonaEducacion.objects.create(nombre=row['nombre'], codigo_sniese=row['codigo_sniese'])

                if sheet_name == 'personaprofesion':
                    reset_model(PersonaProfesion)
                    for index, row in df_sheet.iterrows():
                        PersonaProfesion.objects.create(nombre=row['nombre'])

                if sheet_name == 'tiporelacionlaboral':
                    reset_model(TipoRelacionLaboral)
                    for index, row in df_sheet.iterrows():
                        TipoRelacionLaboral.objects.create(nombre=row['nombre'])

                if sheet_name == 'tiponombramiento':
                    reset_model(TipoNombramiento)
                    for index, row in df_sheet.iterrows():
                        TipoNombramiento.objects.create(nombre=row['nombre'])

                if sheet_name == 'tipocontrato':
                    reset_model(TipoContrato)
                    for index, row in df_sheet.iterrows():
                        TipoContrato.objects.create(nombre=row['nombre'])

                if sheet_name == 'listaenfermedades':
                    reset_model(ListaEnfermedades)
                    for index, row in df_sheet.iterrows():
                        ListaEnfermedades.objects.create(nombre=row['nombre'])

                if sheet_name == 'diagnosticopsicologico':
                    reset_model(DiagnosticoPsicologico)
                    for index, row in df_sheet.iterrows():
                        DiagnosticoPsicologico.objects.create(nombre=row['nombre'])

                if sheet_name == 'formatrabajo':
                    reset_model(FormaTrabajo)
                    for index, row in df_sheet.iterrows():
                        FormaTrabajo.objects.create(nombre=row['nombre'])

            return self.form_valid(form)

        else:
            return self.form_invalid(form)