from builders.sedan_builder import SedanBuilder


if __name__ == "__main__":
    sedan = (
        SedanBuilder()
        .set_motor("2.0 L")
        .set_color("tornasol rojo")
        .set_transmision()
        .set_asientos()
        .set_color_interior("marron")
        .build()
    )
    print(sedan)
