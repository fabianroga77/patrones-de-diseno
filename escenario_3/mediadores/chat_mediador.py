from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from usuarios.usuario import Usuario


class ChatMediator(ABC):

    @abstractmethod
    def enviar(self, mensaje: str, remitente: "Usuario") -> None:
        """Recibe un mensaje del remitente y lo distribuye a los demás."""

    @abstractmethod
    def agregar_usuario(self, usuario: "Usuario") -> None:
        """Registra un nuevo usuario en la sala."""

    @abstractmethod
    def eliminar_usuario(self, usuario: "Usuario") -> None:
        """Elimina un usuario de la sala sin afectar a los demás."""
