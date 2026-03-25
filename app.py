from servicios import *
from archivos import *

inventario = []
opcion = 0

while opcion != 9:

    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    try:
        opcion = int(input("Elige opción: "))

        if opcion == 1:
            n = input("Nombre: ")
            p = float(input("Precio: "))
            c = int(input("Cantidad: "))
            agregar_producto(inventario, n, p, c)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            n = input("Buscar: ")
            p = buscar_producto(inventario, n)
            print(p if p else "No encontrado")

        elif opcion == 4:
            n = input("Producto: ")
            p = float(input("Nuevo precio: "))
            c = int(input("Nueva cantidad: "))
            if not actualizar_producto(inventario, n, p, c):
                print("No existe")

        elif opcion == 5:
            n = input("Eliminar: ")
            if not eliminar_producto(inventario, n):
                print("No existe")

        elif opcion == 6:
            est = calcular_estadisticas(inventario)
            if est:
                print("Unidades:", est["unidades"])
                print("Valor total:", est["valor"])
                print("Más caro:", est["mas_caro"]["nombre"])
                print("Mayor stock:", est["mayor_stock"]["nombre"])
            else:
                print("Sin datos")

        elif opcion == 7:
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                resp = input("¿Reemplazar inventario? (s/n): ").lower()

                if resp == "s":
                    inventario = nuevos
                else:
                    inventario.extend(nuevos)

        elif opcion == 9:
            print("Saliendo...")

        else:
            print("Opción inválida")

    except:
        print("Error en datos, intenta otra vez")
