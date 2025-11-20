from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)

from archivos import (
    cargar_csv,
    exportar_csv,
    guardar_csv
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
    print("7. Cargar inventario desde CSV")
    print("8. Exportar inventario a CSV")
    print("9. Guardar inventario (CSV por defecto)")
    print("10. Salir")
    print("================================")


def main():
    """Función principal que controla el flujo del programa."""
    inventario = []   # Lista de productos. Cada producto es un diccionario.

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
                print("\nProducto encontrado:")
                print(f"Precio: {producto['precio']}  |  Cantidad: {producto['cantidad']}")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "4":
            # Actualizar producto
            nombre = input("Nombre del producto a actualizar: ")
            actualizado = actualizar_producto(inventario, nombre)
            if actualizado:
                print("✔ Producto actualizado.")
            else:
                print("❌ No se pudo actualizar el producto.")

        elif opcion == "5":
            # Eliminar producto
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "6":
            # Calcular estadísticas
            est = calcular_estadisticas(inventario)
            if est:
                print("\n📊 ESTADÍSTICAS DEL INVENTARIO:")
                print(f"Total de productos: {est['total_productos']}")
                print(f"Valor total del inventario: {est['valor_total']}")
                print(f"Producto más caro: {est['producto_mas_caro']}")
                print(f"Precio del producto más caro: {est['precio_producto_mas_caro']}")
            else:
                print("❌ No hay productos para calcular estadísticas.")

        elif opcion == "7":
            cargar_csv(inventario)

        elif opcion == "8":
            exportar_csv(inventario)

        elif opcion == "9":
            guardar_csv(inventario)

        elif opcion == "10":
            print("👋 Hasta pronto!")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
