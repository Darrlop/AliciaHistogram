'''
Funciones creadas en el bootcamp Programación101. El archivo es un compendio de funcionalidades varias 
'''

import string
import unicodedata

def remove_puntuacion(frase):
    caracteres=string.punctuation #Cadena preinicializada en python con los signos de puntuación más habituales
    frase_despuntuada = ""
    i =0
    while i < len(frase):
        if frase[i] not in caracteres:
            frase_despuntuada = frase_despuntuada + frase[i]
        i += 1
    return frase_despuntuada

def eliminar_acentos(cadena):
    forma_nfkd = unicodedata.normalize('NFKD', cadena)
    solo_ascii = forma_nfkd.encode('ASCII', 'ignore')
    return solo_ascii.decode()

def normalize_text(text):
    text = text.lower()  # convertir a minúsculas
    text = text.strip()  # eliminar espacios en blanco al inicio y al final
    return text

def normalizacion(frase):
    normalizada = ""
    normalizada = normalize_text(eliminar_acentos(remove_puntuacion(frase)))
    return normalizada


# Compresor Universal
def compress(elements, initial_value, operation):
    """
    Recibe una secuencia de elementos, un valor inicial y
    una función que representa una operación de combinación
    de dos elementos.
    Devuelve un solo valor comprimido
    """
    accum = initial_value
    for element in elements:
        accum = operation(accum, element)
    return accum

# Selector Universal
def select(elements: list, predicate)-> list:
    """
    Recibe una lista y un predicado. Devuelve una nueva lista con aquellos elementos
    que superan el test del predicado.
    """
    selected = []
    for element in elements:
        if predicate(element):
            selected.append(element)
    return selected

# Transformador Universal
def transform(elements:list, change_element) ->list :
    """
    Recibe una lista y una función para cambiar uno o más elementos. Devuelve una nueva lista 
    con dicha modificación
    """
    new_list = []
    for element in elements:
        new_list.append(change_element(element))
    return new_list

def read_file(text_file: str)->str:
  """
  Abre mediante with open el fichero cuyo nombre te pasan
  por parámetro y devuelve su contenido como una cadena
  """
  texto = ""
  with open (text_file, 'r', encoding='utf_8' ) as mi_file:    
    texto = mi_file.read()
  return texto