productos = {}
productos_array = []

def agregar_productos(nombre, cantidad, precio):
    # Excepciones
    if nombre in productos:
        raise ValueError("El producto ya existe")
    
    # Agregamos el producto
    productos[nombre] = {
        "cantidad" : cantidad,
        "precio" : precio
    }

def agregar_productos(nombre, cantidad, precio):
    if len(productos_array) > 0:
        for x in range(0, len(productos_array)):
            if productos_array[x]["nombre"] == nombre:
                print("existe")
            else:
                print("No existe")
    else:
        print("El arreglo esta vacio")

    producto = {
        "nombre" : nombre,
        "cantidad" : cantidad,
        "precio" : precio
    }
    
    productos_array.append(producto)

def actualizar_stock(nombre, nueva_cantidad):
    if nombre not in productos:
        raise KeyError("El producto no existe")
    
    productos[nombre]["cantidad"] = nueva_cantidad
        

def actualizar_stock(nombre, nueva_cantidad):
    # Excepcion ue el producto a actualizar existe
    # Actualizamos el stock (cantidad)

    for producto in productos_array:
        if producto["nombre"] == nombre:
            producto["cantidad"] = nueva_cantidad
        else:
            raise KeyError("El producto no existe")
        
def eliminar_producto(nombre):
    if nombre not in productos:
        raise KeyError("El producto no existe")
    # productos.pop(nombre)
    del productos[nombre]
    print("Producto Eliminado")

def buscar_producto(nombre): 
    if nombre not in productos:
        raise KeyError("El producto no existe")
    return productos.get(nombre, None)