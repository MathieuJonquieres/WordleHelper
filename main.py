from resolver import resoudre
from resolver import WORD_SIZE
from time import sleep
import json

def retirerLettre(possible : list, pos:int, lettre :str):
    possible[pos].remove(lettre)

def solution(possible,mots):
    while True:
        entree = int(input("Entrez la fonction a utiliser :\n" \
        "                       0 : voir les lettres possibles\n" \
        "                       1 : afficher toutes les possibilités\n" \
        "                       2 : retirer les possibilites\n"
        "                       3 : quitter\n"
        "Choix : "))

        match entree:
            case 0 :
                print("Lettres possibles et fixe (0 = n'importe quel lettres non mal placées ou impossible) : ", possible)
            case 1:
                mots = resoudre(mots, possible)
                print(mots)
            case 2 :
                lettre = input("Lettre a retirer : ")
                pos = int(input("Entrez la position de la lettre à retirer (0=all) : "))
                retirerLettre(possible,pos,lettre)
            case 3:
                exit(0)
        sleep(1)

def start(options : int):
    with open('data.json') as json_file:
        dictionnaire = list(json.load(json_file))

    mots = []
    for mot in dictionnaire:
        if(len(mot)==WORD_SIZE):
            mots.append(mot)

    match options:
        case 0:
            """
            possible=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
            """
            possible=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
        case 1:
            for indice in range(5):
                for letters in range(26):
                    possible.append(chr(ord('a')+letters))

    solution(possible,mots)

'''
Choisir 0 pour pouvoir choisir les lettres a l'avance depuis l'editeur (permet d'avoir un ensemble de lettres déjà prédéfinies)
Choisir 1 pour commencer avec toutes les lettres (plus long car il faut éditer depuis la console avec l'option 2)
'''
start(0)