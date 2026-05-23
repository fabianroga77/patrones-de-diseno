from __future__ import annotations

from typing import List

from mediadores.chat_mediador import ChatMediator
from usuarios.usuario import Usuario


class SalaChat(ChatMediator):

    def __init__(self, nombre_sala: str) -> None:
        self.nombre_sala = nombre_sala
        self._usuarios: List[Usuario] = []

    def agregar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)
        print(f"+ {usuario.nombre} entro a la sala '{self.nombre_sala}'")

    def eliminar_usuario(self, usuario: Usuario) -> None:
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)
            print(f"- {usuario.nombre} salio de la sala '{self.nombre_sala}'")

    def enviar(self, mensaje: str, remitente: Usuario) -> None:
        for usuario in self._usuarios:
            if usuario is not remitente:
                usuario.recibir(mensaje, remitente)
