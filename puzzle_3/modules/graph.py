class Graph:
    def __init__(self, adjacencyList=[], pathMatrix=[], endPoints={}):
        self.adjacencyList = adjacencyList
        self.pathMatrix = pathMatrix
        self.endPoints = endPoints

    def addToGraph(self, neuralStrand):
        xCoord = neuralStrand.getX()
        yCoord = neuralStrand.getY()
        path = neuralStrand.getPath()
        self.__expandPathMatrixToXYPoints(xCoord, yCoord)
        if self.pathMatrix[yCoord][xCoord] == None:
            self.addPointToPathMatrix(xCoord, yCoord)
            self.addPointToAdjacencyList(xCoord, yCoord)
            self.__findPointAdjacencies(xCoord, yCoord)
        directions = {
            'D': self.moveDown,
            'U': self.moveUp,
            'R': self.moveRight,
            'L': self.moveLeft
        }
        for step in path:
            try:
                xCoord, yCoord = directions[step](xCoord, yCoord)
                self.__expandPathMatrixToXYPoints(xCoord, yCoord)
                if self.pathMatrix[yCoord][xCoord] == None:
                    self.addPointToPathMatrix(xCoord, yCoord)
                    self.addPointToAdjacencyList(xCoord, yCoord)
                    self.__findPointAdjacencies(xCoord, yCoord)
            except:
                pass

    def addPointToPathMatrix(self, xCoord, yCoord):
            self.pathMatrix[yCoord][xCoord] = len(self.adjacencyList)

    def addPointToAdjacencyList(self, xCoord, yCoord):
            self.adjacencyList.append([(xCoord, yCoord), []])
    
    def __findPointAdjacencies(self, xCoord, yCoord):
        directions = {
            'D': self.moveDown,
            'U': self.moveUp,
            'R': self.moveRight,
            'L': self.moveLeft
        }
        for direction in directions:
            currentPoint = len(self.adjacencyList) - 1
            xAdjacent, yAdjacent = directions[direction](xCoord, yCoord)
            try:
                if xAdjacent > 0 and yAdjacent > 0:
                    adjacentPoint = self.pathMatrix[yAdjacent][xAdjacent]
                    if adjacentPoint != None:
                        self.__addEdge(currentPoint, adjacentPoint)
            except:
                pass

    def __addEdge(self, currentPoint, adjacentPoint):
        self.adjacencyList[currentPoint][1].append(adjacentPoint)
        self.adjacencyList[adjacentPoint][1].append(currentPoint)

    def __expandPathMatrixToXYPoints(self, xCoord, yCoord):
        while len(self.pathMatrix) <= yCoord:
            self.pathMatrix.append([])
        while len(self.pathMatrix[yCoord]) <= xCoord:
            self.pathMatrix[yCoord].append(None)
    
    @staticmethod
    def moveDown(x, y):
        return x, y + 1
    @staticmethod 
    def moveUp(x, y):
        return x, y - 1
    @staticmethod
    def moveRight(x, y):
        return x + 1, y
    @staticmethod
    def moveLeft(x, y):
        return x - 1, y

if __name__ == '__main__':
    import neuralstrand
    import csv
    f = open("puzzle3.txt", "r")
    strands = []
    for line in f:
        strand = neuralstrand.NeuralStrand(line)
        strands.append(strand)
    graph = Graph()
    for strand in strands:
        graph.addToGraph(strand)

    with open('testFile.csv', mode='w') as testFile:
        fileWriter = csv.writer(testFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        fileWriter.writerows(graph.pathMatrix)