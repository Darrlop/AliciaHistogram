'''
Vertebra el programa para realizar el histograma, funcionando como "main" e incorporando
las función principal para el conteo de palabras. Aunque incorporo custom_types, indico
los tipos de manera estándar para coger fondo en ello
'''
# Opciones:
# from  slugify import slugify  -> formatea texto humano a uno que entienda una máquina con el separador que tú quieras
# import pandas as pd  -> formatea texto para ordenarlo visualmente en columnas y filas -instalac-> pip install pandas en consola

import pandas as pd
import jinja2  # para poder aplicar colores a pandas
from funciones101 import *
from custom_types import *
from texto import leer_fichero_libro, preparar_Texto
from stopwords import load_stopwords
from functools import reduce
from colorama import init, Fore, Back, Style  # para modificar estilo de fondo y letras 

def count_words(texto_tokenizado: list[str], set_stopwords: set[str])-> dict[str:int]:
    '''
    Recibe una lista de palabras (texto) y un set con las stopwords. Construyo un diccionario
    con aquellas palabras que no están en las stopwords, indicando su número de apariciones
    '''    
    apariciones = dict()
    histograma = dict()

    def add_count_palabra(palabra: str)-> None:
        if palabra in apariciones:
            apariciones[palabra] += 1
        else:
            apariciones[palabra] = 1
    
    
    for palabra in texto_tokenizado:
        if palabra not in set_stopwords:
            add_count_palabra(palabra)
    ### Opción aplicando  pandas para formatear el resultado en un formato más accesible a la vista si deseo imprimirlo###
    #df = pd.DataFrame(list(apariciones.items()), columns = ['Palabra', 'Apariciones']) 
    #df = df.sort_values('Apariciones', ascending=False)
    #pd.set_option('display.max_rows', None)
    #print(df) lo pongo en comentario para que vaya al return directo
    #
    #   Si quisiera eliminar lq 1ª col en la visualización, que es un índice propio que crea el dataframe
    # df_str = df.to_string(index=False)
    # print(df_str)
       
    return apariciones
    
def grand_total_words(apariciones: dict[str:int])-> int:
    return(reduce(lambda acum, palabra: acum + apariciones[palabra], apariciones, 0))

def make_histogram(apariciones: dict[str:int], total_palabras: int)-> dict[str:float]:
    return(
        # Esto crea un objeto map, por lo que hay que castearlo a dict. La función crea para cada
        # iteración una tupla (palabra, frecuencia) que luego permite hacer esa conversión a diccionario
        dict(map(lambda palabra : (palabra, apariciones[palabra]/total_palabras) , apariciones))  
    )

def mostrar_tabla(histograma: dict[str:float])-> None:
    #   Creo el dataframe con las columnas indicadas y las ordeno de más a menos según las apariciones
    df = pd.DataFrame(list(histograma.items()), columns = ['Palabra', 'Frecuencia'])
    df = df.sort_values('Frecuencia', ascending = False)
    #   Elimino el limite de filas a mostrar, para ver todas
    pd.set_option('display.max_rows', None)
    #   Si quisiera eliminar lq 1ª col en la visualización, que es un índice propio que crea el dataframe
    #df_str = df.to_string(index=False)
    #print(df_str)
    return df
    
    

try:    
    cadena = leer_fichero_libro('alice_full_text.txt')
    texto_tokenizado = preparar_Texto(cadena)
    set_stopwords = load_stopwords('stopwords.txt')
except FileNotFoundError as e:
    print(f"Error: Fichero no encontrado -> {e}")

apariciones = count_words(texto_tokenizado, set_stopwords)
total_palabras = grand_total_words(apariciones)
histograma = make_histogram(apariciones, total_palabras)
init()  # para inicializar la biblioteca colorama
print(Back.GREEN + "HISTOGRAMA DE 'ALICIA EN EL PAÍS DE LAS MARAVILLAS'" + Back.RESET)
print(mostrar_tabla(histograma))