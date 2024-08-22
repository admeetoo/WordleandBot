import random
import time


pink = "\033[35m"
black = "\033[0;30m"
red = "\033[0;41m"
green = "\033[0;42m"
greentext = "\033[0;32m"
yellow = "\033[0;33m"
white = "\033[0;37m"
nocolor = "\033[0m"


def NoColor(word):
    nocolorWord = nocolor+word+nocolor
    return nocolorWord

def chrToNum(char):
    return ord(char) - 97

def numToChar(num):
    return chr(num + 97)

NumOfLettersWord = [0] * 26

NumOfLettersGuess = [0] * 26

def mid(s, offset, amount):
    return s[offset:offset+amount]
def Green(word):
    greenWord = green+word+nocolor
    return greenWord

def GreenText(word):
    greenTextWord = greentext+word+nocolor
    return greenTextWord

def Yellow(word):
    yellowWord = yellow+word+nocolor
    return yellowWord


def Red(word):
    redWord = red+word+nocolor
    return redWord

def Pink(word):
    PinkWord = pink+word+nocolor
    return PinkWord


print(f'''
Welcome to Adam's {Green("W")}{NoColor(" ")}{Green("O")}{NoColor(" ")}{Green("R")}{NoColor(" ")}{Green("D")}{NoColor(" ")}{Green("L")}{NoColor(" ")}{Green("E")}!
Here are the rules:
- A random 5-letter word will be generated.
- You get 5 chances to get this word.
For each guess, a correctly guessed letter will:
- Turn {Green("Green")} if it is part of the word & in the correct position.
- Turn {Red("Orange")} if it is part of the word, but in the incorrect position.

For Example:
If the word is "Catch"
and the word "Crack" is entered,
the code will return: "{Green("C")}r{Red("a")}{Green("c")}k"
Good Luck!
''')


WordNum = int(random.randrange(1, 2316))
GuessWords = open("GuessWords.txt", "r")
for i in range(WordNum):
    GuessWord = GuessWords.readline().strip()
GuessWords.close()


GuessWord = GuessWord.lower()
for i in range(5):
    char = (mid(GuessWord, i, 1))
    Ix = chrToNum(char)
    NumOfLettersWord[Ix] += 1

def Wordle(GuessWord, guess):
    outputword = ""
    GuessWord = GuessWord.lower()
    guess = guess.lower()
    NumOfLettersGuess = [0] * 26
    for h in range(5):
        charg = (mid(guess, h, 1))
        Ixg = chrToNum(charg)
        NumOfLettersGuess[Ixg] += 1
    for i in range(5):
        letterfound = False
        letterguessi = mid(guess, i, 1)
        for x in range(5):
            letterwordx = mid(GuessWord, x, 1)
            if letterguessi == letterwordx and i == x:
                letterguessi = Green(letterguessi)
                outputword = outputword + letterguessi
                letterfound = True
                break
            elif letterguessi == letterwordx:
                if letterguessi == mid(GuessWord, i, 1):
                    letterguessi = Green(letterguessi)
                    outputword = outputword + letterguessi
                    letterfound = True
                    break
                letterguessi = Red(letterguessi)
                outputword = outputword + letterguessi
                letterfound = True
                break
        if letterfound == False:
            outputword = outputword + letterguessi
    for f in range(5):
        tempo = mid(guess, f, 1)
        if NumOfLettersGuess[chrToNum(tempo)] > NumOfLettersWord[chrToNum(tempo)]:
            outputword = outputword.replace(red + tempo, NoColor(tempo), 1)
            NumOfLettersGuess[chrToNum(tempo)] = NumOfLettersGuess[chrToNum(tempo)] - 1
    return outputword



Guesses = 5
GuessesTaken = 0
errorprompt = f"Invalid word entered. Please try again: "

WordFound = False
isWord = False
while Guesses > 0 and WordFound == False:
    guess = input(f"{Guesses} guesses remaining, please enter another word: ").lower()
    FillerWords = open("FillerandGuess.txt", "r")
    for x in range(12972):
        temp = FillerWords.readline().strip()
        if guess == temp:
            isWord = True
    FillerWords.close()
    while isWord == False:
        guess = input(errorprompt).lower()
        FillerWords = open("FillerandGuess.txt", "r")
        for x in range(12972):
            temp = FillerWords.readline().strip()
            if guess == temp:
                isWord = True
        FillerWords.close()
    if isWord == True:

        print(Wordle(GuessWord, guess))
        GuessesTaken += 1
        if guess == GuessWord:
            print(f'''Congrats, you guessed the word "{GreenText(GuessWord)}" correctly! It took you {GuessesTaken} guesses.''')
            time.sleep(10)
            WordFound = True
        Guesses = Guesses - 1
        isWord = False
if WordFound == False:
    print(f'''Unfortunately, you weren't able to guess the word, "{Pink(GuessWord)}", better luck next time.''')
    time.sleep(10)

