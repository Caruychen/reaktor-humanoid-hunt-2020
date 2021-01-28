from sub_pkg.coordinate import Coordinate

class BreadthFirstPaths:
    def __init__(self, graph):
        self.marked = []
        self.edgeTo = []
        self.paths = []
        self.__breadthFirstSearch(graph)
        self.__setWorkingPaths(graph)
        
    def getPaths(self):
        pathStrings = []
        for path in self.paths:
            pathStrings.append(self.__convertPathToString(path))
        return pathStrings
        
    def __breadthFirstSearch(self, graph):
        adjacencyList = graph.getAdjacencyList()
        startIndex = graph.getEndPoints()['S'][0]
        queue = [startIndex]
        self.__addMark(startIndex)
        while len(queue) > 0:
            currentIndex = queue.pop(0)
            adjacencies = adjacencyList[currentIndex][1]
            for adjacency in adjacencies:
                if self.__isUnmarked(adjacency):
                    queue.append(adjacency)
                    self.__addMark(adjacency)
                    self.__addEdgeTo(adjacency, currentIndex)

    def __setWorkingPaths(self, graph):
        endPoints = graph.getEndPoints()
        adjacencyList = graph.getAdjacencyList()
        for finishIndex in endPoints['F']:
            path = []
            currentIndex = finishIndex
            while True:
                path.append(adjacencyList[currentIndex][0])
                if currentIndex == endPoints['S'][0]:
                    self.paths.append(path[::-1])
                    break
                currentIndex = self.edgeTo[currentIndex]
                if currentIndex is None:
                    break


    def __addMark(self, pointIndex):
        while len(self.marked) <= pointIndex:
            self.marked.append(False)
        self.marked[pointIndex] = True
    
    def __addEdgeTo(self, adjacency, pointIndex):
        while len(self.edgeTo) <= adjacency:
            self.edgeTo.append(None)
        self.edgeTo[adjacency] = pointIndex
    
    def __isUnmarked(self, adjacency):
        return len(self.marked) <= adjacency or not self.marked[adjacency]

    @staticmethod
    def __convertPathToString(path):
        for (idx, point) in enumerate(path):
            currentPoint = Coordinate(point[0], point[1])
            if idx == 0:
                directions = str(currentPoint.getX()) + ',' + str(currentPoint.getY()) + ' '
            else:
                if idx > 1:
                    directions += ','
                directions += currentPoint.mapDirectionFrom(prevPointXY)
            prevPointXY = currentPoint
        return directions
        

if __name__ == '__main__':
    from neuralstrand import NeuralStrand
    from graph import Graph

    testInput = [
        '0,0 R,R,S',
        '3,0 R,D,L,D,R,F',
        '5,1 D,D,F',
        '3,3 R,R,R'
    ]
    testCompletePath = ['2,0 R,R,D,D', '2,0 R,R,D,D,R,D']

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

    bfPath = BreadthFirstPaths(setGraph(setStrands(testInput)))
    assert(bfPath.getPaths() == testCompletePath)