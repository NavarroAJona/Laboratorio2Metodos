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

def add_decorators(words, decorator, n):
    newList=[]
    counterList=0
    for pokemon in words:
        innerCounter=0
        while(innerCounter!=n):
            pokemon = decorator + pokemon + decorator
            innerCounter+=1
        newList.insert(counterList,pokemon)
        counterList+=1

    return newList
hola= add_decorators(load_words("poke.csv"),"$",2)
print(hola)