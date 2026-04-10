# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.
    """
    if len(lista)==0:
        return []
    else:
        del lista[0]
        if len(lista) > 5:
         del lista[3]
         del lista[3]
        elif len(lista)==5:
         del lista[-1]
         del lista[-1]
        elif len(lista)==4:
         del lista[-1]
        return lista
    pass  # Reemplazar con tu implementación

print(len([]))
