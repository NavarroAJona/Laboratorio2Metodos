import pandas as pd

#De momento no se hace ninguna limpieza ya que no parece necesario
def load_words(filename):
    pokemonList = []
    with open(filename, "r") as archive:
        counter=0
        for line in archive:
            pokemonList.insert(counter,line.rstrip())
            counter +=1
    return pokemonList

hola= load_words("pokemon.csv")
print(hola)