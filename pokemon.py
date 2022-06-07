from ctypes.wintypes import HLOCAL
from re import A
from turtle import pos
import numpy as np
import random
#De momento no se hace ninguna limpieza ya que no parece necesario
def load_words(filename):
    pokemonList = []
    with open(filename, "r") as archive:
        counter=0
        for line in archive:
            pokemonList.insert(counter,line.lower().replace("\n",""))
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
        while(innerRange!=len(word)-n):
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
    return transitions

def create_model(words,ngrams):
    decorators = add_decorators(words,"$",ngrams)
    sequence = get_sequences(decorators,ngrams)
    matrix= calculate_transitions(decorators,sequence)
    return (matrix,sequence)

def generate_word(model,seed):
    r = random.Random()
    r.seed(seed)
    transition, sequences = model
    sequenceLength = len(sequences[0])
    finished = False
    endSequence = "$"*sequenceLength
    generatedWord = ''
    transitionRowIndex = 0
    first = True
    while not finished:
        roll = r.random()
        sum = 0
        transitionColumnIndex = -1
        while sum < roll:
            transitionColumnIndex += 1
            cellValue = transition[transitionRowIndex][transitionColumnIndex]
            sum += cellValue
        transitionRowIndex = transitionColumnIndex
        if first:
            generatedWord += sequences[transitionColumnIndex]
            first = False
        else:
            generatedWord += sequences[transitionColumnIndex][-1]
        finished = (sequences[transitionColumnIndex] == endSequence)
    generatedWord = generatedWord.replace("$","")
    return generatedWord.capitalize()

#entradaEjemplo = ['hello','world']
#e= ["casa"]
#palabras = load_words("pokemon.csv")
#ngrama=2
#model = create_model(palabras,1)
#print(generate_word(model, 17))
#model = create_model(palabras,2)
#print(generate_word(model, 42))
#model = create_model(palabras,3)
#print(generate_word(model, 21))
#r = random.Random()
#semilla =420
#r.seed(semilla)
#a=generate_word(create_model(entradaEjemplo,ngrama),value)
#print(matrix,seq)