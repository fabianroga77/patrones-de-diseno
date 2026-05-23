import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from mediadores.sala_chat import SalaChat
from usuarios.usuario_chat import UsuarioChat
from usuarios.usuario_bot import UsuarioBot


if __name__ == "__main__":

    sala = SalaChat("Grupo de Amigos")

    print("\n[Registro de usuarios]")
    fabian = UsuarioChat("Fabian", sala)
    andres = UsuarioChat("Andres", sala)
    carlos = UsuarioChat("carlos", sala)
    pedro = UsuarioChat("Pedro", sala)
    bot = UsuarioBot("ChatBot", sala)

    sala.agregar_usuario(fabian)
    sala.agregar_usuario(andres)
    sala.agregar_usuario(carlos)
    sala.agregar_usuario(pedro)
    sala.agregar_usuario(bot)

    print("\nFabian saluda a todos:")
    fabian.enviar("Hola compis, todo bien?")

    print("\n Andres conestesta::")
    andres.enviar("Que tal Fabian, todo bien parce?")

    print("\n Pedro abandona la sala:")
    sala.eliminar_usuario(pedro)

    carlos.enviar("Alguien me escucha?")

    # Agregar un usuario nuevo tampoco rompe nada
    sofia = UsuarioChat("Sofia", sala)
    sala.agregar_usuario(sofia)
    sofia.enviar("Recien entre a la sala, hola!")
