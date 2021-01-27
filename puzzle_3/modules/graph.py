from pathmatrix import PathMatrix
from adjacencylist import AdjacencyList
from coordinate import Coordinate

class Graph:
    def __init__(self, adjacencyList=[], endPoints={}):
        self.adjacencyList = AdjacencyList()
        self.pathMatrix = PathMatrix()
        self.endPoints = endPoints

    def setGraph(self, neuralStrand):
        point = Coordinate(neuralStrand.getX(), neuralStrand.getY())
        path = neuralStrand.getPath()
        self.addPointToGraph(point)
        self.addPathToGraph(path, point)
    
    def addPointToGraph(self, point):
        self.pathMatrix.expandToXY(point)
        if self.pathMatrix.getPoint(point) == None:
            self.pathMatrix.setPoint(point, len(self.adjacencyList.getList()))
            self.adjacencyList.setPoint(point)
            self.adjacencyList.setAdjacencies(point, self.pathMatrix)
    
    def addPathToGraph(self, path, point):
        for step in path:
            try:
                point = point.getAdjacent(step)
                self.addPointToGraph(point)
            except:
                self.__addToEndPoints(step, point)

    def getPathMatrix(self):
        return self.pathMatrix.getMatrix()
    
    def getAdjacencyList(self):
        return self.adjacencyList.getList()

    def __addToEndPoints(self, step, point):
        if step not in self.endPoints:
            self.endPoints[step] = [self.pathMatrix.getPoint(point)]
        else:
            if self.pathMatrix.getPoint(point) not in self.endPoints[step]:
                self.endPoints[step].append(self.pathMatrix.getPoint(point))

    @staticmethod
    def __parseDirections(d, point):
        x, y = point.getX(), point.getY()
        directions = {
            'D': Coordinate(x, y + 1),
            'U': Coordinate(x, y - 1),
            'R': Coordinate(x + 1, y),
            'L': Coordinate(x - 1, y)
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

        fileWriter.writerows(graph.pathMatrix.pathMatrix)