import os
pathname = os.path.dirname(os.path.abspath(__file__))

def getbytes(bits):
    done = False
    while not done:
        byte = 0
        for _ in range(0, 8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True
            byte = (byte << 1) | bit
        if done == False:
            yield byte


def parseLineToBitArray(line):
    bitArray = [int(el) for el in line.strip()]
    return bitArray

def getByteArray(bitArray):
    return [byte for byte in getbytes(iter(bitArray))]

def isByteValid(byte, array):
    return byte < len(array)

def followUntilInvalid(byte, byteArray):
    # print('following: ', byte)
    if isByteValid(byte, byteArray):
        newByte = byteArray[byte]
        return followUntilInvalid(newByte, byteArray)
    else:
        return byte

def getCharInLine(byteArray):
    for byte in byteArray:
        if isByteValid(byte, byteArray):
            # print('valid byte: ', byte)
            return(followUntilInvalid(byte, byteArray))

def findPassword(file):
    password = ''
    for line in file:
        bitArray = parseLineToBitArray(line)
        byteArray = getByteArray(bitArray)
        char = getCharInLine(byteArray)
        password = password + chr(char)
    return password

if __name__ == '__main__':
    with open('puzzle1.txt', 'r') as inputFile:
        password = findPassword(inputFile)
        print('Password is: ' + password)

        with open(pathname + '/solution.txt', mode='w') as solution:
            solution.write(password + '\n')