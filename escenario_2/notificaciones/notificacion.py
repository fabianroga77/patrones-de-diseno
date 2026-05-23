from abc import ABC, abstractmethod

from escenario_2.plataformas.plataforma import Plataforma


class Notificacion(ABC):

    def __init__(self, plataforma: Plataforma):
        self.plataforma = plataforma

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass

    def cambiar_plataforma(self, nueva: Plataforma) -> None:
        self.plataforma = nueva
