from xmlrpc.client import Boolean
from django.db import models
from applications.administrativos.models import Administrativo

from applications.usuario.models import ModeloBase, User

# Create your models here.
class Sexo(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Sexo'
        verbose_name_plural = u'Sexos'

class Genero(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)
    otro = models.BooleanField(default=False, verbose_name=u'Otro')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Género'
        verbose_name_plural = u'Géneros'

class OrientacionSexual(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Orientación sexual'
        verbose_name_plural = u'Orientaciones sexuales'

class Nacionalidad(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u"Nacionalidad", unique=True)
    nombre_masculino = models.CharField(default='', max_length=100, verbose_name=u"Nacionalidad Masculina")
    nombre_femenino = models.CharField(default='', max_length=100, verbose_name=u"Nacionalidad Femenina")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Nacionalidad'
        verbose_name_plural = u'Nacionalidades'

class Pais(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)
    codigo_sniese = models.CharField(default='', max_length=15, verbose_name=u'Código SNIESE')
    nacionalidad = models.ForeignKey(Nacionalidad, blank=True, null=True, verbose_name=u"Nacionalidad", on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'País'
        verbose_name_plural = u'Países'

class Zona(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)
    codigo_sniese = models.CharField(default='', max_length=15, verbose_name=u'Código SNIESE')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Zona'
        verbose_name_plural = u'Zonas'


class Provincia(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)
    alias = models.CharField(default='', max_length=100, verbose_name=u'Alias')
    zona = models.ForeignKey(Zona, blank=True, null=True, verbose_name=u"Zona", on_delete=models.SET_NULL)
    codigo_sniese = models.CharField(default='', max_length=15, verbose_name=u'Código SNIESE')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Provincia'
        verbose_name_plural = u'Provincias'

class Canton(ModeloBase):
    provincia = models.ForeignKey(Provincia, blank=True, null=True, verbose_name=u"Provincia", on_delete=models.SET_NULL)
    alias = models.CharField(default='', max_length=100, verbose_name=u'Alias')
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre')
    codigo_sniese = models.CharField(default='', null=True, max_length=15, verbose_name=u'Código SNIESE')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Cantón'
        verbose_name_plural = u'Cantones'


class TipoParroquia(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Tipo de parroquia'
        verbose_name_plural = u'Tipos de parroquias'


class Parroquia(ModeloBase):
    canton = models.ForeignKey(Canton, verbose_name=u"Canton", blank=True, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(default='', max_length=100, verbose_name=u"Nombre")
    alias = models.CharField(default='', max_length=100, verbose_name=u"Alias")
    tipoparroquia = models.ForeignKey(TipoParroquia, blank=True, null=True, verbose_name=u"Tipo parroquia", on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Parroquia'
        verbose_name_plural = u'Parroquias'
        ordering = ['nombre']


class TipoSangre(ModeloBase):
    sangre = models.CharField(default='', max_length=100, verbose_name=u'Sangre', unique=True)

    def __str__(self):
        return self.sangre
    class Meta:
        verbose_name = u'Tipo de sangre'
        verbose_name_plural = u'Tipos de sangre'


class PersonaEstadoCivil(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Estado civil'
        verbose_name_plural = u'Estados civiles'


class TipoLicencia(ModeloBase):
    nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre', unique=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Tipo de licencia'
        verbose_name_plural = u'Tipos de licencias'


class Persona(ModeloBase):
    nombres = models.CharField(default='', max_length=100, verbose_name=u'Nombre')
    nombres_completos = models.CharField(default='', max_length=1000, verbose_name=u'Nombre')
    apellido1 = models.CharField(default='', max_length=50, verbose_name=u"1er Apellido")
    apellido2 = models.CharField(default='', max_length=50, verbose_name=u"2do Apellido")
    cedula = models.CharField(default='', max_length=13, verbose_name=u"Cedula")
    fecha_caducidad_cedula = models.DateField(blank=True, null=True)
    pasaporte = models.CharField(default='', max_length=30, verbose_name=u"Pasaporte / Identificación")
    fecha_nacimiento = models.DateField(verbose_name=u"Fecha de nacimiento", blank=True, null=True)
    sexo = models.ForeignKey(Sexo, verbose_name=u'Sexo', blank=True, null=True, on_delete=models.SET_NULL)
    genero = models.ForeignKey(Genero, blank=True, null=True, verbose_name=u'Orientación sexual', on_delete=models.SET_NULL)
    orientacion_sexual = models.ForeignKey(OrientacionSexual, blank=True, null=True, verbose_name=u'Orientación sexual', on_delete=models.DO_NOTHING)
    
    pais_procedencia = models.ForeignKey(Pais, blank=True, null=True, verbose_name=u'País procedencia', 
                                        on_delete=models.SET_NULL, related_name='pais_procedencia')
    pais_residencia = models.ForeignKey(Pais, blank=True, null=True, verbose_name=u'País de residencia', 
                                        on_delete=models.SET_NULL, related_name='pais_residencia')
    nacionalidad = models.ForeignKey(Nacionalidad, blank=True, null=True, verbose_name=u"Nacionalidad", on_delete=models.SET_NULL)


    provincia_procedencia_select = models.ForeignKey(Provincia, blank=True, null=True, verbose_name=u"Provincia de procedencia", 
                                        on_delete=models.SET_NULL, related_name='provincia_procedencia')
    canton_procedencia_select = models.ForeignKey(Canton, blank=True, null=True, verbose_name=u"Cantón de procedencia", 
                                        on_delete=models.SET_NULL, related_name='canton_procedencia')
    parroquia_procedencia_select = models.ForeignKey(Parroquia, blank=True, null=True, verbose_name=u"Parroquia de procedencia", 
                                        on_delete=models.SET_NULL, related_name='parroquia_procedencia')


    provincia_procedencia = models.CharField(max_length=100, verbose_name=u"Provincia de procedencia", blank=True, null=True)
    canton_procedencia = models.CharField(max_length=100, verbose_name=u"Cantón de procedencia", blank=True, null=True)
    parroquia_procedencia = models.CharField(max_length=100, verbose_name=u"Parroquia de procedencia", blank=True, null=True)
    

    provincia_residencia = models.ForeignKey(Provincia, blank=True, null=True, verbose_name=u"Provincia de residencia", 
                                        on_delete=models.SET_NULL, related_name='provincia_residencia')
    canton_residencia = models.ForeignKey(Canton, blank=True, null=True, verbose_name=u"Cantón de residencia", 
                                        on_delete=models.SET_NULL, related_name='canton_residencia')
    parroquia_residencia = models.ForeignKey(Parroquia, blank=True, null=True, verbose_name=u"Parroquia de residencia", 
                                        on_delete=models.SET_NULL, related_name='parroquia_residencia')
    
    sector_procedencia = models.CharField(default='', max_length=100, verbose_name=u"Sector de procedencia")
    sector_residencia = models.CharField(default='', max_length=100, verbose_name=u"Sector de residencia")

    direccion_procedencia = models.CharField(default='', max_length=100, verbose_name=u"Calle principal de procedencia")
    direccion_residencia = models.CharField(default='', max_length=100, verbose_name=u"Calle principal residencia")
    
    direccion2procedencia = models.CharField(default='', max_length=100, verbose_name=u"Calle secundaria procedecia") 
    direccion2_residencia = models.CharField(default='', max_length=100, verbose_name=u"Calle secundaria residencia")

    codigo_postal = models.CharField(default='', max_length=30, verbose_name=u"Código postal")
    referencia = models.CharField(default='', max_length=100, verbose_name=u"Referencia")
    num_direccion = models.CharField(default='', max_length=15, verbose_name=u"Numero de domicilio")

    telefono_movil = models.CharField(default='', max_length=50, verbose_name=u"Teléfono movil")
    telefono_fijo = models.CharField(default='', max_length=50, verbose_name=u"Teléfono fijo")
    
    email = models.CharField(default='', max_length=200, verbose_name=u"Correo electrónico personal")
    email_institucional = models.CharField(default='', max_length=200, verbose_name=u"Correo electrónico institucional")
    
    sangre = models.ForeignKey(TipoSangre, blank=True, null=True, verbose_name=u"Tipo de Sangre", on_delete=models.SET_NULL)
    estado_civil = models.ForeignKey(PersonaEstadoCivil, blank=True, null=True, verbose_name=u"Estado civil", on_delete=models.SET_NULL)
    tipo_licencia = models.ForeignKey(TipoLicencia, blank=True, null=True, verbose_name=u"Tipo licencia", on_delete=models.SET_NULL)
    libreta_militar = models.CharField(default='', max_length=30, verbose_name=u"Libreta Militar")    
    
    email_verified = models.BooleanField(default=False)
    contrasena_temporal = models.CharField(default='', max_length=100, verbose_name=u"Contrasena Temporal Correo Institucional")

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellido1 + ' ' + self.apellido2

    def crear_perfil(self, temporal=None, administrativo=None):
        if administrativo:
            if not PerfilUsuario.objects.filter(persona=self, administrativo=administrativo).exists():
                perfil = PerfilUsuario(persona=self, administrativo=administrativo)
                perfil.save()

    def grupos(self):
        return self.usuario.groups.all().distinct()   


class PerfilUsuario(ModeloBase):
    persona = models.ForeignKey(Persona, verbose_name=u"Persona", on_delete=models.CASCADE, related_name='perfil_usuario')
    administrativo = models.OneToOneField(Administrativo, blank=True, null=True, verbose_name=u"Otro", on_delete=models.SET_NULL, related_name='perfil_usuario_otro')


    def __str__(self):
        return self.persona
    
    class Meta:
        verbose_name = u"Perfil de usuario"
        verbose_name_plural = u"Perfiles de usuario"
        ordering = ['persona']

class Raza(ModeloBase):
    nombre = models.CharField(default="", max_length=50, verbose_name=u"Nombre")
    codigo_sniese = models.CharField(default="", max_length=15, verbose_name=u"Código SNIESE")

    class Meta:
        verbose_name_plural = u"Etnias"
        ordering = ['nombre']
        unique_together = ('nombre', )

class NacionalidadIndigena(ModeloBase):
    nombre = models.CharField(default="", max_length=50, verbose_name=u"Nombre")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = u"Nacionalidades Indígenas"
        ordering = ['nombre']
        unique_together = ('nombre', )

class Discapacidad(ModeloBase):
    nombre = models.CharField(default="", max_length=50, verbose_name=u"Nombre")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Discapacidades"
        ordering = ['nombre']
        unique_together = ('nombre', )


class ParentescoPersona(ModeloBase):
    nombre = models.CharField(default="", max_length=50, verbose_name=u"Nombre")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de Parentescos"
        ordering = ['nombre']
        unique_together = ('nombre', )


class PersonaEducacion(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Nombre")
    codigo_sniese = models.CharField(default="", max_length=15, verbose_name=u"Código SNIESE")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Niveles de Educación"
        ordering = ['nombre']
        unique_together = ('nombre', )  


class PersonaProfesion(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Nombre")
    activo = models.BooleanField(default=True, verbose_name=u"Activo")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Profesiones"
        ordering = ['nombre']
        unique_together = ('nombre', )


class TipoRelacionLaboral(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Nombre")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos de Relación Laboral"
        ordering = ['nombre']
        unique_together = ('nombre', )


class TipoNombramiento(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Tipo de Nombramiento")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos de Nombramiento"
        ordering = ['nombre']
        unique_together = ('nombre', )


class TipoContrato(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Tipo de Contrato")
    fecha = models.DateField(verbose_name=u"Fecha", blank=True, null=True)
    archivo = models.FileField(upload_to='contratos/', verbose_name=u"Archivo", blank=True, null=True)
    activo = models.BooleanField(default=True, verbose_name=u"Activo")
    indefinido = models.BooleanField(default=False, verbose_name=u"Indefinido")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos de Contratos"
        ordering = ['nombre']
        unique_together = ('nombre', )


class ListaEnfermedades(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Nombre")
    cronica = models.BooleanField(default=False, verbose_name=u"Cronica")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Enfermedades"
        ordering = ['nombre']
        unique_together = ('nombre', )
    
class DiagnosticoPsicologico(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Nombre")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Diagnosticos Psicologicos"
        ordering = ['nombre']
        unique_together = ('nombre', )


class FormaTrabajo(ModeloBase):
    nombre = models.CharField(default="", max_length=100, verbose_name=u"Nombre")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Formas de Trabajo"
        ordering = ['nombre']
        unique_together = ('nombre', )

class PersonaDatosFamiliares(ModeloBase):
    parentesco = models.ForeignKey(ParentescoPersona, verbose_name=u"Parentesco", on_delete=models.CASCADE, related_name='persona_datos_familiares')
    nombre = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Nombre")
    fallecido = models.BooleanField(default=False, verbose_name=u"Fallecido")
    cedula = models.CharField(default="", blank=True, null=True, max_length=15, verbose_name=u"Cédula")
    fecha_nacimiento = models.DateField(default=None, blank=True, null=True, verbose_name=u"Fecha de nacimiento")
    edad = models.IntegerField(default=None, blank=True, null=True, verbose_name=u"Edad")
    estado_civil = models.ForeignKey(PersonaEstadoCivil, blank=True, null=True, verbose_name=u"Estado civil", on_delete=models.SET_NULL)
    telefono_fijo = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Teléfono fijo")
    telefono_movil = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Teléfono movil")
    educacion = models.ForeignKey(PersonaEducacion, blank=True, null=True, verbose_name=u"Nivel de educación", on_delete=models.SET_NULL)
    profesion = models.ForeignKey(PersonaProfesion, blank=True, null=True, verbose_name=u"Profesión", on_delete=models.SET_NULL)
    lugar_trabajo = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Lugar de Trabajo")
    lista_enfermedades = models.ManyToManyField(ListaEnfermedades, blank=True, verbose_name=u"Enfermedades")
    enfermedad = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Otras Enfermedades")
    tiene_diagnostico_psicologico = models.BooleanField(default=False, verbose_name=u"Tiene Diagnóstico Psicológico")
    diagnostico_psicologico = models.ManyToManyField(DiagnosticoPsicologico, blank=True, verbose_name=u"Diagnóstico Psicológico")
    recibio_medicacion_diagnostico = models.BooleanField(default=False, verbose_name=u"Recibió Medicación")
    forma_trabajo = models.ForeignKey(FormaTrabajo, blank=True, null=True, verbose_name=u"Forma de Trabajo", on_delete=models.SET_NULL)
    ingreso_mensual = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=u"Ingreso Mensual")
    recibe_bono = models.BooleanField(default=False, verbose_name=u"Recibe Bono")
    ingreso_bono = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=u"Ingreso Bono")
    motivo_bono = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Motivo del Bono")
    fecha_bobo = models.DateField(default=None, blank=True, null=True, verbose_name=u"Fecha del Bono")
    convive = models.BooleanField(default=False, verbose_name=u"Convive")
    convivio = models.BooleanField(default=False, verbose_name=u"Convivio")
    trabaja = models.BooleanField(default=False, verbose_name=u"Trabaja")
    sustento_hogar = models.BooleanField(default=False, verbose_name=u"Sustento del Hogar")
    sistema_familiar = models.BooleanField(default=False, verbose_name=u"Sistema Familiar")
    tiene_discapacidad = models.BooleanField(default=False, verbose_name=u"Tiene Discapacidad")
    tipo_discapacidad = models.ForeignKey(Discapacidad, blank=True, null=True, verbose_name=u"Tipo de Discapacidad", on_delete=models.SET_NULL)
    porcentaje_discapacidad = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name="Porcentaje discapacidad")
    carnet_discapacidad = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Carnet de Discapacidad")
    migrante = models.BooleanField(default=False, verbose_name=u"Migrante")
    fecha_migracion = models.DateField(default=None, blank=True, null=True, verbose_name=u"Fecha de Migración")
    motivo_migracion = models.CharField(default="", blank=True, null=True, max_length=50, verbose_name=u"Motivo de Migración")
    migrante_retornado = models.BooleanField(default=False, verbose_name=u"Migrante Retornado")
    fecha_retorno = models.DateField(default=None, blank=True, null=True, verbose_name=u"Fecha de Retorno")

    def __str__(self):
        return self.nombre


class PersonaExtension(ModeloBase):
    persona = models.ForeignKey(Persona, verbose_name=u"Persona", on_delete=models.PROTECT, related_name='persona_extension')
    sera_padre = models.BooleanField(default=False, verbose_name=u"Será padre")
    historia_clinica_iess = models.CharField(default="", max_length=50, blank=True, null=True, verbose_name=u"Historia clínica IESS")
    contacto_emergencia = models.CharField(default="", max_length=50, blank=True, null=True, verbose_name=u"Contacto de emergencia")
    relacion_contacto_emergencia = models.ForeignKey(ParentescoPersona, blank=True, null=True, verbose_name=u"Relación con el contacto de emergencia", on_delete=models.SET_NULL)
    telefono_emergencia = models.CharField(default="", max_length=50, blank=True, null=True, verbose_name=u"Teléfono de emergencia")
    email_contacto_emergencia = models.CharField(default="", max_length=50, blank=True, null=True, verbose_name=u"Correo electrónico de emergencia")
    vida_estudiantil = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Vida estudiantil")
    situacion_familiar = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Situación familiar")
    situacion_emocional = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Situación emocional")
    vida_social = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Vida social")
    toma_decision = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Toma decisiones")
    datos_damiliares = models.ManyToManyField(PersonaDatosFamiliares)

    def __str__(self):
        return self.persona.nombre
    
    class Meta:
        verbose_name_plural = "Personas Extensiones"
        unique_together = ('persona', )





# Persona Ficha médica
TIPOFICHAMEDICA = (
    (1, 'DIAGNÓSTICO INICIAL'),
    (2, 'PREOCUPACIONAL'),
    (3, 'RETIRO'),
    (4, 'OCUPACIONAL/ PERIÓDICOS'),
    (5, 'REINGRESO'),
    (6, 'CAMBIO DE PUESTO'),
)

class PersonaFichaMedica(ModeloBase):
    ficha_llena = models.BooleanField(default=False, verbose_name=u"Ficha Llena")
    fecha_actualizacion = models.DateField(default=None, blank=True, null=True, verbose_name=u"Fecha de Actualización")
# ***********************************************************************

class PerfilInscripcion(ModeloBase):
    persona = models.ForeignKey(Persona, verbose_name=u"Persona", on_delete=models.CASCADE, related_name='perfil_inscripcion')
    raza = models.ForeignKey(Raza, blank=True, null=True, verbose_name="Raza", on_delete=models.SET_NULL)
    nacionalidad_indigena = models.ForeignKey(NacionalidadIndigena, blank=True, null=True, verbose_name="Nacionalidad indígena", on_delete=models.SET_NULL)
    tiene_discapacidad = models.BooleanField(default=False, verbose_name="Tiene discapacidad")
    verificado_bienestar = models.BooleanField(default=False, verbose_name="Verificado bienestar")
    aprobado_bienestar = models.BooleanField(default=False, verbose_name="Aprobado bienestar")
    verificado_admin = models.BooleanField(default=False, verbose_name="Verificado administrativo")
    discapacidad_ws = models.BooleanField(default=False, verbose_name="Discapacidad WS")
    tipo_discapacidad = models.ForeignKey(Discapacidad, blank=True, null=True, verbose_name="Tipo discapacidad", on_delete=models.SET_NULL)
    porcentaje_discapacidad = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name="Porcentaje discapacidad")
    carnet_discapacidad = models.CharField(default="", max_length=50, verbose_name="Carnet discapacidad")
    archivo = models.FileField(upload_to='archivos/discapacidad/', verbose_name="Archivo")