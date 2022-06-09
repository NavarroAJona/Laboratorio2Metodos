#Dominic Tarassenko B97790
#Jonathan Navarro B85580


from ctypes.wintypes import HLOCAL
from re import A
from turtle import pos
import numpy as np
import random

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

def get_probability(model,word):
    transition,sequences = model
    sequenceSize = len(sequences[0])
    possiblePokemon = add_decorators([word],"$",sequenceSize)[0].lower()
    probability = 1
    for position in range(0,len(possiblePokemon)):
        subSequence1 = possiblePokemon[position:position+sequenceSize]
        subSequence2 = possiblePokemon[position+1:position+sequenceSize+1]
        if subSequence2 not in sequences:
            #Imposible crear la subsecuencia
            probability = 0
            break
        if(len(subSequence1)==len(subSequence2)):
            transitionValue = transition[sequences.index(subSequence1)][sequences.index(subSequence2)]
            probability = probability*transitionValue
    return probability



seed = 5000
palabras = load_words("pokemon.csv")
model1 = create_model(palabras,1)
model2 = create_model(palabras,2)
model3 = create_model(palabras,3)


#valor1=get_probability(create_model(palabras,1),"mew")
#valor2=get_probability(create_model(palabras,2),"mew")
#valor3=get_probability(create_model(palabras,3),"mew")
#print("proba1:", valor1)
#print("proba2:", valor2)
#print("proba3:", valor3)

#valor1=get_probability(create_model(palabras,1),"dominic")
#valor2=get_probability(create_model(palabras,2),"dominic")
#valor3=get_probability(create_model(palabras,3),"dominic")
#valor4=get_probability(create_model(palabras,3),"dominic")
#print("proba1:", valor1)
#print("proba2:", valor2)
#print("proba3:", valor3)
#print("proba4:", valor4)
#ojo lo podemos cambiar jejeps

#PARTE 8 DEL LABORATORIO
#a ¿Por qué la probabilidad de formar un nombre parece aumentar conforme n incrementa?
#R/ Esto solo pasa con la probabilidad de formar un nombre de pokemon que esté en el csv.
# Conforme n incrementa, la cantidad de nombres que se pueden crear disminuye, y como
# la probabilidad de los nombres imposibles de formar con secuencias del n mayor se vuelve 0,
# forsozamente los que siguen siendo posibles tienen que aumentar en probabilidad, 
# para que todas las probabilidades sigan sumando 1

#b ¿Encontró algún otro nombre interesante para un Pokemon? ¿Con qué n y con qué semilla? 
# ¿Encontró algún nombre que no tiene sentido? ¿Con qué n y semilla? 
# (Incluya el código de demostración)

#R/ Entre los nombres interesantes o posibles que se generaron estaban:
# Nomperio seed 863 n 2
print("n=1 seed 863:",generate_word(model2,863))
# Slygon seed 878 n 2
print("n=1 seed 878:",generate_word(model2,878))
# Huronda seed 885 n 1
print("n=1 seed 885:",generate_word(model1,885))
# Marelphox seed 893 n 3
print("n=1 seed 893:",generate_word(model3,893))
#Entre los nombres que no tienen sentido estaban:
# Nkiewawiopinittcrnonty seed 841 n 1
print("n=1 seed 841:",generate_word(model1,841))
# Excadabrawdaunchespirizionneking seed 855 n 2
print("n=1 seed 855:",generate_word(model2,855))
# Linachoranggupoweldeockiorsaneligro seed 2869 n 1 
print("n=1 seed 863:",generate_word(model1,2869))

#c Explique en sus propias palabras 
# ¿de qué manera se están usando las cadenas de Markov para modelar los nombres?
#R/ Se está haciendo una cadena de markov en la que cada estado es el n-grama actual, y las probabilidades
# de transición son las frecuencias normalizadas de los ngramas que le siguen a ese. De esta forma,
# las secuencias de caracteres que más pasan en nombres de pokemon tienen mayor probabilidad de suceder
# cuando se hace un recorrido para generar un nombre, y entonces se forman nombres que sí suenan como pokemons.