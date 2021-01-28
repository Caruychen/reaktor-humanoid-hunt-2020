from sub_pkg.pathmatrix import PathMatrix
from sub_pkg.adjacencylist import AdjacencyList
from sub_pkg.endpoints import EndPoints
from sub_pkg.coordinate import Coordinate

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
        if self.pathMatrix.getIndex(point) == None:
            self.pathMatrix.setIndex(point, len(self.adjacencyList.getList()))
            self.adjacencyList.setPoint(point)
            self.adjacencyList.setAdjacencies(point, self.pathMatrix)
    
    def addPathToGraph(self, path, point):
        for step in path:
            try:
                point = point.getAdjacentCoordinate(step)
                self.addPointToGraph(point)
            except:
                pointIndex = self.pathMatrix.getIndex(point)
                self.endPoints.setEndPoint(step, pointIndex)

    def getPathMatrix(self):
        return self.pathMatrix.getMatrix()
    
    def getAdjacencyList(self):
        return self.adjacencyList.getList()

    def getEndPoints(self):
        return self.endPoints.getEndPoints()

if __name__ == '__main__':
    from neuralstrand import NeuralStrand
    testInput = [
        '0,0 R,R,R,R',
        '4,1 D',
        '3,2 U,L'
    ]
    testMatrix = [
        [0, 1, 2, 3, 4],
        [None, None, 9, 8, 5],
        [None, None, None, 7, 6]
    ]
    testAdjacencies = [
        [(0, 0), []],
        [(1, 0), []],
        [(2, 0), []], 
        [(3, 0), []], 
        [(4, 0), []], 
        [(4, 1), [6, 8]], 
        [(4, 2), [5, 7]], 
        [(3, 2), [6, 8]], 
        [(3, 1), [7, 5, 9]], 
        [(2, 1), [8]]]

    def setStrands(testInput):
        strands = []
        for line in testInput:
            strand = NeuralStrand(line)
            strands.append(strand)
        return strands
    
    def setGraph(strands):
        graph = Graph()
        for strand in strands:
            graph.setGraph(strand)
        return graph

    graph = setGraph(setStrands(testInput))
    assert(graph.getPathMatrix() == testMatrix)
    assert(graph.getAdjacencyList() == testAdjacencies)

    