
from dataclasses import dataclass


@dataclass(frozen=True)
class Persona:
    nombre: str

    def __post_init__(self):
        if not isinstance(self.nombre, str):
            raise ValueError("El nombre debe ser un texto")

        nombre_limpio = self.nombre.strip()

        if not nombre_limpio:
            raise ValueError("El nombre no puede estar vacio")

        object.__setattr__(self, "nombre", nombre_limpio)

    def saludar(self) -> str:
        return f"Hola {self.nombre}"
