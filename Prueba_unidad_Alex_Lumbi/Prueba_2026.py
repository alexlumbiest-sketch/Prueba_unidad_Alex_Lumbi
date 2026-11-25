class Pan:
    def __init__(self, codigo, tipo, precio, unidades):
        self.codigo = codigo
        self.tipo = tipo
        self.precio = precio
        self.unidades = unidades

    def vender(self, cantidad):
        """Resta unidades si se puede. Devuelve True o False."""
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.unidades:
            print(f"Error: solo hay {self.unidades} unidades.")
            return False
        self.unidades -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.tipo:<14}{self.precio:>8.2f}{self.unidades:>10}"


# Lista de objetos con los 2 panes iniciales
panes = [
    Pan(1, "Enrollado", 0.15, 120),
    Pan(2, "Integral", 0.25, 60),
]

opcion = 0
while opcion != 4:
    print("\n=== PANADERÍA LA ESPIGA ===")
    print("1. Registrar pan")
    print("2. Mostrar panes")
    print("3. Vender pan")
    print("4. Salir")

    try:
        opcion = int(input("Elija una opción: "))
    except ValueError:
        print("Opción no válida.")
        opcion = 0
        continue

    if opcion == 1:
        try:
            tipo = input("Tipo de pan: ").strip()
            precio = float(input("Precio: "))
            unidades = int(input("Unidades: "))
            codigo = len(panes) + 1
            panes.append(Pan(codigo, tipo, precio, unidades))
            print(f"Registrado con el código {codigo}.")
        except ValueError:
            print("Error: el precio y las unidades deben ser números.")

    elif opcion == 2:
        print(f"\n{'Código':<8}{'Tipo':<14}{'Precio':>8}{'Unidades':>10}")
        print("-" * 40)
        for pan in panes:
            print(pan)

    elif opcion == 3:
        try:
            codigo = int(input("Código del pan: "))
            encontrado = None
            for pan in panes:
                if pan.codigo == codigo:
                    encontrado = pan

            if encontrado is None:
                print("Error: no existe ese código.")
            else:
                cantidad = int(input("Cantidad a vender: "))
                if encontrado.vender(cantidad):
                    print(f"Listo. Quedan {encontrado.unidades} unidades.")
        except ValueError:
            print("Error: debe escribir un número entero.")

    elif opcion == 4:
        print("¡Hasta luego!")

    else:
        print("Opción no válida.")