import json
import datetime

with open("ventas.json", "r") as openfile:
    ventas = json.load(openfile)

with open("compras.json", "r") as openfile:
    compras = json.load(openfile)

with open("stock.json", "r") as openfile:
    stock = json.load(openfile)

# Inicializar listas de ventas y compras

register = {}
compra = {}

while True:

    print("1. Registrar venta")
    print("2. Registrar compra")
    print("5. Salir")
    print("")
    opcion = input("Ingrese una opción: ")
    print("")

    if opcion == "1":
        # Registrar venta
        fecha_venta = datetime.date.today()
        nombre_cliente = input("Ingrese el nombre del paciente: ")
        direccion_cliente = input("Ingrese la dirección del paciente: ")
        nombre_empleado = input("Ingrese el nombre del empleado: ")
        cargo_empleado = input("Ingrese el cargo del empleado: ")

        productos_vendidos = []

        while True:
            nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
            if nombre_producto.lower() == 'salir':
                break

            encontrado = False
            for producto in stock:
                if producto['nombre'].lower() == nombre_producto.lower():
                    precio = producto['precio']
                    stock_actual = producto['stock']

                    cantidad = int(input(f"Ingrese la cantidad que desea comprar (stock disponible: {stock_actual}): "))

                    if cantidad > stock_actual:
                        print("Lo sentimos, no tenemos suficiente stock de este producto.")
                    else:
                        productos_vendidos.append({
                            "nombreMedicamento": nombre_producto,
                            "cantidadVendida": cantidad,
                            "precio": precio,
                        })

                        # Actualizar el stock
                        producto['stock'] -= cantidad

                    encontrado = True
                    break

            if not encontrado:
                print("Lo sentimos, no tenemos ese producto.")

            add_more = input("¿Desea agregar otro producto? (si/no): ")
            if add_more.lower() != 'si':
                break

        register = {
            "fecha": fecha_venta.strftime("%Y-%m-%d"),
            "paciente": {
                "nombre": nombre_cliente,
                "direccion": direccion_cliente
            },
            "empleado": {
                "nombre": nombre_empleado,
                "cargo": cargo_empleado
            },
            "productos": productos_vendidos
        }


        ventas += [register]
        print("Venta registrada con éxito!")

        with open("ventas.json", "w") as  f:
            json.dump(ventas, f, indent=4)

    elif opcion == "2":

        fecha_compra = datetime.date.today()
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        contacto_proveedor = input("Ingrese el contacto del proveedor: ")

        productos_comprados = []

        while True:
            nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
            if nombre_producto.lower() == 'salir':
                break
            
            encontrado = False
            for producto in stock:
                if producto['nombre'].lower() == nombre_producto.lower():
                    precio_compra = float(input("Ingrese el precio de compra del producto: "))
                    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
                    
                    productos_comprados.append({
                        "nombre": nombre_producto,
                        "cantidad": cantidad,
                        "precio_compra": precio_compra,
                        "total": precio_compra * cantidad
                    })
                    
                    # Actualizar el stock
                    producto['stock'] += cantidad
                    encontrado = True
                    break
            
            if not encontrado:
                print("Lo sentimos, no tenemos ese producto en el stock actual.")
            
            add_more = input("¿Desea agregar otro producto? (si/no): ")
            if add_more.lower() != 'si':
                break

        compra = {
            "fecha": fecha_compra.strftime("%Y-%m-%d"),
            "proveedor": {
                "nombre": nombre_proveedor,
                "contacto": contacto_proveedor
            },
            "productos": productos_comprados
        }

        compras += [compra]
        print("Compra registrada con éxito.")

        with open("compras.json", "w") as  f:
            json.dump(compras, f, indent=4)