'''
Vertebra el programa para realizar el histograma, funcionando como "main" e incorporando
las función principal para el conteo de palabras. Aunque incorporo custom_types, indico
los tipos de manera estándar para coger fondo en ello
'''
# Opciones:
# from  slugify import slugify  -> formatea texto humano a uno que entienda una máquina con el separador que tú quieras
# import pandas as pd  -> formatea texto para ordenarlo visualmente en columnas y filas -instalac-> pip install pandas en consola

import pandas as pd
from funciones101 import *
from custom_types import *
from texto import leer_fichero_libro, preparar_Texto
from stopwords import load_stopwords

def count_words(texto_tokenizado: list[str], set_stopwords: set[str])-> dict[str:int]:
    '''
    Recibe una lista de palabras (texto) y un set con las stopwords. Construyo un diccionario
    con aquellas palabras que no están en las stopwords, indicando su número de apariciones
    '''    
    histograma = dict()

    def add_count_palabra(palabra: str)-> None:
        if palabra in histograma:
            histograma[palabra] += 1
        else:
            histograma[palabra] = 1


    for palabra in texto_tokenizado:
        if palabra not in set_stopwords:
            add_count_palabra(palabra)
    ###Aplico pandas para formatear el resultado en un formato más accesible a la vista###
    #   Creo el dataframe con las columnas indicadas y las ordeno de más a menos según las apariciones
    df = pd.DataFrame(list(histograma.items()), columns=['Palabra', 'Apariciones']) 
    df = df.sort_values('Apariciones', ascending=False)
    #   Elimino el limite de filas a mostrar, para ver todas
    pd.set_option('display.max_rows', None)
    print(df)
    #   Si quiero eliminar lq 1ª col en la visualización, que es un índice propio que crea el dataframe
    # df_str = df.to_string(index=False)
    # print(df_str)    
    

try:
    cadena = leer_fichero_libro('alice_full_text.txt')
    texto_tokenizado = preparar_Texto(cadena)
    set_stopwords = load_stopwords('stopwords.txt')
except FileNotFoundError as e:
    print(f"Error: Fichero no encontrado -> {e}")
count_words(texto_tokenizado, set_stopwords)
        