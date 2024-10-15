from UTN_Heroes_Dataset.utn_pp import get_original_matrix, clear_console
from .validaciones import validar_opcion
from .salida_consola import mostrar_menu
from .data import matriz_concesionaria
from .funciones import punto_dos

matriz_concesionaria = get_original_matrix()
def app_concesionaria(matriz)->None:
    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 9)
        match opcion:
            case 1: pass
            case 2: punto_dos(matriz)
            case 3: pass
            case 4: pass
            case 5: pass
            case 6: pass
            case 7: pass
            case 8: pass
            case 9: break
        clear_console()

if __name__ == "__main__":
    app_concesionaria(matriz_concesionaria)