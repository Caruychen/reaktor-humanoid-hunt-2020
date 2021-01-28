f = open("puzzle2.txt", "r")
signal = f.read()

def getCharFrequencies(signal):
    charCount = {}
    for char in signal:
        if char in charCount:
            newValue = charCount[char] + 1
            charCount.update({char: newValue})
        else:
            charCount[char] = 1
    return charCount

def getMostFrequentChar(frequencyDict):
    maxValue = max(frequencyDict.values())
    maxKeys = [k for k, v in frequencyDict.items() if v == maxValue]
    return maxKeys[0]

def getSubsequentCharsDict(signal):
    subCharsLists = {}
    previousChar = None
    for currentChar in signal:
        if currentChar not in subCharsLists:
            subCharsLists[currentChar] = {}
        if previousChar != None:
            if currentChar in subCharsLists[previousChar]:
                newValue = subCharsLists[previousChar][currentChar] + 1
                subCharsLists[previousChar].update({currentChar: newValue})
            else:
                subCharsLists[previousChar][currentChar] = 1
        previousChar = currentChar
    return subCharsLists

def findBaseValue(signal):
    totalFrequency = getCharFrequencies(signal)
    subCharDict = getSubsequentCharsDict(signal)
    currentChar = getMostFrequentChar(totalFrequency)
    password = currentChar
    while currentChar != ";":
        currentChar = getMostFrequentChar(subCharDict[currentChar])
        password += currentChar
    return password

print(findBaseValue(signal))

f.close()