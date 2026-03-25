import csv

def guardar_csv(inventario, ruta):
    if len(inventario) == 0:
        print("No hay datos para guardar")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Formato incorrecto")
                return []

            for fila in reader:
                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"Archivo cargado. Errores: {errores}")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
        return []
