# modelo.py

class Pan:
    def __init__(self, codigo, tipo, precio, unidades):
        self.codigo = codigo
        self.tipo = tipo
        self.precio = precio
        self.unidades = unidades
        self.validar()

    def validar(self):
        if not self.tipo or self.tipo.strip() == "":
            raise ValueError("Error: el tipo de pan no puede estar vacío.")
        if self.precio <= 0:
            raise ValueError("Error: el precio debe ser mayor que cero.")
        if self.unidades < 0:
            raise ValueError("Error: las unidades no pueden ser negativas.")

    def vender(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Error: la cantidad debe ser mayor que cero.")
        if cantidad > self.unidades:
            raise ValueError(f"Error: solo hay {self.unidades} unidades.")
        self.unidades -= cantidad
        return self.unidades

    def __str__(self):
        return f"{self.codigo:<8}{self.tipo:<14}{self.precio:>8.2f}{self.unidades:>10}"


class ListaPanes:
    def __init__(self):
        self.panes = [
            Pan(1, "Enrollado", 0.15, 120),
            Pan(2, "Integral", 0.25, 60),
        ]

    def registrar(self, tipo, precio, unidades):
        codigo = len(self.panes) + 1
        nuevo_pan = Pan(codigo, tipo, precio, unidades)
        self.panes.append(nuevo_pan)
        return codigo

    def buscar(self, codigo):
        for pan in self.panes:
            if pan.codigo == codigo:
                return pan
        return None

    def vender_pan(self, codigo, cantidad):
        pan = self.buscar(codigo)
        if pan is None:
            raise ValueError("Error: no existe ese código.")
        return pan.vender(cantidad)

    def obtener_todos(self):
        return self.panes