from lettersModifier import WORD_SIZE
from app import solution
import json



def start(option: int=1):
    with open('data.json') as json_file:
        dictionnary = list(json.load(json_file))

    wordsList = []
    for word in dictionnary:
        if(len(word)==WORD_SIZE):
            wordsList.append(word)

    if(option==0):
            """
            possibility=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
            """
            possibility=[['a','l','t'],
            ['a','w','y'],
            ['a','r'],
            ['i'],
            ['c','f','t']]
            
    else:
        possibility=[]
        for index in range(WORD_SIZE):
            possibility.append([])
            for letters in range(26):
                possibility[index].append(chr(ord('a')+letters))
    solution(possibility, wordsList)

'''
Enter start(0) to customize the letters choice directly from the script
Enter start() to customize the letters choice from the terminal
'''
start()