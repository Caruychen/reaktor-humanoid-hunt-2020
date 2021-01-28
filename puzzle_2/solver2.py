import os
pathname = os.path.dirname(os.path.abspath(__file__))

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
    charFrequencies = getCharFrequencies(signal)
    subCharDict = getSubsequentCharsDict(signal)
    currentChar = getMostFrequentChar(charFrequencies)
    password = currentChar
    while currentChar != ";":
        currentChar = getMostFrequentChar(subCharDict[currentChar])
        password += currentChar
    return password

if __name__ == '__main__':
    with open(pathname + '/puzzle2.txt', 'r') as inputFile:
        signal = inputFile.read()
        answer = findBaseValue(signal)
        print('Password is: ' + answer)

        with open(pathname + '/solution.txt', mode='w') as solution:
            solution.write(answer + '\n')
