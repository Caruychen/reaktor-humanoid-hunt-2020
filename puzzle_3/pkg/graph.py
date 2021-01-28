from sub_pkg.pathmatrix import PathMatrix
from sub_pkg.adjacencylist import AdjacencyList
from sub_pkg.endpoints import EndPoints
from sub_pkg.coordinate import Coordinate

class Graph:
    '''
    Complete graph representation holding the adjacency list, 2D path matrix, and end point collections
    Adjacency list allows search algorithm to find a path by iterating over adjacencies to each point.
    Path matrix is mainly used internally to validate adjacencies.
    '''
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
            newAdjacencyIndex = len(self.adjacencyList.getList())
            self.pathMatrix.setIndex(point, newAdjacencyIndex)
            self.adjacencyList.setPoint(point)
            self.adjacencyList.setAdjacencies(point, self.pathMatrix)
    
    def addPathToGraph(self, path, point):
        directions = ['D','U','R','L']
        for step in path:
            if step in directions:
                point = point.getAdjacentCoordinate(step)
                self.addPointToGraph(point)
            else:
                endIndex = self.pathMatrix.getIndex(point)
                self.endPoints.setEndPoint(step, endIndex)

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
        [(0, 0), [1]],
        [(1, 0), [0, 2]],
        [(2, 0), [1, 3, 9]],
        [(3, 0), [2, 4, 8]],
        [(4, 0), [3, 5]],
        [(4, 1), [4, 6, 8]],
        [(4, 2), [5, 7]],
        [(3, 2), [6, 8]],
        [(3, 1), [7, 3, 5, 9]],
        [(2, 1), [2, 8]]
    ]

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

    