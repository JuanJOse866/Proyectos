class Factura:
    def __init__(self, nombre_cliente, documento_identidad, nombre_empresa, direccion):
        self.nombre_cliente = nombre_cliente
        self.documento_identidad = documento_identidad
        self.nombre_empresa = nombre_empresa
        self.direccion = direccion

    def generar_factura(self):
        # Aquí puedes implementar la lógica para generar la factura
        print("Factura generada para:", self.nombre_cliente)


class Producto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor


def cotizar_productos():
    total = 0
    productos = []
    while True:
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar la cotización): ")
        if nombre.lower() == 'fin':
            break
        valor = float(input("Ingrese el valor del producto: "))
        productos.append(Producto(nombre, valor))
        total += valor
    print("Total a pagar:", total)


def comprar_productos():
    total = 0
    productos = []
    while True:
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar la compra): ")
        if nombre.lower() == 'fin':
            break
        valor = float(input("Ingrese el valor del producto: "))
        productos.append(Producto(nombre, valor))
        total += valor
    print("Total a pagar:", total)
    cantidad_depositada = float(input("Ingrese la cantidad de dinero a depositar: "))
    cambio = cantidad_depositada - total
    print("Cambio a devolver:", cambio)


def modificar_compra():
    # Aquí puedes implementar la lógica para modificar la compra
    pass


def seleccionar_mercado():
    print("Opciones de mercado:")
    print("1. Homecenter")
    print("2. El euro")
    print("3. Salir del sistema")
    opcion = int(input("Seleccione un mercado (1, 2, 3): "))
    if opcion == 1:
        print("Ha seleccionado Homecenter")
    elif opcion == 2:
        print("Ha seleccionado El euro")
    elif opcion == 3:
        print("Saliendo del sistema...")
    else:
        print("Opción inválida")


def main():
    print("Bienvenido al sistema de gestión financiera")

    nombre_cliente = input("Ingrese su nombre completo: ")
    documento_identidad = input("Ingrese su número de documento de identidad: ")
    nombre_empresa = input("Ingrese el nombre de la empresa: ")
    direccion = input("Ingrese la dirección: ")

    factura = Factura(nombre_cliente, documento_identidad, nombre_empresa, direccion)
    factura.generar_factura()

    while True:
        print("\nMenu:")
        print("1. Cotizar productos")
        print("2. Comprar productos")
        print("3. Modificar compra")
        print("4. Seleccionar mercado")
        print("5. Salir del sistema")
        opcion = int(input("Seleccione una opción (1-5): "))

        if opcion == 1:
            cotizar_productos()
        elif opcion == 2:
            comprar_productos()
        elif opcion == 3:
            modificar_compra()
        elif opcion == 4:
            seleccionar_mercado()
        elif opcion == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
