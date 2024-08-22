import pytest
from inventario import agregar_productos, actualizar_stock, eliminar_producto, buscar_producto, productos

def setup_function():
    productos.clear()


def test_agregar():
    agregar_productos("Manzanas", 50, 2.50)
    assert buscar_producto("Manzanas") == {"cantidad" : 50, "precio" : 2.50}
    with pytest.raises(ValueError):
        agregar_productos("Manzanas", 100, 200) # El Producto ya existe

def test_actualizar():
    agregar_productos("Manzanas", 50, 2.50)
    actualizar_stock("Manzanas", 500)
    assert buscar_producto("Manzanas") == {"cantidad" : 500, "precio" : 2.50}
    with pytest.raises(KeyError):
        actualizar_stock("Peras", 50) # No Existe

def test_eliminar():
    agregar_productos("Manzanas", 50, 2.50)
    eliminar_producto("Manzanas")
    assert buscar_producto("Manzanas") is None

    with pytest.raises(KeyError):
        eliminar_producto("Peras", 50) # No existe
    
def test_buscar():
    agregar_productos("Manzanas", 50, 2.50)
    assert buscar_producto("Manzanas") == {"cantidad" : 50, "precio" : 2.50}
    assert buscar_producto("Peras") is None

    with pytest.raises(KeyError):
        buscar_producto("Banana") # No existe