from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n===== MENÚ DEL INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Salir")
    print("===============================")

def main():
    """Función principal que controla el flujo del programa."""
    inventario = {}  # Diccionario de productos: nombre -> {precio, cantidad}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            # Agregar producto
            agregar_producto(inventario)
            print("✔ Producto agregado.")

        elif opcion == "2":
            # Mostrar inventario completo
            mostrar_inventario(inventario)

        elif opcion == "3":
            # Buscar producto
            nombre = input("Nombre del producto a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print("Producto encontrado:\nPrecio:", producto['precio']," |  Cantidad: ", producto['cantidad'])
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "4":
            # Actualizar producto
            nombre = input("Nombre del producto a actualizar: ")
            # Convertimos solo si no están vacíos
            # servicios.actualizar_producto solicita solo (inventario, nombre)
            # Las conversiones y opciones se manejan dentro de la función de servicios
            actualizado = actualizar_producto(inventario, nombre)

        elif opcion == "5":
            # Eliminar producto
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)
            
        elif opcion == "6":
            # Calcular estadísticas
            est = calcular_estadisticas(inventario)
            print("\n📊 ESTADÍSTICAS DEL INVENTARIO:")
            print(f"Total de productos: {est['total_productos']}")
            print(f"Valor total: {est['valor_total']}")
            print(f"Producto más caro: {est['producto_mas_caro']}")
            print(f"Precio del producto más caro: {est['precio_producto_mas_caro']}")

        elif opcion == "7":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()