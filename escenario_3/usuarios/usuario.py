from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mediadores.chat_mediador import ChatMediator


class Usuario(ABC):

    def __init__(self, nombre: str, mediador: "ChatMediator") -> None:
        self.nombre = nombre
        self._mediador = mediador

    def enviar(self, mensaje: str) -> None:
        print(f"[{self.nombre}] envia: '{mensaje}'")
        self._mediador.enviar(mensaje, self)

    @abstractmethod
    def recibir(self, mensaje: str, remitente: "Usuario") -> None:
        """Cada tipo de usuario decide cómo reacciona al recibir un mensaje."""
