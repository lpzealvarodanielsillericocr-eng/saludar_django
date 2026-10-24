
from typing import Protocol


class SaludarUseCase(Protocol):

    def ejecutar(self, nombre: str) -> str:
        ...
