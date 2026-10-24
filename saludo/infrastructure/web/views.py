
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from saludo.application.ports.saludar_use_case import SaludarUseCase
from saludo.application.services.saludar_service import SaludarService


servicio: SaludarUseCase = SaludarService()


@csrf_exempt
def saludar(request):

    if request.method != "POST":
        respuesta = JsonResponse(
            {"error": "Solo se permite el metodo POST"},
            status=405
        )
        respuesta["Allow"] = "POST"
        return respuesta

    if request.content_type != "application/json":
        return JsonResponse(
            {"error": "Se requiere Content-Type: application/json"},
            status=415
        )

    try:
        datos = json.loads(request.body.decode("utf-8"))

    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "El JSON enviado no es valido"},
            status=400
        )

    if not isinstance(datos, dict):
        return JsonResponse(
            {"error": "Debes enviar un objeto JSON"},
            status=400
        )

    nombre = datos.get("nombre")

    try:
        resultado = servicio.ejecutar(nombre)

    except ValueError as error:
        return JsonResponse(
            {"error": str(error)},
            status=400
        )

    return JsonResponse(
        {"saludo": resultado},
        json_dumps_params={"ensure_ascii": False}
    )
