# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.
    """
    if indice>=len(lista) or  indice<= -len(lista):
        return None
    else:
     return lista[indice]
    pass  # Reemplazar con tu implementación

