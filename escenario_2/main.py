from plataformas.plataforma_web import PlataformaWeb
from plataformas.plataforma_movil import PlataformaMovil
from plataformas.plataforma_escritorio import PlataformaEscritorio
from notificaciones.notificacion_mensaje import NotificacionMensaje
from notificaciones.notificacion_alerta import NotificacionAlerta
from notificaciones.notificacion_advertencia import NotificacionAdvertencia
from notificaciones.notificacion_confirmacion import NotificacionConfirmacion


if __name__ == "__main__":
    print("PATRON APLICADO: BRIDGE")

    web = PlataformaWeb()
    movil = PlataformaMovil()
    escritorio = PlataformaEscritorio()

    print("\nCASO: Misma alerta en 3 plataformas distintas:")
    NotificacionAlerta(web).enviar("Servidor caido")
    NotificacionAlerta(movil).enviar("Servidor caido")
    NotificacionAlerta(escritorio).enviar("Servidor caido")

    print("\nCASO: Distintos tipos en escritorio:")
    NotificacionMensaje(escritorio).enviar("Tienes un nuevo correo")
    NotificacionAdvertencia(escritorio).enviar("Batería baja al 10%")
    NotificacionConfirmacion(escritorio).enviar("Archivo guardado correctamente")

    print("\nCASO Cambiando plataforma en caliente:")
    notif = NotificacionAdvertencia(web)
    notif.enviar("Esta advertencia va a la web")
    notif.cambiar_plataforma(movil)
    notif.enviar("Y ahora la MISMA notificación va al móvil")
    notif.cambiar_plataforma(escritorio)
    notif.enviar("Y ahora al escritorio")

    print("\nCASO 4 Combinación 4 tipos x 3 plataformas:")
    tipos = [NotificacionMensaje, NotificacionAlerta,
             NotificacionAdvertencia, NotificacionConfirmacion]
    plataformas = [web, movil, escritorio]

    for tipo in tipos:
        for plataforma in plataformas:
            tipo(plataforma).enviar(f"Demo de {tipo.__name__}")
