from escenario_2.notificaciones.notificacion import Notificacion


class NotificacionAlerta(Notificacion):
    def enviar(self, mensaje: str) -> None:
        self.plataforma.mostrar("ALERTA", mensaje.upper())
