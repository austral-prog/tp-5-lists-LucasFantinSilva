# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas
    Returns:
        La lista de listas modificada según las reglas
    """
    lista1, lista2, lista3=lista_de_listas
    lista1=lista1[:2]
    lista2=lista2[1:4]
    lista3=lista3[-2:]
    result=[lista1,lista2,lista3]
    return result
    pass  # Reemplazar con tu implementación

lista = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_lists(lista))