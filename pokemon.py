from ctypes.wintypes import HLOCAL
from re import A
from turtle import pos
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
    transitionDicts = {}
    sequenceSize = len(sequences[0])
    for sequenceOuter in sequences:
        transitionDicts[sequenceOuter] = {}
        for sequenceInner in sequences:
           transitionDicts[sequenceOuter][sequenceInner] = 0 
    for word in words:
        wordLength = len(word)
        for i in range(wordLength-sequenceSize):
            transitionDicts[word[i:i+sequenceSize]][word[i+1:i+1+sequenceSize]] += 1
    sequenceAmount = len(sequences)
    transitions = np.zeros((sequenceAmount, sequenceAmount) ,dtype=float)
    for i in range(sequenceAmount):
        for j in range(sequenceAmount):
            transitions[i][j] = transitionDicts[sequences[i]][sequences[j]]
        transitions[i] /= np.sum(transitions[i])
    print(transitions)
    return transitions

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
#matrix,seq = create_model(entradaEjemplo,ngrama)
#print(matrix,seq)

