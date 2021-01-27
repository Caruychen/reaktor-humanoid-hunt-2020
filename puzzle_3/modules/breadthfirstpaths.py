from coordinate import Coordinate

class BreadthFirstPaths:
    def __init__(self, graph):
        self.marked = []
        self.edgeTo = []
        self.paths = []
        self.__bfs(graph)
        self.__findPaths(graph)
        
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
        
    def __bfs(self, graph):
        adjacencyList = graph.getAdjacencyList()
        startIndex = graph.getEndPoints()['S'][0]
        queue = []
        queue.append(startIndex)
        self.__addMark(startIndex)
        while len(queue) > 0:
            currentPointIndex = queue.pop(0)
            for adjacency in adjacencyList[currentPointIndex][1]:
                try:
                    if not self.marked[adjacency]:
                        queue.append(adjacency)
                        self.__addMark(adjacency)
                        self.__addEdge(adjacency, currentPointIndex)
                except:
                    queue.append(adjacency)
                    self.__addMark(adjacency)
                    self.__addEdge(adjacency, currentPointIndex)

    def __findPaths(self, graph):
        endPoints = graph.getEndPoints()
        adjacencyList = graph.getAdjacencyList()
        for finish in endPoints['F']:
            path = [(finish, adjacencyList[finish][0])]
            pointBefore = self.edgeTo[finish]
            while True:
                if pointBefore is None:
                    break
                path.append((pointBefore, adjacencyList[pointBefore][0]))
                pointBefore = self.edgeTo[pointBefore]
            if path[-1][0] == endPoints['S'][0]:
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


if __name__ == '__main__':
    import csv
    from neuralstrand import NeuralStrand
    from graph import Graph
    f = open("puzzle3.txt", "r")
    strands = []
    for line in f:
        strand = NeuralStrand(line)
        strands.append(strand)
    graph = Graph()
    for strand in strands:
        graph.setGraph(strand)
    
    bfPath = BreadthFirstPaths(graph)
    print(bfPath.getPaths())