from applications.core.models import Canton, Pais, Parroquia

from applications.core.utils import bad_json, get_query_params, ok_json

# Create your views here.
def api_view(request):
    action, data = get_query_params (request)
    if not action:
        return bad_json({"error": "No se ha enviado el parametro action"})

    if request.method == 'POST':
        if action == "get_cantones":
            cantones = Canton.objects.filter(provincia_id=data["provincia_id"])
            cantones = cantones.values('id', 'nombre')
            return ok_json({"cantones": list(cantones)})
    
        if action == "get_parroquias":
            parroquias = Parroquia.objects.filter(canton_id=data["canton_id"])
            parroquias = parroquias.values('id', 'nombre')
            return ok_json({"parroquias": list(parroquias)})
        
        if action == "get_nacionalidad":
            #Encontrar la única nacionalidad del modelo Nacionalidad con el id enviado
            pais = Pais.objects.get(id=data["pais_id"])
            nacionalidad = pais.nacionalidad
            if nacionalidad:
                nacionalidad_id = pais.nacionalidad.id
            else:
                nacionalidad_id = 0
            return ok_json({"nacionalidad_id": nacionalidad_id})

        return ok_json({"result": "ok"})
    else:
        print("entrando en el get")
        return ok_json({"result": "ok"})