from .data import matriz_concesionaria
from .auxiliares import sumar_lista
"""
0 lista marcas
1 lista modelo
2 lista cantidades
3 lista precios
4 lista recaudacion

"""

print (matriz_concesionaria)
#2 Calcular la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.

def punto_dos(matriz:list[list])->None:
    """_summary_ suma las unidades de todas las concesionarias y las retorna
    Args:
        matriz (list[list]): matriz de datos
    """
    cantidad_total = sumar_lista(matriz, 2)
    print (f"la cantidad total de unidades almacenadas es: {cantidad_total}")

#sin terminar
def punto_cinco(matriz:list[list]):
    lista_cantidades = matriz[2]
    lista_precios = matriz[3]
    lista_recaudacion = []
    for indice in range(len(lista_cantidades)):
        for subindice in range(len(lista_precios)):
            recaudacion = lista_cantidades[indice]*lista_precios[subindice]
    lista_recaudacion.append(recaudacion)




