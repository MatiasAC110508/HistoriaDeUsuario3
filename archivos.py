import csv
import os

# Ruta por defecto donde se guardarán tus CSV
CARPETA = "Datos"
ARCHIVO = "inventario.csv"


def guardar_csv(inventario, ruta=None, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    - inventario: lista de diccionarios.
    - ruta: ruta completa del archivo.
    """
    if not inventario:
        print("❌ ERROR: El inventario está vacío. No se puede guardar.\n")
        return False

    # Generar ruta por defecto si no se envía una
    if ruta is None:
        os.makedirs(CARPETA, exist_ok=True)
        ruta = os.path.join(CARPETA, ARCHIVO)

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["nombre", "precio", "cantidad"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if incluir_header:
                writer.writeheader()

            writer.writerows(inventario)

        print(f"✔ Inventario guardado en: {ruta}\n")
        return True

    except Exception as e:
        print(f"❌ ERROR al guardar el CSV: {e}\n")
        return False



def cargar_csv(inventario, ruta=None):
    """
    Carga productos desde un CSV al inventario.
    - inventario: lista donde se cargarán los productos.
    """
    if ruta is None:
        ruta = os.path.join(CARPETA, ARCHIVO)

    if not os.path.exists(ruta):
        print(f"❌ ERROR: No existe el archivo CSV: {ruta}\n")
        return False

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # Limpiar inventario actual
            inventario.clear()

            for row in reader:
                inventario.append({
                    "nombre": row["nombre"],
                    "precio": float(row["precio"]),
                    "cantidad": int(row["cantidad"])
                })

        print(f"✔ Inventario cargado desde: {ruta}\n")
        return True

    except Exception as e:
        print(f"❌ ERROR al cargar CSV: {e}\n")
        return False



def exportar_csv(inventario):
    """
    Exporta el inventario en una carpeta llamada 'Exportados'.
    Ideal para opción de 'Exportar CSV' del menú.
    """
    if not inventario:
        print("❌ ERROR: El inventario está vacío. No se puede exportar.\n")
        return False

    carpeta = "Exportados"
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, ARCHIVO)

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["nombre", "precio", "cantidad"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(inventario)

        print(f"✔ CSV exportado correctamente en: {ruta}\n")
        return True

    except Exception as e:
        print(f"❌ ERROR al exportar CSV: {e}\n")
        return False
