class PathMatrix:
    '''
    Holds a 2 dimensional matrix mapping the entire neural path.
    Maps each adjacencyList index to a corresponding x, y coordinate in this matrix
    '''

    def __init__(self):
        self.pathMatrix = []

    def expandToXY(self, point):
        y, x = point.getY(), point.getX()
        while len(self.pathMatrix) <= y:
            self.pathMatrix.append([])
        while len(self.pathMatrix[y]) <= x:
            self.pathMatrix[y].append(None)
    
    def setIndex(self, point, adjacencyIndex):
        y, x = point.getY(), point.getX()
        self.pathMatrix[y][x] = adjacencyIndex

    def getIndex(self, point):
        y, x = point.getY(), point.getX()
        if len(self.pathMatrix) > y and len(self.pathMatrix[y]) > x:
            return self.pathMatrix[y][x]
    
    def getMatrix(self):
        return self.pathMatrix