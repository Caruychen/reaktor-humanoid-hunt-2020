import sys, os
if sys.version_info[0] < 3:
    raise Exception("Please use Python 3")

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, pathname + '/pkg')
sys.path.insert(1, pathname + '/pkg/sub_pkg')

from pkg.neuralstrand import NeuralStrand
from pkg.graph import Graph
from pkg.breadthfirstpaths import BreadthFirstPaths


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
    with open(pathname + '/puzzle3.txt', 'r') as inputFile:
        answers = getAnswers(inputFile)
        print('Writing answers to ' + pathname + '/solutions.txt...')
        print(answers)
        with open(pathname + '/solutions.txt', mode='w') as solutions:
            for answer in answers:
                solutions.write(answer + '\n')