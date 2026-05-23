from escenario_2.plataformas.plataforma import Plataforma


class PlataformaMovil(Plataforma):
    def mostrar(self, titulo: str, mensaje: str) -> None:
        print(f"Telefono:  hacia --> {titulo} - {mensaje}")
