class AdjacencyList:
    def __init__(self):
        self.adjacencyList = []
    
    def setPoint(self, x, y):
        self.adjacencyList.append([(x, y), []])

    def setAdjacencies(self, x, y, pathMatrix):
        directions = ['D','U','R','L']
        currentPoint = len(self.adjacencyList) - 1
        for direction in directions:
            xAdjacent, yAdjacent = self.__parseDirections(direction, x, y)
            try:
                if xAdjacent > 0 and yAdjacent > 0:
                    adjacentPoint = pathMatrix.getPoint(xAdjacent, yAdjacent)
                    if adjacentPoint != None:
                        self.__addEdge(currentPoint, adjacentPoint)
            except:
                pass
    
    def getList(self):
        return self.adjacencyList

    def __addEdge(self, currentPoint, adjacentPoint):
        self.adjacencyList[currentPoint][1].append(adjacentPoint)
        self.adjacencyList[adjacentPoint][1].append(currentPoint)

    @staticmethod
    def __parseDirections(d, x, y):
        directions = {
            'D': [x, y + 1],
            'U': [x, y - 1],
            'R': [x + 1, y],
            'L': [x - 1, y]
        }
        return directions[d]