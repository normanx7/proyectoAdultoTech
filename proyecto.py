# Talento Lab, Entrega de Proyecto - Norman Primera DNI 19102676 #25047

inventario_productos = []

def agregar_producto(): # Agregar producto - nombre, categoría, y precio
        while True:
            ingresar_nombre_producto = input("Ingrese el nombre del producto: ").strip().capitalize()
            if ingresar_nombre_producto != "":
                break
            else:
                print("El nombre del producto NO puede estar vacío. Inténte de nuevo.\n")

        while True:
            ingresar_categoria_produc = input("Ingrese la categoria del prodcuto: ").strip().capitalize()
            if ingresar_categoria_produc != "":
                break
            else:
                print("La categoria del producto NO puede estar vacía. Inténte de nuevo.\n")

        while True:
            try:
                ingresar_precio_producto = int(input("Ingrese el precio del prodcuto: "))
                if ingresar_precio_producto > 0:
                    break
                else:
                    print("El precio del producto NO puede ser menor a 0. Inténte de nuevo.\n")
            except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número para el precio.\n")
        
        nuevo_producto = {
            'nombre': ingresar_nombre_producto,
            'categoria': ingresar_categoria_produc,
            'precio': ingresar_precio_producto
        }

        inventario_productos.append(nuevo_producto)
        print(f"!- El producto: '{ingresar_nombre_producto}', fue ingresado al inventario.\n")

def mostrar_productos(): # Mostrar productos
    if not inventario_productos:
        print("Inventario vacio.\n")
    else:
        print("!--Productos en inventario--!")
        for producto in inventario_productos:
            print(f"* Producto: '{producto['nombre']}', Categoría: '{producto['categoria']}', Precio: '{producto['precio']}'.")

def buscar_producto(): # Buscar producto
    if not inventario_productos:
        print("Inventario vacio, no hay productos para buscar.-\n")
    else:
        buscar_producto = input("Ingrese el producto que desea buscar: ").strip().capitalize()
        en_inventario = False
        for producto in inventario_productos:
            if producto['nombre'] == buscar_producto:
                print(f" Disponible, producto: '{producto['nombre']}', categ.: '{producto['categoria']}', precio: '{producto['precio']}'.")
                en_inventario = True
                break
        if not en_inventario:
            print(f"El producto '{buscar_producto}' no se encuentra en el inventario.\n")

def borrar_producto(): # Eliminar producto
    if not inventario_productos:
        print("Inventario vacio, no hay productos para eliminar.-\n")
    else:
        eliminar_producto = input("Ingrese el producto que desea eliminar: ").strip().capitalize()
        eliminado = False
        for i, producto in enumerate(inventario_productos):
            if producto['nombre'] == eliminar_producto:
                inventario_productos.pop(i)
                print(f"El producto '{eliminar_producto}' fue eliminado del inventario.\n")
                eliminado = True
        if not eliminado:
            print(f"El producto '{eliminar_producto}' no existe en el inventario.\n")

def mostrar_menu():
    while True:
        print("\n!!--Menú de Opciones:--!!\n 1. Agregar producto\n 2. Mostrar productos\n 3. Buscar producto\n 4. Eliminar producto\n 5. Salir\n.")

        opcion = input("-. Seleccione una opción (número): ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            borrar_producto()        
        elif opcion == "5":
            print("¡Gracias por usar el programa! ¡Chau!")
            break
        else:
            print("Opción no válida. Por favor, ingresá un número del 1 al 5.\n")

mostrar_menu()

