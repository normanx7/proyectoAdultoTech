# Talento Lab, Entrega de Proyecto Final - Norman Primera DNI 19102676 #25047

import sqlite3 # Importando modulo SQLITE3

from colorama import Fore, Back, Style, init
init() # Importando e inicializando funcionalidades de Colorama

# Conexión a la base de datos
conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL
    )
''')
conexion.commit()

def registrar_producto(nombre_producto, descripcion_producto, cantidad_pruducto, precio_producto, categoria_producto):
    """Agrega un nuevo producto al inventario"""
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)", (nombre_producto, descripcion_producto, cantidad_pruducto, precio_producto, categoria_producto))
    conexion.commit()
    print(Fore.GREEN + "Producto ingresado con éxito" + Style.RESET_ALL)

def mostrar_productos():
    """Visualizar productos existentes en el inventario"""
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print(Back.CYAN + "\n Lista de Prodcutos: " + Style.RESET_ALL)
    for producto in productos:
        print(f"ID: {producto[0]}, Producto: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: $ {producto[4]:.2f}, Categoria: {producto[5]}") 

def buscar_producto(id_producto):
    """Buscar productos en el inventario, mediante su ID."""
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    if producto:
        print(Back.CYAN + "\n Prodcuto: " + Style.RESET_ALL)
        print(f"ID: {producto[0]}, Producto: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: $ {producto[4]:.2f}, Categoria: {producto[5]}")
    else:
        print(Fore.RED + "Producto no encontrado en el inventario." + Style.RESET_ALL)

def buscar_producto_nombre(nombre_producto):
    """Buscar productos en el inventario por Nombre."""
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre_producto,))
    productos = cursor.fetchall()
    for producto in productos:
        print(f"ID: {producto[0]}, Producto: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: $ {producto[4]:.2f}, Categoria: {producto[5]}")
    else:
        print(Fore.RED + "Producto no encontrado en el inventario." + Style.RESET_ALL)

def actualizar_producto(id_producto):
    """Actualizar datos de productos, mediante su ID."""
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    if producto:
        print(f"Producto actual: {producto}")
        nombre = input("Nuevo nombre: ")
        descripcion = input("Nueva descripción: ")
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))
        categoria = input("Nueva categoría: ")

        cursor.execute('''
            UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        ''', (nombre, descripcion, cantidad, precio, categoria, id_producto))
        conexion.commit()
        print(Fore.GREEN + "Producto actualizado exitosamente en el inventario." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Producto no encontrado." + Style.RESET_ALL)

def eliminar_producto(id_producto):
    """Eliminar producto del inventario"""
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    if cursor.rowcount > 0:
        print(Fore.GREEN + "Producto eliminado del inventario." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Producto no encontrado en el inventario." + Style.RESET_ALL)

def reporte_bajo_stock(cantidad_unidades):
    """Reporte de productos según stock"""
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (cantidad_unidades,))
    productos = cursor.fetchall()
    if productos:
        print(Back.CYAN + f"Los siguientes productos tienen un stock inferior o igual a {cantidad_unidades} unidades." + Style.RESET_ALL) 
        for producto in productos:
            
            print(Fore.RED + f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]}")
    else:
        print(Fore.GREEN + f"Todos los productos tienen un stock superior a {cantidad_unidades} unidades." + Style.RESET_ALL)

def main(): # Menú interactivo
    while True:
        print(Fore.BLUE + "======Menú de Opciones======" + Style.RESET_ALL)
        print("1. Registrar producto")
        print("2. Ver todos los productos")
        print("3. Buscar por ID")
        print("4. Buscar por nombre")
        print("5. Actualizar producto")
        print("6. Eliminar producto")
        print("7. Reporte de bajo stock")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1": # Agregar producto
            while True: 
                nombre_producto = input("Ingrese el nombre del producto: ").strip()
                if nombre_producto != "":
                    break
                else:
                    print(Fore.RED + "El nombre del producto NO puede quedar vacio. " + Style.RESET_ALL)

            while True: 
                descripcion_producto = input("Ingrese una breve descripción del producto: ").strip()
                if descripcion_producto != "":
                    break
                else:
                    print(Fore.RED + "La descripción del producto NO puede quedar vacio. " + Style.RESET_ALL)

            while True:
                try:
                    cantidad_producto = float(input("Ingrese la cantidad producto: "))
                    if cantidad_producto > 0:
                                    break
                    else:
                        print(Fore.RED + "La cantidad del producto NO puede ser menor a 0. " + Style.RESET_ALL)
                except ValueError:
                        print(Fore.RED + "Entrada inválida. Por favor, ingrese un número para la cantidad.\n" + Style.RESET_ALL)

            while True:
                try:
                    precio_producto = float(input("Ingrese el precio del producto: "))
                    if precio_producto > 0:
                        break
                    else:
                        print(Fore.RED + "El precio del producto NO puede ser menor a 0. " + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "Entrada inválida. Por favor, ingrese un número para el precio.\n" + Style.RESET_ALL)
            
            while True: 
                categoria_producto = input("Ingrese la categoria del producto: ").strip()
                if categoria_producto != "":
                    break
                else:
                    print(Fore.RED + "La categoria del producto NO puede quedar vacio. " + Style.RESET_ALL)

            registrar_producto(nombre_producto, descripcion_producto, cantidad_producto, precio_producto, categoria_producto)

        elif opcion == '2': # Mostrar todos los productos del inventario
            mostrar_productos()
        
        elif opcion == '3': # Busca producto en el inventario por su ID
            id_producto = input("Ingrese el ID del producto: ").strip()
            buscar_producto(id_producto)

        elif opcion == '4':  # Busca producto en el inventario por su nombre
            nombre_producto = input("Ingrese el nombre del producto: ").strip()
            buscar_producto(nombre_producto)

        elif opcion == '5':
            id_producto = input("Ingrese el ID del producto que desea actualizar: ").strip()
            actualizar_producto(id_producto)

        elif opcion == '6':
            id_producto = input("Ingresá el ID del producto que desea eliminar: ").strip()
            eliminar_producto(id_producto)

        elif opcion == '7': 
            cantidad_unidades = int(input("Ingrese la cantidad de unidades que por las que desea consultar el stock: "))
            reporte_bajo_stock(cantidad_unidades)

        elif opcion == '8':
            print(Fore.MAGENTA + "Saliendo del sistema ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()