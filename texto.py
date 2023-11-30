'''
Este py tiene comoobjetivo cargar el texto de la novela de Alicia y preparar el texto,
realizando la normalización del mismo y su tokenización en una lista. Hace uso del módulo de funciones101
'''
from funciones101 import *
from custom_types import *

def leer_fichero_libro(titulo: str)-> str:
    ''' lee el fichero del libro y lo retorna en una cadena '''
    try:
        cadena = read_file(titulo)  # 'alice_full_text.txt'
    except FileNotFoundError as e:
        print(f"Error en el acceso al fichero- > {e}")
    return cadena
    

def preparar_Texto(cadena: str)-> list[str]:
    ''' 
    Recibe una cadena con el texto de la novela de Alicia y normaliza el texto, dejándolo tokenizado en una lista 
    '''
    #Tokenizo
    cadena_pura = normalizacion(cadena)
    lista_tokens = cadena_pura.split()
    #limpio
    return lista_tokens


if __name__ == "__main__":
  try:
    cadena = leer_fichero_libro('alice_full_text.txt')
    texto_tokenizado = preparar_Texto(cadena)
  except FileNotFoundError as e:
     print(f"Error: Fichero no encontrado -> {e}")
   
