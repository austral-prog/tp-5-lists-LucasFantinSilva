# Ejercicio 3: Agregar elementos al principio y final

def add_elements(lista):
    """
    Agrega 'Pink' al principio y 'Yellow' al final de la lista.
    """
    lista.append("Yellow")
    lista.insert(-len(lista),"Pink")
    return lista
    pass  # Reemplazar con tu implementación


lista = []
print(add_elements(lista))