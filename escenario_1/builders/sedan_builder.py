from escenario_1.builders.automovil_builder import AutomovilBuilder


class SedanBuilder(AutomovilBuilder):
    def __init__(self):
        super().__init__()
        self._color_interior_nterior = None

    def set_motor(self, motor: str | None = None) -> "SedanBuilder":
        self._motor = motor or "1.6L Turbo"
        return self

    def set_color(self, color: str) -> "SedanBuilder":
        self._color = color
        return self

    def set_transmision(self, transmision: str | None = None) -> "SedanBuilder":
        self._transmision = transmision or "Automática 6 velocidades"
        return self

    def set_asientos(self, asientos: int | None = None) -> "SedanBuilder":
        self._asientos = asientos or 5
        return self

    def set_techo_solar(self, activo: bool = True) -> "SedanBuilder":
        self._techo_solar = activo
        return self

    def set_color_interior(self, color_interior: str = "gris") -> "SedanBuilder":
        self._color_interior = color_interior
        return self