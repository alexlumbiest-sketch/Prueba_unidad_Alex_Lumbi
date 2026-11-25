# vista.py

class VistaPanaderia:
    def mostrar_menu(self):
        print("\n=== PANADERÍA LA ESPIGA ===")
        print("1. Registrar pan")
        print("2. Mostrar panes")
        print("3. Vender pan")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Elija una opción: ").strip()

    def pedir_datos_pan(self):
        tipo = input("Tipo de pan: ").strip()
        precio = float(input("Precio: "))
        unidades = int(input("Unidades: "))
        return tipo, precio, unidades

    def pedir_codigo(self):
        return int(input("Código del pan: "))

    def pedir_cantidad(self):
        return int(input("Cantidad a vender: "))

    def mostrar_panes(self, panes):
        print(f"\n{'Código':<8}{'Tipo':<14}{'Precio':>8}{'Unidades':>10}")
        print("-" * 40)
        for pan in panes:
            print(pan)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)