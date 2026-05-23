from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Automovil:
    motor: str
    color: str
    transmision: str
    asientos: int
    techo_solar: bool = False
    color_interior: str = "gris"

    def __str__(self):
        return (
            f"Automóvil:"
            f"\n  Motor       : {self.motor}"
            f"\n  Color       : {self.color}"
            f"\n  Transmisión : {self.transmision}"
            f"\n  Asientos    : {self.asientos}"
            f"\n  Techo solar : {'Sí' if self.techo_solar else 'No'}"
            f"\n  Color interior : {self.color_interior if self.color_interior else 'gris por defecto'}"

        )


class AutomovilBuilder(ABC):
    def __init__(self):
        self._motor: str | None = None
        self._color: str | None = None
        self._transmision: str | None = None
        self._asientos: int | None = None
        self._techo_solar: bool = False
        self._color_interior: str = "gris"

    @abstractmethod
    def set_motor(self, motor: str | None = None) -> "AutomovilBuilder": ...

    @abstractmethod
    def set_color(self, color: str) -> "AutomovilBuilder": ...

    @abstractmethod
    def set_transmision(self, transmision: str | None = None) -> "AutomovilBuilder": ...

    @abstractmethod
    def set_asientos(self, asientos: int | None = None) -> "AutomovilBuilder": ...

    @abstractmethod
    def set_techo_solar(self, activo: bool = True) -> "AutomovilBuilder": ...

    @abstractmethod
    def set_color_interior(self, color_interior: str | None = None) -> "AutomovilBuilder": ...

    def build(self) -> Automovil:
        if not all([self._motor, self._color, self._transmision, self._asientos]):
            raise ValueError("Faltan atributos obligatorios para construir el automóvil.")
        return Automovil(
            motor=self._motor,
            color=self._color,
            transmision=self._transmision,
            asientos=self._asientos,
            techo_solar=self._techo_solar,
            color_interior=self._color_interior
        )
