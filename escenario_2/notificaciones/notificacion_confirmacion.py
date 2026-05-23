from escenario_2.notificaciones.notificacion import Notificacion


class NotificacionConfirmacion(Notificacion):
    def enviar(self, mensaje: str) -> None:
        self.plataforma.mostrar("Confirmación", mensaje)
