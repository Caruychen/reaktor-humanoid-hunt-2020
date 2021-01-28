class AdjacencyList:
    '''
    Maintains an indexed list of coordinates and adjacency lists:
        [(x,y), [adjacencyIndex, ...], ...]
    Each element is a point on the path matrix, and holds its correspondnig coordinates.
    Setting adjacencies adds to the adjacency list of each point with a parallel adjacency.
    '''

    def __init__(self):
        self.adjacencyList = []
    
    def setPoint(self, point):
        x, y = point.getX(), point.getY()
        self.adjacencyList.append([(x, y), []])

    def setAdjacencies(self, point, pathMatrix):
        directions = ['D','U','R','L']
        currentIndex = len(self.adjacencyList) - 1
        for direction in directions:
            adjacentPoint = point.getAdjacentCoordinate(direction)
            if self.__isValidAdjacency(adjacentPoint, pathMatrix):
                adjacentIndex = pathMatrix.getIndex(adjacentPoint)
                self.__addEdge(currentIndex, adjacentIndex)
    
    def getList(self):
        return self.adjacencyList

    def __addEdge(self, currentIndex, adjacentIndex):
        self.adjacencyList[currentIndex][1].append(adjacentIndex)
        self.adjacencyList[adjacentIndex][1].append(currentIndex)
    
    def __isValidAdjacency(self, adjacentPoint, pathMatrix):
        x, y = adjacentPoint.getX(), adjacentPoint.getY()
        adjacentIndex = pathMatrix.getIndex(adjacentPoint)
        return x >= 0 and y >= 0 and adjacentIndex != None
