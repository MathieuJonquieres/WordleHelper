WORD_SIZE = 5

def addLetter(possibility : list, letter :str, pos:int):
    '''
    Add the [letter] into [possibility] at the [pos] position
    If the [pos] add the letter into all [possibility] list
    '''
    letter = lowercaseConverter(letter)
    match pos:
        case 0:
            for index in range(WORD_SIZE):
                if letter not in possibility[index]:
                    possibility[index].append(letter)
                    possibility[index].sort()
        case others:
            if letter not in possibility[pos-1]:
                possibility[pos-1].append(letter)
                possibility[pos-1].sort()

def delLetter(possibility : list, letter :str):
    '''
    Delete the [letter] from all [possibility] list
    '''
    for index in range(WORD_SIZE):
        if letter in possibility[index]:
            possibility[index].remove(letter)

def addIncorrect(possibility, incorrect, letterUsed, letter, pos):
    if (letter not in incorrect) and (letter in possibility[pos-1]):
        incorrect[letter]=[]
        for i in range(WORD_SIZE):
            incorrect[letter]+=[i+1]
    if letter in incorrect:
        if pos in incorrect[letter]:
            incorrect[letter].remove(pos)
            possibility[pos-1].remove(letter)
    letterUsed.add(letter)
         

def letterInput(text:str):
    letter = input(text)
    while(len(letter)!=1 
            & (ord('a')<=ord(letter[0])<=ord('z')
            or ord('A')<=ord(letter[0])<=ord('Z'))):
                letter = input(text)
    letter = lowercaseConverter(letter)
    return letter

def posInput(text, minPos:int):
    pos = -1
    while pos>WORD_SIZE or pos<minPos:
        pos = int(input(text))
    return pos

def lowercaseConverter(letter:str):
    if(ord('A')<=ord(letter[0])<=ord('Z')):
        letter = str(chr(ord(letter[0])-(ord('A')-ord('a'))))
    return letter