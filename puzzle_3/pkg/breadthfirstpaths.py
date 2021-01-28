from coordinate import Coordinate

class BreadthFirstPaths:
    def __init__(self, graph):
        self.marked = []
        self.edgeTo = []
        self.paths = []
        self.__breadthFirstSearch(graph)
        self.__setPaths(graph)
        
    def getPaths(self):
        pathStrings = []
        for path in self.paths:
            for (idx, point) in enumerate(path):
                currentPointXY = Coordinate(point[1][0], point[1][1])
                if idx == 0:
                    directions = str(currentPointXY.getX()) + ',' + str(currentPointXY.getY()) + ' '
                else:
                    if idx > 1:
                        directions += ','
                    directions += currentPointXY.mapDirectionFrom(prevPointXY)
                prevPointXY = currentPointXY
            pathStrings.append(directions)
        return pathStrings
        
    def __breadthFirstSearch(self, graph):
        adjacencyList = graph.getAdjacencyList()
        startIndex = graph.getEndPoints()['S'][0]
        queue = [startIndex]
        self.__addMark(startIndex)
        while len(queue) > 0:
            currentPointIndex = queue.pop(0)
            currentAdjacencies = adjacencyList[currentPointIndex][1]
            for adjacency in currentAdjacencies:
                if self.__isUnmarked(adjacency):
                    queue.append(adjacency)
                    self.__addMark(adjacency)
                    self.__addEdge(adjacency, currentPointIndex)

    def __setPaths(self, graph):
        endPoints = graph.getEndPoints()
        adjacencyList = graph.getAdjacencyList()
        for finishIndex in endPoints['F']:
            path = [(finishIndex, self.getPointXY(finishIndex, adjacencyList))]
            nextIndex = self.edgeTo[finishIndex]
            while True:
                if nextIndex is None:
                    break
                path.append((nextIndex, self.getPointXY(nextIndex, adjacencyList)))
                nextIndex = self.edgeTo[nextIndex]
            if self.__isPathComplete(path, endPoints):
                path.reverse()
                self.paths.append(path)

    def __addMark(self, pointIndex):
        while len(self.marked) <= pointIndex:
            self.marked.append(False)
        self.marked[pointIndex] = True
    
    def __addEdge(self, adjacency, pointIndex):
        while len(self.edgeTo) <= adjacency:
            self.edgeTo.append(None)
        self.edgeTo[adjacency] = pointIndex
    
    def __isUnmarked(self, adjacency):
        return len(self.marked) <= adjacency or not self.marked[adjacency]

    @staticmethod
    def getPointXY(index, adjacencyList):
        return adjacencyList[index][0]
    
    @staticmethod
    def __isPathComplete(path, endPoints):
        return path[-1][0] == endPoints['S'][0]

if __name__ == '__main__':
    import csv
    from neuralstrand import NeuralStrand
    from graph import Graph

    f = open('puzzle3.txt', 'r')

    strands = []
    for line in f:
        strand = NeuralStrand(line)
        strands.append(strand)
        
    graph = Graph()
    for strand in strands:
        graph.setGraph(strand)
    
    bfPath = BreadthFirstPaths(graph)
    print(bfPath.getPaths())