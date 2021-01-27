class NeuralStrand:
    def __init__(self, inputLine=''):
        try:
            self.setStrand(inputLine)
        except:
            self.start = None
            self.path = None

    def setStrand(self, inputLine):
        splitLine = inputLine.strip().split(' ')
        self.setStart(splitLine)
        self.setPath(splitLine)

    def setStart(self, splitLine):
        self.start = [int(coordinate) for coordinate in splitLine[0].split(',')]
    
    def setPath(self, splitLine):
        try:
            self.path = splitLine[1].split(',')
        except:
            self.path = ''

if __name__ == '__main__':
    f = open("puzzle3.txt", "r")
    strands = []
    for line in f:
        strand = NeuralStrand()
        strand.setStrand(line)
        strands.append(strand)
    print(strands[0].start)
    print(strands[0].path)
    