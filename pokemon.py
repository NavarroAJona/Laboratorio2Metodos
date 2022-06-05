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
    sequencesSize = len(sequences[0])
    if(sequencesSize==1):
        sequencesSize=0
    transitionMatrix = np.zeros((size,size))
    for i in range(0,size):
        divideValueCounter = 1
        for j in range(0,size):
            sequencesMerged = sequences[i] + sequences[j][sequencesSize:]
            if(any(sequencesMerged in string for string in words)):
                #Con esto cuento cuantas veces se repite una subbsecuencia en todas las palabras
                sequencesCounter = [string for string in words if sequencesMerged in string]  
                divideValueCounter +=1
                transitionMatrix[i][j]=len(sequencesCounter)
        for position in range(0,size):
            if(transitionMatrix[i][position]!=0):
                transitionMatrix[i][position]=round(transitionMatrix[i][position]/divideValueCounter,3)
                
    print(transitionMatrix)
    return transitionMatrix

#Puse "wow" para comprobar que si nos funciona bien que si una subsecuencia
#aparece dos veces entonces salga 0.66 y 0.33, ahi si ve la explicacion
#del metodo 3 me entendera mejor creo
entradaEjemplo = ['$hello$','$world$','$wow$']
palabras = load_words("poke.csv")
decorador = "$"
#Sustituir con palabra si queremos cargar el csv
decoradores = add_decorators(entradaEjemplo,decorador,2)
secuencia= get_sequences(decoradores,1)
calculate_transitions(entradaEjemplo,secuencia)
print(secuencia)

