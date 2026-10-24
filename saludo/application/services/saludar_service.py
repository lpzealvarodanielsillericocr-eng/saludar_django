
from saludo.domain.persona import Persona


class SaludarService:

    def ejecutar(self, nombre: str) -> str:
        persona = Persona(nombre)
        return persona.saludar()
