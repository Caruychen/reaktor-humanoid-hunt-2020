class NeuralStrand:
    def __init__(self, inputLine=''):
        self.setStrand(inputLine)

    def setStrand(self, inputLine):
        splitLine = inputLine.strip().split(' ')
        self.__setStart(splitLine)
        self.__setPath(splitLine)

    def __setStart(self, splitLine):
        self.start = [int(coordinate) for coordinate in splitLine[0].split(',')]
    
    def __setPath(self, splitLine):
        try:
            self.path = splitLine[1].split(',')
        except:
            self.path = ''
    
    def getStart(self):
        return self.start
    
    def getPath(self):
        return self.path

    def getX(self):
        return self.start[0]
    
    def getY(self):
        return self.start[1]

if __name__ == '__main__':
    f = open("puzzle3.txt", "r")
    strands = []
    for line in f:
        strand = NeuralStrand(line)
        strands.append(strand)
    print(strands[0].getStart())
    print(strands[0].getPath())
    print(strands[0].getX(), strands[0].getY())
    