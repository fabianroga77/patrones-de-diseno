from escenario_2.notificaciones.notificacion import Notificacion


class NotificacionAdvertencia(Notificacion):
    def enviar(self, mensaje: str) -> None:
        self.plataforma.mostrar("Advertencia", mensaje)
