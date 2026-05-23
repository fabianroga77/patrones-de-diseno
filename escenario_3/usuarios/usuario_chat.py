from __future__ import annotations

from datetime import datetime

from usuarios.usuario import Usuario


class UsuarioChat(Usuario):

    def recibir(self, mensaje: str, remitente: Usuario) -> None:
        hora = datetime.now().strftime("%H:%M:%S")
        print(f"   [{hora}] {self.nombre} recibe de {remitente.nombre}: '{mensaje}'")
