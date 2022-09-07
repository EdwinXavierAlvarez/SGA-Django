from io import BytesIO
import json

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseBadRequest
from xhtml2pdf import pisa
from django.template.loader import get_template

from django.core.mail import send_mail
from django.conf import settings
from applications.core.models import Persona
from applications.usuario.models import User

from sga.settings import CLAVE_USUARIO_CEDULA, DEFAULT_PASSWORD

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# Envio de un solo email
def send_email(subject, body, to):
    send_mail(subject, body, settings.EMAIL_HOST_USER, [to])
    return


from django.core.management.color import no_style
from django.db import connection

def reset_model(model):
    model.objects.all().delete()
    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [model])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)
    return

def null_safe_float_to_int(value):
    import pandas as pd
    if pd.isnull(value):
        return None
    else:
        return int(value)

def null_safe_string(value):
    import pandas as pd
    if pd.isnull(value):
        return None
    else:
        return str(value)

def ok_json(data):
    import pandas as pd
    if "result" not in data:
        data.update({"result": "ok"})
    return HttpResponse(json.dumps(data), content_type='application/json')

def bad_json(mensaje=None, error=None, extradata=None):
    data = {'result': 'bad'}
    if mensaje:
        data['mensaje'] = mensaje
    if error:
        if error >= 0:
            if error == 0:
                data['mensaje'] = "Solicitud incorrecta"
            elif error == 1:
                data['mensaje'] = "Error al guardar los datos"
            elif error == 2:
                data['mensaje'] = "Error al eliminar los datos"
    if extradata:
        data.update(extradata)
    return HttpResponseBadRequest(json.dumps(data), content_type='application/json')

def get_query_params(request):
    action = request.GET.get('action', '')
    data = json.loads(request.body)
    if action == "":
        if action in data:
            action = data['action']
        else:
            action == None            
    return action, data


def calcular_username(persona, variant=1, estudiante=None):
    import unidecode
    nombres = persona.nombres
    apellido1 = persona.apellido1
    # Reemplaza los espacios en blanco por un solo espacio
    nombres_filter = " ".join(nombres.split()).lower()
    apellido1_filter = " ".join(apellido1.split()).lower()

    array_nombres = nombres_filter.split(" ")

    if len(array_nombres) > 1:
        username_v1 = array_nombres[0][0] + array_nombres[1] + apellido1_filter
    else:
        username_v1 = array_nombres[0][0] + apellido1_filter
    if not estudiante:
        username_v1 = array_nombres[0] + "." + apellido1_filter

    # Replace all alphanumeric characters
    username = unidecode.unidecode(username_v1)

    # Remove non-alphanumeric characters
    username = ''.join(filter(lambda x: x.isalnum(), username))

    if variant > 1:
        username += str(variant)
    if not User.objects.filter(username=username).exists():
        return username
    else:
        return calcular_username(persona, variant+1, estudiante)

def generar_usuario(persona, username, grupo_id=None):
    password = DEFAULT_PASSWORD
    if CLAVE_USUARIO_CEDULA:
        if persona.cedula:
            password = persona.cedula
        else:
            password = persona.pasaporte
    
    user = User.objects.create_user(username=username, password=password)
    persona.usuario = user
    persona.save()
    grupo = Group.objects.get(pk=grupo_id)
    user.groups.add(grupo) if grupo else None
    return persona