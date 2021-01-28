class NeuralStrand:
    ''' Splits the starting point and path of the neural strand, and converts them to arrays '''

    def __init__(self, inputLine):
        self.setStrand(inputLine)

    def setStrand(self, inputLine):
        if len(inputLine) == 0:
            raise Exception("Input line is empty!")

        splitLine = inputLine.strip().split(' ')
        self.__setStart(splitLine)
        self.__setPath(splitLine)

    def __setStart(self, splitLine):
        coordinates = splitLine[0].split(',')
        if len(coordinates) < 2:
            raise Exception("Coordinates incomplete!")

        self.start = [int(coordinate) for coordinate in coordinates]
    
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
    testInput = [
        '20,60 U,U,L,U,R,R,U,R,D,D,R,D,L,D,R,R,R,R,U,R,R,R,R,R,R,R,D',
        '104,15'
    ]

    def parse(input):
        strands = []
        for line in input:
            strand = NeuralStrand(line)
            strands.append(strand)
        return strands

    strands = parse(testInput)
    assert(strands[0].getStart() == [20,60])
    assert(strands[0].getPath() == ['U','U','L','U','R','R','U','R','D','D','R','D','L','D'
                                    ,'R','R','R','R','U','R','R','R','R','R','R','R','D'])
    assert(strands[1].getStart() == [104,15])
    assert(strands[1].getPath() == '')
    