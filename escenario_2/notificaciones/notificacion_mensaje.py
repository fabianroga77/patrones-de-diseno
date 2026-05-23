from escenario_2.notificaciones.notificacion import Notificacion


class NotificacionMensaje(Notificacion):
    def enviar(self, mensaje: str) -> None:
        self.plataforma.mostrar("Mensaje", mensaje)
