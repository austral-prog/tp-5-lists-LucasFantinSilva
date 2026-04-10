# Ejercicio 5: Encontrar el máximo en una lista
m = 1
def find_max(lista):

    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.
    """

    if len(lista)==0:
        return None
    elif len(lista)==1:
        return lista[0]
    else:
     if len(lista)>=2:
        if lista[0]>lista[1]:
            m=lista[0]
        else: m=lista[1]
        if len(lista) >= 3:
            if lista[2] > m:
                m = lista[2]
     if len(lista)>=4:
        if lista[3]>m:
            m=lista[3]
     if len(lista)>=5:
        if lista[4]>m:
            m=lista[4]
     if len(lista)>=6:
        if lista[5]>m:
            m=lista[5]
     return m

    pass  # Reemplazar con tu implementación


result = find_max([-5, 10, -3, 0, 60])
print(result)