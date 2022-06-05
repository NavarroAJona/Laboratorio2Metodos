from ctypes.wintypes import HLOCAL
from re import A
import pandas as pd
import bisect

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

#Definitivamente podria tener mejores nombres pero es muy tarde y no lo se
def get_sequences(words, n):
    sequenceList = []
    counterList = 0
    for word in words:
        innerRange=0
        while(innerRange!=len(word)-1):
            subSequence = (word[innerRange:innerRange+n]).lower()
            if((subSequence in sequenceList)==False):
                sequenceList.insert(counterList,subSequence)
            innerRange+=1
    return sorted(sequenceList)


hola= get_sequences(add_decorators(load_words("poke.csv"),"$",2),1)
print(hola)