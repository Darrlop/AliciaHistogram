'''
Este py tiene como objetivo cargar el archivo con las stopwords que aplicaremos en el histograma posterior.
No requiere de normalización pero si de tokenización en formato de colección/set. Hace uso del módulo de funciones101
'''
from funciones101 import read_file

def load_stopwords(fichero_words: str)-> set[str]:
  ''' Carga y tokenización del fichero de stopwords.txt. Se devuelve una colección/set con las stop words'''
  stopw = read_file(fichero_words)
  stopw = stopw.split()
  set_stopwords = set(stopw)
  return set_stopwords


if __name__ == "__main__":
  try:
    set_stopwords = load_stopwords('stopwords.txt')
  except FileNotFoundError as e:
    print(f"Error: Fichero no encontrado -> {e}")