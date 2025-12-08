from resolver import resolve
from resolver import uniqueWords
from lettersModifier import *

def solution(possibility, wordsList):
    letterUsed = set()
    incorrect = {}
    while True:
        choixFonction=-1
        while choixFonction<0 or choixFonction>4:
            choixFonction = int(input("Select a function :\n" \
            "                       0 : See letters list\n" \
            "                       1 : See possible words\n" \
            "                       2 : See "+str(WORD_SIZE)+" letter unique word\n" \
            "                       3 : Edit letters list\n" \
            "                       4 : Quit\n" \
            "Enter your choice : "))

        match choixFonction:
            case 0 :
                for indice in range(WORD_SIZE):
                    print("Letter n°",indice+1,":",possibility[indice])
                for letter in incorrect:
                    print("Allowed position for the letter :",letter,":",incorrect[letter])
            case 1:
                wordsList = resolve(wordsList, possibility, incorrect)
                print(wordsList)

            case 2:
                print(uniqueWords(wordsList,possibility,incorrect))

            case 3 :
                choixChangement=-1
                while(choixChangement<0 or choixChangement>3):
                    choixChangement = int(input("EDIT : Select a modification :\n" \
                    "                       0 : Add a letter at a position\n" \
                    "                       1 : Delete a letter from all lists\n" \
                    "                       2 : Add a wrong position for a letter\n"
                    "                       3 : Enter a fixed letter at a position\n"
                    "Enter your choice : "))
                match choixChangement:
                    case 0:
                        letter = letterInput("Adding letter : ")
                        pos = posInput("Select the position (0=all) : ",0)
                        addLetter(possibility,letter,pos)

                    case 1:
                        letter = letterInput("Deleting letter : ")
                        delLetter(possibility,letter)
                        letterUsed.add(letter)
                        print(letterUsed)

                    case 2:
                        letter = letterInput("Wrong placed letter : ")
                        pos = posInput("Select the position : ",1)
                        addIncorrect(possibility, incorrect, letterUsed, letter, pos)
                        letterUsed.add(letter)
                        print(letterUsed)        

                    case 3:
                        letter = letterInput("Fixed letter : ")
                        pos = posInput("Select the position : ",1)
                        possibility[pos-1]=[lowercaseConverter(letter)]
                        letterUsed.add(letter)
                        print(letterUsed)
                        
            case 4:
                exit(0)

