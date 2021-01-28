from package.neuralstrand import NeuralStrand
from package.graph import Graph
from package.breadthfirstpaths import BreadthFirstPaths

def parseNeuralStrands(inputFile):
    return [NeuralStrand(line) for line in inputFile]

def createGraphObjectFrom(neuralStrands):
    graph = Graph()
    for strand in neuralStrands:
        graph.setGraph(strand)
    return graph

def processGraph(graph):
    bfs = BreadthFirstPaths(graph)
    return bfs.getPaths()

def getAnswers(inputFile):
    neuralStrands = parseNeuralStrands(inputFile)
    graph = createGraphObjectFrom(neuralStrands)
    return processGraph(graph)

if __name__ == '__main__':
    with open('puzzle3.txt', 'r') as inputFile:
        answers = getAnswers(inputFile)
        with open('solutions.txt', mode='w') as solutions:
            for answer in answers:
                solutions.write(answer + '\n')