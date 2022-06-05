from ctypes.wintypes import HLOCAL
from re import A
from turtle import pos
import pandas as pd
import numpy as np

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

#Potencialmente nombres feos
def calculate_transitions(words, sequences):
    size = len(sequences)
    #Este sequencesSize se usa para mas adelante para
    #poder mezclar dos secuencias y ver si estan en una palabra
    sequencesSize = len(sequences[0])-1
    transitionMatrix = np.zeros((size,size))
    print(words)
    for i in range(0,size):
        divideValueCounter = 0
        for j in range(0,size):
            sequencesMerged = sequences[i] + sequences[j][sequencesSize:]
            if(any(sequencesMerged in string for string in words)):
                sequencesCounter = len([string for string in words if sequencesMerged in string])
                divideValueCounter +=sequencesCounter
                transitionMatrix[i][j]=sequencesCounter
        for position in range(0,size):
            if(transitionMatrix[i][position]!=0):
                transitionMatrix[i][position]=round(transitionMatrix[i][position]/divideValueCounter,3)
                
    return transitionMatrix

def create_model(words,ngrams):
    decorators = add_decorators(words,"$",ngrams)
    sequence = get_sequences(decorators,ngrams)
    matrix= calculate_transitions(decorators,sequence)
    return (matrix,sequence)

#Puse "wow" para comprobar que si nos funciona bien que si una subsecuencia
#aparece dos veces entonces salga 0.66 y 0.33, ahi si ve la explicacion
#del metodo 3 me entendera mejor creo
entradaEjemplo = ['hello','world']
palabras = load_words("poke.csv")
ngrama=1
#cuando nos pongamos modo loco cambiamos entradaEjemplo por palabras
#Creo que ya sirve para cualquier ngrama
matrix,seq = create_model(entradaEjemplo,ngrama)
print(matrix,seq)

