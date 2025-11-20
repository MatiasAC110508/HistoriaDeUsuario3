"""Módulo de servicios para la gestión de inventario."""

def agregar_producto(inventario):
    """Agrega un nuevo producto al inventario."""
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    inventario[nombre] = {
        'precio': precio,
        'cantidad': cantidad
    }
    print(f"Producto '{nombre}' agregado al inventario.")   
    
def mostrar_inventario(inventario):
    """Muestra todos los productos en el inventario."""
    if not inventario:
        print("El inventario está vacío.")
        return
    
    print("Inventario:")
    for nombre, detalles in inventario.items():
        print(f"Producto: {nombre} | Precio: {detalles['precio']} | Cantidad: {detalles['cantidad']}")
        
def buscar_producto(inventario, nombre):
    """Busca un producto por nombre en el inventario."""
    return inventario.get(nombre, None)

def actualizar_producto(inventario, nombre):
    """Actualiza el precio y/o cantidad de un producto existente."""
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
        return
    
    nuevo_precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
    nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
    
    if nuevo_precio:
        producto['precio'] = float(nuevo_precio)
    if nueva_cantidad:
        producto['cantidad'] = int(nueva_cantidad)
    
    print(f"Producto '{nombre}' actualizado.")
    
def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario."""
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
        
def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario."""
    total_productos = len(inventario)
    valor_total = sum(detalles['precio'] * detalles['cantidad'] for detalles in inventario.values())
    producto_mas_caro = max(inventario.items(), key = lambda item: item[1]['precio'], default=(None, None))
    producto_mayor_stock = max(inventario.items(), key = lambda item: item[1]['cantidad'], default=(None, None))
    
    estadisticas = {
        'total_productos': total_productos,
        'valor_total': valor_total,
        'producto_mas_caro': producto_mas_caro[0] if producto_mas_caro[0] else None,
        'precio_producto_mas_caro': producto_mas_caro[1]['precio'] if producto_mas_caro[1] else None,
        'producto_mayor_stock': producto_mayor_stock[0] if producto_mayor_stock[0] else None
    }
    
    return estadisticas