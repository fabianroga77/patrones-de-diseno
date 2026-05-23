from __future__ import annotations

from datetime import datetime

from usuarios.usuario import Usuario


class UsuarioBot(Usuario):
    def recibir(self, mensaje: str, remitente: Usuario) -> None:
        hora = datetime.now().strftime("%H:%M:%S")
        print(f"   [{hora}] {self.nombre} (bot) recibe de {remitente.nombre}: '{mensaje}'")

        if "hola" in mensaje.lower():
            self.enviar(f"Hola {remitente.nombre}! Soy un bot")
