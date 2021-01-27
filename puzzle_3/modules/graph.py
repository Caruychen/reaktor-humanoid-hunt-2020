from pathmatrix import PathMatrix
from adjacencylist import AdjacencyList
from endpoints import EndPoints
from coordinate import Coordinate

class Graph:
    def __init__(self):
        self.adjacencyList = AdjacencyList()
        self.pathMatrix = PathMatrix()
        self.endPoints = EndPoints()

    def setGraph(self, neuralStrand):
        startPoint = Coordinate(neuralStrand.getX(), neuralStrand.getY())
        path = neuralStrand.getPath()
        self.addPointToGraph(startPoint)
        self.addPathToGraph(path, startPoint)
    
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
                pointIndex = self.pathMatrix.getPoint(point)
                self.endPoints.setEndPoint(step, pointIndex)

    def getPathMatrix(self):
        return self.pathMatrix.getMatrix()
    
    def getAdjacencyList(self):
        return self.adjacencyList.getList()

    def getEndPoints(self):
        return self.endPoints.getEndPoints()

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
    
    for adj in graph.getAdjacencyList():
        if len(adj[1]) > 4:
            print(adj)
    print(graph.getEndPoints())
   
    with open('testFile.csv', mode='w') as testFile:
        fileWriter = csv.writer(testFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        fileWriter.writerows(graph.pathMatrix.pathMatrix)