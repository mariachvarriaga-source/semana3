def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("Inventario vacío")
    else:
        for p in inventario:
            print(f"{p['nombre']} - ${p['precio']} - Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None:
            p["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            p["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        return True
    return False


def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        return None

    unidades = sum(p["cantidad"] for p in inventario)
    valor = sum(p["precio"] * p["cantidad"] for p in inventario)

    mas_caro = max(inventario, key=lambda x: x["precio"])
    mayor_stock = max(inventario, key=lambda x: x["cantidad"])

    return {
        "unidades": unidades,
        "valor": valor,
        "mas_caro": mas_caro,
        "mayor_stock": mayor_stock
    }
