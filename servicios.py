"""Módulo de servicios para la gestión de inventario con listas de diccionarios."""

def agregar_producto(inventario):
    """Agrega un nuevo producto a la lista del inventario."""

    nombre = input("Nombre del producto: ").strip()

    # buscar si ya existe
    if buscar_producto(inventario, nombre):
        print("❌ ERROR: El producto ya existe.")
        return False

    # entrada segura
    while True:
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print("❌ ERROR: Ingresa valores numéricos correctos.")

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

    print(f"✔ Producto '{nombre}' agregado.")
    return True



def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario."""
    if not inventario:
        print("📭 El inventario está vacío.")
        return

    print("\n===== INVENTARIO =====")
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
    print("=======================")



def buscar_producto(inventario, nombre):
    """Devuelve un producto por su nombre, o None si no existe."""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None



def actualizar_producto(inventario, nombre):
    """Actualiza datos de un producto existente."""
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print("❌ Producto no encontrado.")
        return False

    print("Deja un valor en blanco para no modificarlo.")

    # precio
    nuevo_precio = input("Nuevo precio: ").strip()
    if nuevo_precio != "":
        try:
            producto["precio"] = float(nuevo_precio)
        except ValueError:
            print("❌ Precio inválido.")
            return False

    # cantidad
    nueva_cantidad = input("Nueva cantidad: ").strip()
    if nueva_cantidad != "":
        try:
            producto["cantidad"] = int(nueva_cantidad)
        except ValueError:
            print("❌ Cantidad inválida.")
            return False

    print(f"✔ Producto '{nombre}' actualizado.")
    return True



def eliminar_producto(inventario, nombre):
    """Elimina un producto por su nombre."""
    for i, p in enumerate(inventario):
        if p["nombre"].lower() == nombre.lower():
            inventario.pop(i)
            print(f"✔ Producto '{nombre}' eliminado.")
            return True

    print("❌ Producto no encontrado.")
    return False



def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario."""
    if not inventario:
        print("📭 No hay productos para calcular estadísticas.")
        return None

    total_productos = len(inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "total_productos": total_productos,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro["nombre"],
        "precio_producto_mas_caro": producto_mas_caro["precio"],
        "producto_mayor_stock": producto_mayor_stock["nombre"]
    }
