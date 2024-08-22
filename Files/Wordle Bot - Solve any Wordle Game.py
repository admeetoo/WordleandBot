import time

wordfound = False
greentext = "\033[0;32m"
nocolor = "\033[0m"
greytext = "\033[0;37m"
redtext = "\033[0;31m"
yellow = "\033[0;33m"
pink = "\033[35m"

def Yellow(word):
    yellowWord = yellow+word+nocolor
    return yellowWord

def Pink(word):
    PinkWord = pink+word+nocolor
    return PinkWord

def RedText(word):
    redTextWord = redtext+word+nocolor
    return redTextWord

def GreenText(word):
    greenTextWord = greentext+word+nocolor
    return greenTextWord

def GreyText(word):
    greyTextWord = greytext+word+nocolor
    return greyTextWord

LettersFound = [False] * 26
clicker = False
def mid(s, offset, amount):
    return s[offset:offset+amount]

def chrToNum(char):
    return ord(char) - 97

def numToChar(num):
    return chr(num + 97)

arr = []
percentarray = [8.46, 2.43, 4.12, 3.4, 10.65, 1.99, 2.69, 3.36, 5.8, 0.23, 1.81, 6.21, 2.73, 4.97, 6.51, 3.17, 0.25, 7.77, 5.78, 6.3, 4.03, 1.32, 1.68, 0.32, 3.67, 0.35]
wordtotal = 0
word = ""
arrfsorting = [0] * 26
charg = ""
power = float(1)
# Give each word score, and add to 2d array

# GuessWordsFile = open("FillerandGuess.txt", "r")
# for i in range(12972):
#     word = GuessWordsFile.readline().strip()
#     for x in range(5):
#         charg = (mid(word, x, 1))
#         Ixm = chrToNum(charg)
#         arrfsorting[Ixm] += 1
#         if arrfsorting[chrToNum(mid(word, x, 1))] == 0:
#             wordtotal += percentarray[chrToNum(mid(word, x, 1))]
#         else:
#             power = arrfsorting[chrToNum(mid(word, x, 1))]
#             # ensure repeated letters are given less score.
#             wordtotal += (percentarray[chrToNum(mid(word, x, 1))]) * (float(0.35) ** float(power))
#     power = 1
#     arrfsorting = [0] * 26
#     arr.append([word, wordtotal])
#     wordtotal = 0
#     word = ""

sortedarray = []
largest = 0
# Sort Entire Array, copy to text file (save processing)
#
# for x in range(12972):
#     for i in range(12972):
#         if arr[i][1] > largest and arr[i][1] > 0:
#             largest = arr[i][1]
#             place = i
#     if arr[place][1] > 0:
#         sortedarray.append(arr[place][0])
#         arr[place][1] = 0
#         largest = 0
#         place = 0
# sortedfile = open("sortedarray.txt", "w")
# for i in range(len(sortedarray)):
#     sortedfile.write(sortedarray[i]+"\n")

sortedfile = open("sortedarray.txt", "r")
for i in range(12972):
    sortedarray.append(sortedfile.readline().strip())

greenlist = []
def green(char, ix):
    greenlist.append(ix)
    popped1 = True
    while popped1 == True:
        for i in range(len(sortedarray)):
            if mid(sortedarray[i], ix, 1) != char and len(sortedarray) > 0:
                sortedarray.pop(i)
                popped1 = True
                break
            popped1 = False
    popped1 = False
    if len(sortedarray) == 1:
        clicker = True
        wordfound = True
def orange(char, ix):
    for i in range(len(sortedarray)-1, -1, -1):
        if mid(sortedarray[i], ix, 1) == char and len(sortedarray) > 0:
            sortedarray.pop(i)
    for i in range(len(sortedarray)-1, -1, -1):   #remove word if it doesn't contain the letter
        flagcontains = False
        for y in range(5):
            if y not in greenlist:
                if mid(sortedarray[i], y, 1) == char:
                    flagcontains = True
                    break
        if flagcontains == False and len(sortedarray) > 0:
            sortedarray.pop(i)
    if len(sortedarray) == 1:
        clicker = True
        wordfound = True

def grey(char, ix):
    try:
        if LettersFound[chrToNum(char)] == False:
            for i in range(len(sortedarray)-1, -1, -1):
                for y in range(5):
                    if mid(sortedarray[i], y, 1) == char and len(sortedarray) > 0:
                        sortedarray.pop(i)
        elif LettersFound[chrToNum(char)] == True:
            popped2 = True
            while popped2 == True:
                for i in range(len(sortedarray)):  # remove the word if it contains the letter in that spot
                    if mid(sortedarray[i], ix, 1) == char and len(sortedarray) > 0:
                        sortedarray.pop(i)
                        popped2 = True
                        break
                    popped2 = False
        if len(sortedarray) == 1:
            clicker = True
            wordfound = True
    except:
        print("small error grey")

greylist = []
orangelist = []

yourword = "slate"
Ixg = 0
for h in range(5):
    charg = (mid(yourword, h, 1))
    Ixg = chrToNum(charg)
    LettersFound[Ixg] = True

Guesses = 0
print(f'''
Welcome to Adam's wordle bot!

Here is a quick rundown:-
- You will enter your word, and will be prompted to enter the color returned by each letter in the word, in order.
- You will enter the colors: "{GreenText("Green")}", "{RedText("Orange")}", or "{GreyText("Grey")}". 
- (You may also use ({GreenText("1")}, {RedText("2")}, or {GreyText("3")}) 
or "({GreenText("V")}", "{GreenText("O")}", "{GreyText("G")})", respectively.)

- The code will then return the next most suitable word(s).
Generally, the best first guess is "Slate".\n''')
while wordfound == False and Guesses < 5:
    time.sleep(1.5)
    correctword = input("Was the word correct? ").lower()
    if correctword == "yes" or correctword == "y":
        wordfound = True
    if len(sortedarray) == 1 or wordfound == True:
        if Guesses != 0:
            print(f'''Congrats, you found the word, "{GreenText(sortedarray[0].capitalize())}", in {Guesses + 1} guesses.''')
        elif Guesses == 0:
            print(f'''Congrats, you found the word, "Slate", in 1 guess.''')
        time.sleep(10)
        wordfound = True
        break
    LettersFound = [False] * 26
    yourword = input(f'''Input word #{Guesses + 1}: ''')
    if yourword == sortedarray[0]:
        sortedarray.pop(0)
    for i in range(5):
        if clicker == True:
            clicker = False
            break
        color = input(f'''Color #{i+1}: ''')
        color = color.lower()
        if color == "green" or color == "1" or color == "v":
            green(mid(yourword, i, 1), i)
            Ixg = chrToNum(mid(yourword, i, 1))
            LettersFound[Ixg] = True
        elif color == "orange" or color == "2" or color == "o":
            orangelist.append(i)
            Ixg = chrToNum(mid(yourword, i, 1))
            LettersFound[Ixg] = True
        elif color == "grey" or color == "3" or color == "g":
            greylist.append(i)
    for i in range(len(orangelist)):
        orange(mid(yourword, orangelist[i], 1), orangelist[i])
    for i in range(len(greylist)):
        grey(mid(yourword, greylist[i], 1), greylist[i])
    orangelist = []
    greenlist = []
    greylist = []
    print(f"\nThere are {len(sortedarray)} possible words remaining.")
    if len(sortedarray) < 2:
        print(f'''The only possible guess remaining is: "{Pink(sortedarray[0])}".''')
    else:
        print(f'''In order, the most suitable guesses are: "{sortedarray[0]}", and "{sortedarray[1]}".''')
    Guesses += 1



if wordfound == False:
    print(f'''
Unfortunately, the bot wasn't able to guess the word
however, we think it was one of the following words: ''')
    for i in range(len(sortedarray)):
        print(sortedarray[i].capitalize())