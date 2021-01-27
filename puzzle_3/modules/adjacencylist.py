class AdjacencyList:
    def __init__(self):
        self.adjacencyList = []
    
    def setPoint(self, point):
        x, y = point.getX(), point.getY()
        self.adjacencyList.append([(x, y), []])

    def setAdjacencies(self, point, pathMatrix):
        directions = ['D','U','R','L']
        currentPointIndex = len(self.adjacencyList) - 1
        x, y = point.getX(), point.getY()
        for direction in directions:
            xAdjacent, yAdjacent = self.__parseDirections(direction, x, y)
            try:
                if xAdjacent > 0 and yAdjacent > 0:
                    adjacentPoint = pathMatrix.getPoint(xAdjacent, yAdjacent)
                    if adjacentPoint != None:
                        self.__addEdge(currentPointIndex, adjacentPoint)
            except:
                pass
    
    def getList(self):
        return self.adjacencyList

    def __addEdge(self, currentPointIndex, adjacentPoint):
        self.adjacencyList[currentPointIndex][1].append(adjacentPoint)
        self.adjacencyList[adjacentPoint][1].append(currentPointIndex)

    @staticmethod
    def __parseDirections(d, x, y):
        directions = {
            'D': [x, y + 1],
            'U': [x, y - 1],
            'R': [x + 1, y],
            'L': [x - 1, y]
        }
        return directions[d]