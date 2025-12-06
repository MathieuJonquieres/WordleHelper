from lettersModifier import WORD_SIZE
from app import solution
import json



def start(options : int=1):
    with open('data.json') as json_file:
        dictionnaire = list(json.load(json_file))

    mots = []
    for mot in dictionnaire:
        if(len(mot)==WORD_SIZE):
            mots.append(mot)

    if(options==0):
            """
            possible=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
            """
            possible=[['a','l','t'],
            ['a','w','y'],
            ['a','r'],
            ['i'],
            ['c','f','t']]
            
    else:
        possible=[]
        for indice in range(WORD_SIZE):
            possible.append([])
            for letters in range(26):
                possible[indice].append(chr(ord('a')+letters))
    malPlace={}

    solution(possible, malPlace, mots)

'''
Choisir 0 pour pouvoir choisir les lettres a l'avance depuis l'editeur
    (permet d'avoir un ensemble de lettres déjà prédéfinies)
Risque d'erreur si modification de la taille du mot recherché!

Choisir un autre entier pour commencer avec toutes les lettres
    (plus long car il faut éditer les lettres possibles depuis la console avec l'option 2)
'''
start()