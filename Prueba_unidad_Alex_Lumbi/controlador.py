# controlador.py

class ControladorPanaderia:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def iniciar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                self.registrar_pan()
            elif opcion == "2":
                self.mostrar_panes()
            elif opcion == "3":
                self.vender_pan()
            elif opcion == "4":
                self.vista.mostrar_mensaje("¡Hasta luego!")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida.")

    def registrar_pan(self):
        try:
            # 1. Pedir a la vista
            tipo, precio, unidades = self.vista.pedir_datos_pan()
            # 2. Llamar al modelo
            codigo = self.modelo.registrar(tipo, precio, unidades)
            # 3. Mostrar con la vista
            self.vista.mostrar_mensaje(f"Registrado con el código {codigo}.")
        except ValueError as e:
            if "could not convert" in str(e) or "invalid literal" in str(e):
                self.vista.mostrar_mensaje("Error: el precio y las unidades deben ser números.")
            else:
                self.vista.mostrar_mensaje(str(e))

    def mostrar_panes(self):
        # 1 y 2. Llamar al modelo
        panes = self.modelo.obtener_todos()
        # 3. Mostrar con la vista
        self.vista.mostrar_panes(panes)

    def vender_pan(self):
        try:
            # 1. Pedir código a la vista y verificar existencia en el modelo
            codigo = self.vista.pedir_codigo()
            if self.modelo.buscar(codigo) is None:
                self.vista.mostrar_mensaje("Error: no existe ese código.")
                return

            cantidad = self.vista.pedir_cantidad()
            # 2. Llamar al modelo
            restantes = self.modelo.vender_pan(codigo, cantidad)
            # 3. Mostrar con la vista
            self.vista.mostrar_mensaje(f"Listo. Quedan {restantes} unidades.")
        except ValueError as e:
            if "invalid literal" in str(e):
                self.vista.mostrar_mensaje("Error: debe escribir un número entero.")
            else:
                self.vista.mostrar_mensaje(str(e))