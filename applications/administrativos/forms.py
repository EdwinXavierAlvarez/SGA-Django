from django import forms

from applications.core.forms import BaseForm
from applications.core.models import Canton, Nacionalidad, OrientacionSexual, Pais, Parroquia, PersonaEstadoCivil, Provincia, Sexo, TipoSangre


class AgregarAdministrativoForm(BaseForm):
    cedula = forms.CharField(label="Cédula", max_length=10,
                            widget=forms.TextInput(attrs={'labelwidth': 6, 'validate': "cedula"}))
    pasaporte = forms.CharField(label="Pasaporte", max_length=10, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    nombres = forms.CharField(label="Nombres", max_length=50, required=True)
    apellido1 = forms.CharField(label="1er Apellido", max_length=50, required=True,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    apellido2 = forms.CharField(label="2do Apellido", max_length=50, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    
    pais_procedencia = forms.ModelChoiceField(label="País de Nacimiento", queryset=Pais.objects.all(), required=True,
                            widget=forms.Select(attrs={'labelwidth': 6, 'separator': "NACIMIENTO"}))
    nacionalidad = forms.ModelChoiceField(label="Nacionalidad", queryset=Nacionalidad.objects.all(),
                            widget=forms.Select(attrs={'labelwidth': 6}))
    
    provincia_procedencia = forms.CharField(label="Provincia de Nacimiento", max_length=50, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    canton_procedencia = forms.CharField(label="Cantón de Nacimiento", max_length=50, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    parroquia_procedencia = forms.CharField(label="Parroquia de Nacimiento", max_length=50, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    
    provincia_procedencia_select = forms.ModelChoiceField(label="Provincia de Nacimiento", required=False, queryset=Provincia.objects,
                            widget=forms.Select(attrs={'labelwidth': 6}))
    canton_procedencia_select = forms.ModelChoiceField(label="Cantón de Nacimiento", required=False, queryset=Canton.objects,
                            widget=forms.Select(attrs={'labelwidth': 6}))
    parroquia_procedencia_select = forms.ModelChoiceField(label="Parroquia de Nacimiento", required=False, queryset=Parroquia.objects,
                            widget=forms.Select(attrs={'labelwidth': 6}))
    
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", 
                            widget=forms.DateInput(attrs={'type': 'date', 'labelwidth': 6}))
    estado_civil = forms.ModelChoiceField(label="Estado Civil", queryset=PersonaEstadoCivil.objects.all(),
                            widget=forms.Select(attrs={'labelwidth': 6}))
    
    provincia = forms.ModelChoiceField(label="Provincia de Residencia", queryset=Provincia.objects.all(), required=True,
                            widget=forms.Select(attrs={'labelwidth': 6, 'separator': "RESIDENCIA"}))
    canton = forms.ModelChoiceField(label="Cantón de Residencia", queryset=Canton.objects.all(), required=True,
                            widget=forms.Select(attrs={'labelwidth': 6}))
    parroquia = forms.ModelChoiceField(label="Parroquia de Residencia", queryset=Parroquia.objects.all(), required=True,
                            widget=forms.Select(attrs={'labelwidth': 6}))
    sector_residencia = forms.CharField(label="Sector", max_length=100, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    direccion_residencia = forms.CharField(label="Calle Principal", max_length=100, required=True,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    num_direccion = forms.CharField(label="Número Domicilio", max_length=15, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    direccion2 = forms.CharField(label="Calle Secundaria", max_length=20, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6}))
    telefono_movil = forms.CharField(label="Teléfono Móvil", required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6,
                            'separator': "OTROS", 'validate': "telefono_movil"}))
    telefono_fijo = forms.CharField(label="Teléfono Fijo", max_length=15, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6, 'validate': "telefono_fijo"}))
    email = forms.CharField(label="Correo Electrónico", max_length=50, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6, 'type': "email"}))
    email_institucional = forms.CharField(label="Correo Institucional", max_length=50, required=False,
                            widget=forms.TextInput(attrs={'labelwidth': 6, 'type': "email"}))
    sexo = forms.ModelChoiceField(label="Sexo", queryset=Sexo.objects.all(), required=True,
                            widget=forms.Select(attrs={'labelwidth': 6}))
    orientacion_sexual = forms.ModelChoiceField(label="Orientación Sexual", queryset=OrientacionSexual.objects.all(), required=True,
                            widget=forms.Select(attrs={'labelwidth': 6}))
    sangre = forms.ModelChoiceField(label="Tipo de Sangre", queryset=TipoSangre.objects.all(), required=True,
                            widget=forms.Select(attrs={'labelwidth': 6}))