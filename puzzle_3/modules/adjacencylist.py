class AdjacencyList:
    def __init__(self):
        self.adjacencyList = []
    
    def setPoint(self, point):
        x, y = point.getX(), point.getY()
        self.adjacencyList.append([(x, y), []])

    def setAdjacencies(self, point, pathMatrix):
        directions = ['D','U','R','L']
        currentPointIndex = len(self.adjacencyList) - 1
        for direction in directions:
            adjacentCoord = point.getAdjacent(direction)
            try:
                if adjacentCoord.getX() > 0 and adjacentCoord.getY() > 0:
                    adjacentPointIndex = pathMatrix.getPoint(adjacentCoord)
                    if adjacentPointIndex != None:
                        self.__addEdge(currentPointIndex, adjacentPointIndex)
            except:
                pass
    
    def getList(self):
        return self.adjacencyList

    def __addEdge(self, currentPointIndex, adjacentPointIndex):
        self.adjacencyList[currentPointIndex][1].append(adjacentPointIndex)
        self.adjacencyList[adjacentPointIndex][1].append(currentPointIndex)
