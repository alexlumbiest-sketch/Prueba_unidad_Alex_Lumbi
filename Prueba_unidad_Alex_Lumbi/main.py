# main.py

from modelo import ListaPanes
from vista import VistaPanaderia
from controlador import ControladorPanaderia


def main():
    modelo = ListaPanes()
    vista = VistaPanaderia()
    controlador = ControladorPanaderia(modelo, vista)
    controlador.iniciar()


if __name__ == "__main__":
    main()