from escenario_2.plataformas.plataforma import Plataforma


class PlataformaEscritorio(Plataforma):
    def mostrar(self, titulo: str, mensaje: str) -> None:
        print(f"ESCRITORIO ventana: {titulo} - {mensaje}")
