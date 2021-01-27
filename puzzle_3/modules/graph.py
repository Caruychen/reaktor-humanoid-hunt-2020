class Graph:
    def __init__(self, adjacencyList=[], pathMatrix=[], endPoints={}):
        self.adjacencyList = adjacencyList
        self.pathMatrix = pathMatrix
        self.endPoints = endPoints

    def setGraph(self, neuralStrand):
        xCoord = neuralStrand.getX()
        yCoord = neuralStrand.getY()
        path = neuralStrand.getPath()
        self.addPointToGraph(xCoord, yCoord)
        self.addPathToGraph(path, xCoord, yCoord)
    
    def addPointToGraph(self, xCoord, yCoord):
        self.__expandPathMatrixToXYPoints(xCoord, yCoord)
        if self.pathMatrix[yCoord][xCoord] == None:
            self.__addPointToPathMatrix(xCoord, yCoord)
            self.__addPointToAdjacencyList(xCoord, yCoord)
            self.__findPointAdjacencies(xCoord, yCoord)
    
    def addPathToGraph(self, path, xCoord, yCoord):
        for step in path:
            try:
                xCoord, yCoord = self.__parseDirections(step, xCoord, yCoord)
                self.addPointToGraph(xCoord, yCoord)
            except:
                self.__addToEndPoints(step, xCoord, yCoord)
    
    def __addToEndPoints(self, step, xCoord, yCoord):
        if step not in self.endPoints:
            self.endPoints[step] = [self.pathMatrix[yCoord][xCoord]]
        else:
            if self.pathMatrix[yCoord][xCoord] not in self.endPoints[step]:
                self.endPoints[step].append(self.pathMatrix[yCoord][xCoord])

    def __addPointToPathMatrix(self, xCoord, yCoord):
            self.pathMatrix[yCoord][xCoord] = len(self.adjacencyList)

    def __addPointToAdjacencyList(self, xCoord, yCoord):
            self.adjacencyList.append([(xCoord, yCoord), []])
    
    def __findPointAdjacencies(self, xCoord, yCoord):
        directions = ['D','U','R','L']
        for direction in directions:
            currentPoint = len(self.adjacencyList) - 1
            xAdjacent, yAdjacent = self.__parseDirections(direction, xCoord, yCoord)
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
    def __parseDirections(d, x, y):
        directions = {
            'D': [x, y + 1],
            'U': [x, y - 1],
            'R': [x + 1, y],
            'L': [x - 1, y]
        }
        return directions[d]

if __name__ == '__main__':
    from neuralstrand import NeuralStrand
    import csv
    f = open("puzzle3.txt", "r")
    strands = []
    for line in f:
        strand = NeuralStrand(line)
        strands.append(strand)
    graph = Graph()
    for strand in strands:
        graph.setGraph(strand)

    with open('testFile.csv', mode='w') as testFile:
        fileWriter = csv.writer(testFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        fileWriter.writerows(graph.pathMatrix)