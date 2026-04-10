# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    """
    Verifica si ambas listas tienen el mismo elemento en la tercera posición.
    Si alguna de las listas no tiene un tercer elemento, retorna False.
    Returns:
        True si ambas listas tienen el mismo tercer elemento, False en caso contrario
    """
    if len(lista1)>=3 and len(lista2)>=3:
      if lista1[2]==lista2[2]:
        return True
      else: return False
    else: return False
    pass  # Reemplazar con tu implementación
