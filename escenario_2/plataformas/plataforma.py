from abc import ABC, abstractmethod


class Plataforma(ABC):
    @abstractmethod
    def mostrar(self, titulo: str, mensaje: str) -> None:
        pass
