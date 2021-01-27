class PathMatrix:
    def __init__(self):
        self.pathMatrix = []

    def expandToXY(self, x, y):
        while len(self.pathMatrix) <= y:
            self.pathMatrix.append([])
        while len(self.pathMatrix[y]) <= x:
            self.pathMatrix[y].append(None)
    
    def setPoint(self, x, y, adjacencyIndex):
        self.pathMatrix[y][x] = adjacencyIndex

    def getPoint(self, x, y):
        return self.pathMatrix[y][x]
    
    def getMatrix(self):
        return self.pathMatrix