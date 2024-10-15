from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla


def sumar_lista(matriz:list[list], indice:int)->float:
    """_summary_ suma la una lista de tipo int y la devuelve
    Args:
        matriz (list[list]): matriz de datos
        indice (int): indice de la lista que queremos sumar
    Returns:
        float: suma total
    """
    suma = 0
    lista = matriz[indice]
    for indice in range (len(lista)):
        elemento_actual = lista[indice]
        suma += elemento_actual 
    return suma

