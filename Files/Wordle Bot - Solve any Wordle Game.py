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
word2 = ""
arrfsorting = [0] * 26
charg = ""
power = float(1)
arrGuessListSmall = []
arr2 = []  #2d array holding all scores for filler words.
arrayfillerrewards = [0.0] * 26
arrayfillerlettercounts = [0] * 26
letterinword = [False] * 26




# Give each word score, and add to 2d array
# TOGGLE START

# SmallWordsFile = open("GuessWords.txt", "r")
# for i in range(2316):
#     word2 = SmallWordsFile.readline().strip()
#     arrGuessListSmall.append(word2)
#
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
#     for y in range(len(arrGuessListSmall)):
#         if word == arrGuessListSmall[y]:
#             # Give larger reward if the word is in the smaller word list, as it is more likely to be the word.
#             # Toggle this line if you want to turn this functionality off.
#             wordtotal += 1
#     power = 1
#     arrfsorting = [0] * 26
#     arr.append([word, wordtotal])
#     wordtotal = 0
#     word = ""

# TOGGLE END


sortedarray = []
largest = 0
outputfiller2 = ""


# Sort Entire Array, copy to text file (save processing)
# TOGGLE START

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
# sortedfile.close()

# TOGGLE END

sortedarrayfillers = []
sortedfile = open("sortedarray.txt", "r")
for i in range(12972):
    sortedarray.append(sortedfile.readline().strip())
sortedfile.close()

sortedfile = open("sortedarray.txt", "r")
for i in range(12972):
    sortedarrayfillers.append(sortedfile.readline().strip())
sortedfile.close()
temporary1 = ""
temporary2 = ""
temporary3 = ""


def maximum():
    global sortedarray
    if len(sortedarray) < 8:
        return len(sortedarray)
    else:
        return 8


guesswordslist = []
countersetletters = 0 #Amount of letters found in every one of the remaining words.
def dynamic_percent_array():
    global sortedarrayfillers, letterinword, sortedarray, arrayfillerrewards, arrayfillerlettercounts, countersetletters, outputfiller2, temporary1, temporary2, temporary3
    countersetletters = 0
    wordtotalin = 0
    sto = ""
    internalflaglettercorrectplace = True
    arraysortedfillersresetable = []
    arrayfillerrewards = [0.0] * 26
    arrayofsorting = [0] * 26
    arrayfillerlettercounts = [0] * 26
    for i in range(len(sortedarray)):
        letterinword = [False] * 26
        for x in range(5):
            if letterinword[chrToNum(mid(sortedarray[i], x, 1))] == False:
                letterinword[chrToNum(mid(sortedarray[i], x, 1))] = True
                arrayfillerlettercounts[chrToNum(mid(sortedarray[i], x, 1))] += 1
    for i in range(26):
        arrayfillerrewards[i] = arrayfillerlettercounts[i]/len(sortedarray)
        if arrayfillerrewards[i] == 1.0:
            for m in range(5):
                sto = mid(sortedarray[0], m, 1)
                for h in range(maximum()):
                    if mid(sortedarray[h], m, 1) != sto:
                        internalflaglettercorrectplace = False
                if internalflaglettercorrectplace == True:
                    countersetletters += 1
        if arrayfillerrewards[i] == 0.0:
            arrayfillerrewards[i] = 1.5
    for i in range(len(sortedarrayfillers)):
        arrayofsorting = [0] * 26
        wordtotalin = 0
        for x in range(5):
            if arrayofsorting[chrToNum(mid(sortedarrayfillers[i], x, 1))] == 0:
                wordtotalin += arrayfillerrewards[chrToNum(mid(sortedarrayfillers[i], x, 1))]
            else:
                wordtotalin += 30
            arrayofsorting[chrToNum(mid(sortedarrayfillers[i], x, 1))] += 1
        arraysortedfillersresetable.append([wordtotalin, sortedarrayfillers[i]])
    arraysortedfillersresetable.sort()
    temporary1 = arraysortedfillersresetable[0][1]
    temporary2 = arraysortedfillersresetable[1][1]
    temporary3 = arraysortedfillersresetable[2][1]






guesswords = open("GuessWords.txt", "r")
for i in range(2316):
    guesswordslist.append(guesswords.readline().strip())
guesswords.close()


greenlist = []
def green(char, ix):
    if len(sortedarray) != 0:
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
    else:
        print("There are no more possible guesses. This either means you have made some incorrect inputs, or the word you are looking for is not in my list.")



def orange(char, ix):
    if len(sortedarray) != 0:
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
    else:
        print("There are no more possible guesses. This either means you have made some incorrect inputs, or the word you are looking for is not in my list.")



def grey(char, ix):
    if len(sortedarray) != 0:
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
    else:
        print("There are no more possible guesses. This either means you have made some incorrect inputs, or the word you are looking for is not in my list.")


lilflag = False
templist = [""] * 4
greencount = 0
fillertrials = 0
greylist = []
orangelist = []
color = ""
correctword = ""
yourword = "slate"
Ixg = 0
for h in range(5):
    charg = (mid(yourword, h, 1))
    Ixg = chrToNum(charg)
    LettersFound[Ixg] = True
yourword = ""
Guesses = 0
wordsbefore = 0
wordsafter = 0
percentremoved = 0.0
print(f'''
Welcome to Adam's wordle bot!

Here is a quick rundown:-
- You will enter your word, and will be prompted to enter the color returned by each letter in the word, in order.
- You will enter the colors: "{GreyText("Grey")}", "{RedText("Orange")}", or "{GreenText("Green")}". 
- (You may also use ({GreyText("1")}, {RedText("2")}, or {GreenText("3")}) or ("{GreyText("G")}", "{RedText("O")}", "{GreenText("V")}"), respectively.)

- There are {len(sortedarray)} possible words to be found.
- The code will then return the next most suitable word(s).
- Words highlighted in {Yellow("yellow")} are common words.
''')

playagain = ""
playagain2 = True
toggle = False
endgame = False
flagfiller = False
# START OF MAIN CODE

while endgame == False:
    print('''Generally, the best first guess is "Slate".''')

    while wordfound == False and Guesses < 6:
        while len(yourword) != 5:
            yourword = input(f'''\nInput word #{Guesses + 1}: ''').lower().strip()
            if len(yourword) != 5:
                print("Incorrect Input, please make sure to input a 5 letter word.")
            elif len(yourword) == 5:
                break
        while correctword != "yes" and correctword != "no" and correctword != "y" and correctword != "n":
            if (yourword == temporary1 or yourword == temporary2 or yourword == temporary3) and flagfiller == True:
                print(f'''You've used the filler word "{yourword.title()}", please enter the colors that were returned:''')
                flagfiller = False
                break
            flagfiller = False
            correctword = input(f'''Was the word "{yourword}" correct? ''').lower().strip()
            if correctword != "yes" and correctword != "no" and correctword != "y" and correctword != "n":
                print("Incorrect Input, please give a yes or no answer.")
            else:
                break
        if correctword == "yes" or correctword == "y":
            wordfound = True
        if len(sortedarray) == 1 or wordfound == True:
            print(f'''Congrats, you found the word, "{GreenText(yourword.capitalize())}", in {Guesses + 1} guesses.''')
            wordfound = True
            break
        LettersFound = [False] * 26
        for i in range(len(sortedarray)):
            if yourword == sortedarray[i]:
                sortedarray.pop(i)
                break
        wordsbefore = len(sortedarray)
        for i in range(5):
            if clicker == True:
                clicker = False
                break
            while color != "green" and color != "v" and color != "1" and color != "orange" and color != "2" and color != "o" and color != "grey" and color != "3" and color != "g":
                if Guesses == 5:
                    print("Unfortunately, the bot wasn't able to guess your word, however, you can still input the colors returned one last time so we can narrow down the final remaining posibilities.")
                else:
                    if i == 0 and lilflag == False and (yourword != temporary1 and yourword != temporary2 and yourword != temporary3):
                        print("Please input the colors returned:")
                        lilflag = True
                color = input(f'''Color #{i+1}: ''').lower()
                if color != "green" and color != "v" and color != "1" and color != "orange" and color != "2" and color != "o" and color != "grey" and color != "3" and color != "g":
                    print("Incorrect Input, please input one of the three viable colors, Green, Orange, or Grey (Or their corresponding codes).")
                else:
                    break
            if color == "green" or color == "3" or color == "v":
                if len(sortedarray) != 0:
                    green(mid(yourword, i, 1), i)
                    Ixg = chrToNum(mid(yourword, i, 1))
                    LettersFound[Ixg] = True
                    greencount += 1
                else:
                    print("I am here green")
                    break
            elif color == "orange" or color == "2" or color == "o":
                orangelist.append(i)
                Ixg = chrToNum(mid(yourword, i, 1))
                LettersFound[Ixg] = True
            elif color == "grey" or color == "1" or color == "g":
                greylist.append(i)
            color = ""
        for i in range(len(orangelist)):
            if len(sortedarray) != 0:
                orange(mid(yourword, orangelist[i], 1), orangelist[i])
        for i in range(len(greylist)):
            if len(sortedarray) != 0:
                grey(mid(yourword, greylist[i], 1), greylist[i])
        wordsafter = len(sortedarray)
        percentremoved = ((wordsbefore - wordsafter) / wordsbefore)
        orangelist = []
        greenlist = []
        greylist = []
        print(f"\nThere are {len(sortedarray)} possible words remaining.")
        if len(sortedarray) == 0:
            print("There are no more possible guesses. This either means you have made some incorrect inputs, or the word you are looking for is not in my list.")
            wordfound = True
            break
        elif len(sortedarray) == 1:
            print(f'''The only possible guess remaining is: "{Pink(sortedarray[0])}".''')
        else:
            if len(sortedarray) == 2:
                for i in range(2):
                    for y in range(len(guesswordslist)):
                        if sortedarray[i] == guesswordslist[y]:
                            templist[i] = Yellow(sortedarray[i])
                            break
                        templist[i] = sortedarray[i]
            elif len(sortedarray) == 3:
                for i in range(3):
                    for y in range(len(guesswordslist)):
                        if sortedarray[i] == guesswordslist[y]:
                            templist[i] = Yellow(sortedarray[i])
                            break
                        templist[i] = sortedarray[i]
            elif len(sortedarray) >= 4:
                for i in range(4):
                    for y in range(len(guesswordslist)):
                        if sortedarray[i] == guesswordslist[y]:
                            templist[i] = Yellow(sortedarray[i])
                            break
                        templist[i] = sortedarray[i]
            dynamic_percent_array()
            if (countersetletters > 2 and len(sortedarray) > 2) or (greencount > 2 or (float(percentremoved) < 0.50 and len(sortedarray) > 5)) and fillertrials < 2 and len(sortedarray) > 2 and Guesses < 4 and Guesses > 0:
                fillertrials += 1
                if len(sortedarray) == 2:
                    print(f'''In order, the most suitable guesses are: "{templist[0]}", and "{templist[1]}".''')
                elif len(sortedarray) == 3:
                    print(f'''In order, the most suitable guesses are: "{templist[0]}", "{templist[1]}", and "{templist[2]}".''')
                elif len(sortedarray) >= 4:
                    print(f'''In order, the most suitable guesses are: "{templist[0]}", "{templist[1]}", "{templist[2]}", and "{templist[3]}".''')
                flagfiller = True
                print(f'''However, I suggest you use a filler word here to narrow down the possibilities.\nHere are the 3 most suitable filler words: "{temporary1.title()}", "{temporary2.title()}", & "{temporary3.title()}".''')
            else:
                if len(sortedarray) == 2:
                    print(f'''In order, the most suitable guesses are: "{templist[0]}", and "{templist[1]}".''')
                elif len(sortedarray) == 3:
                    print(f'''In order, the most suitable guesses are: "{templist[0]}", "{templist[1]}", and "{templist[2]}".''')
                elif len(sortedarray) >= 4:
                    print(f'''In order, the most suitable guesses are: "{templist[0]}", "{templist[1]}", "{templist[2]}", and "{templist[3]}".''')
            templist = [""] * 4

        Guesses += 1
        yourword = ""
        color = ""
        correctword = ""
        greencount = 0
        lilflag = False



    if wordfound == False:
        print(f'''
Unfortunately, the bot wasn't able to guess the word
however, we think it was one of the following words: ''')
        for i in range(len(sortedarray)):
            print(sortedarray[i].capitalize())

    while playagain != "yes" and playagain != "no" and playagain != "n" and playagain != "y":
        if toggle == True:
            print("Incorrect input, please enter yes or no.")
        playagain = input("\nDo you want to figure out another word?\n").lower()
        if playagain == "yes" or playagain == "y":
            playagain2 = True
            print("\nAlright,")
            toggle = False
            Guesses = 0
            sortedarray = []
            sortedarrayfillers = []
            sortedfile = open("sortedarray.txt", "r")
            for i in range(12972):
                sortedarray.append(sortedfile.readline().strip())
            sortedfile.close()

            sortedfile = open("sortedarray.txt", "r")
            for i in range(12972):
                sortedarrayfillers.append(sortedfile.readline().strip())
            sortedfile.close()

            guesswordslist = []

            guesswords = open("GuessWords.txt", "r")
            for i in range(2316):
                guesswordslist.append(guesswords.readline().strip())
            guesswords.close()
            greenlist = []
            templist = [""] * 4
            greencount = 0
            fillertrials = 0
            greylist = []
            orangelist = []
            color = ""
            correctword = ""
            wordfound = False
            yourword = ""
            playagain = ""
            break
        elif playagain == "no" or playagain == "n":
            playagain2 = False
            toggle = False
            break
        else:
            toggle = True

    if playagain2 == False:
        break

print("\nOkay,\nThanks for using Adam's Wordle Bot!")
time.sleep(10)


