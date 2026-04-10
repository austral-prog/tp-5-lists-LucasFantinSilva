# Ejercicio 6: Encontrar el mínimo en una lista

def find_min(lista):
    """
    Encuentra y retorna el valor mínimo en una lista de números.
    Si la lista está vacía, retorna None.
    """
    if len(lista) == 0:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        if len(lista) >= 2:
            if lista[0] < lista[1]:
                m = lista[0]
            else: m=lista[1]
        if len(lista) >= 3:
            if lista[2] < m:
                m = lista[2]
        if len(lista) >= 4:
            if lista[3] < m:
                m = lista[3]
        if len(lista) >= 5:
            if lista[4] < m:
                m = lista[4]
        if len(lista) >= 6:
            if lista[5] < m:
                m = lista[5]
        if len(lista) >= 7:
            if lista[6] < m:
                m = lista[6]
        return m
    pass  # Reemplazar con tu implementación
