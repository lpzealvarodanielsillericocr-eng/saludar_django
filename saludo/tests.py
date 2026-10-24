
import json

from django.test import SimpleTestCase


class SaludarTests(SimpleTestCase):

    def test_saludo_correcto(self):
        respuesta = self.client.post(
            "/api/saludar/",
            data=json.dumps({"nombre": "Alvaro"}),
            content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(
            respuesta.json(),
            {"saludo": "Hola Alvaro"}
        )

    def test_nombre_vacio(self):
        respuesta = self.client.post(
            "/api/saludar/",
            data=json.dumps({"nombre": ""}),
            content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 400)

    def test_metodo_incorrecto(self):
        respuesta = self.client.get("/api/saludar/")

        self.assertEqual(respuesta.status_code, 405)
