class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = round(precio, 2)  # Asegurar que el precio siempre tenga dos decimales

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = round(nuevo_precio, 2)  # Aplicar redondeo también al actualizar

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            return "Error: El ID ya existe."
        self.productos[producto.get_id()] = producto
        return "Producto agregado correctamente."

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            return "Producto eliminado correctamente."
        return "Error: El producto no existe."

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            return "Error: Producto no encontrado."

        producto = self.productos[id_producto]
        if cantidad is not None:
            producto.set_cantidad(cantidad)
        if precio is not None:
            producto.set_precio(precio)

        return "Producto actualizado correctamente."

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        if not self.productos:
            return "El inventario está vacío."
        return "\n".join(str(p) for p in self.productos.values())


if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                print(inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio)))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            print(inventario.eliminar_producto(id_producto))

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")

            cantidad = int(cantidad) if cantidad.strip().isdigit() else None
            precio = float(precio) if precio.replace(".", "", 1).isdigit() else None

            print(inventario.actualizar_producto(id_producto, cantidad, precio))

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_por_nombre(nombre)
            if productos:
                for p in productos:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            print(inventario.mostrar_productos())

        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
