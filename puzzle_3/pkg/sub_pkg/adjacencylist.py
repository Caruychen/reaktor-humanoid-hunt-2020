class AdjacencyList:
    '''
    Maintains an indexed list of coordinates and adjacency lists:
        [(x,y), [adjacencies, ...], ...]
    Each element holds coordinates of its corresponding pointon the path matrix,
    and setting adjacencies adds parallel edges for each point adjacent to each other.
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
            x, y = adjacentPoint.getX(), adjacentPoint.getY()
            try:
                if x > 0 and y > 0:
                    adjacentIndex = pathMatrix.getIndex(adjacentPoint)
                    if adjacentIndex != None:
                        self.__addEdge(currentIndex, adjacentIndex)
            except:
                pass
    
    def getList(self):
        return self.adjacencyList

    def __addEdge(self, currentIndex, adjacentIndex):
        self.adjacencyList[currentIndex][1].append(adjacentIndex)
        self.adjacencyList[adjacentIndex][1].append(currentIndex)
