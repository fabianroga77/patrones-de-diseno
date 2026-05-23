from escenario_2.plataformas.plataforma import Plataforma


class PlataformaWeb(Plataforma):
    def mostrar(self, titulo: str, mensaje: str) -> None:
        print(f"WEB  --> {titulo} - {mensaje}")
