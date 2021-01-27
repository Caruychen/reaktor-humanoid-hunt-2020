from modules.neuralstrand import NeuralStrand
from modules.graph import Graph
from modules.breadthfirstpaths import BreadthFirstPaths

f = open("puzzle3.txt", "r")

neuralStrands = [NeuralStrand(line) for line in f]

# def constructGraphs(file):
#     adjacencyArray = []
#     positionMatrix = []
#     endDict = {}
#     inputs = parseInputs(file)
#     for input in inputs:
#         xCoord = input[0]
#         yCoord = input[1]
#         buildPath = input[2]
#         adjacencyArray, positionMatrix = updateAdjacencyAndMatrix(adjacencyArray, positionMatrix, xCoord, yCoord)
#         for step in buildPath:
#             try: 
#                 xCoord, yCoord = directions[step](xCoord, yCoord)
#                 adjacencyArray, positionMatrix = updateAdjacencyAndMatrix(adjacencyArray, positionMatrix, xCoord, yCoord)
#             except:
#                 if step not in endDict:
#                     endDict[step] = [positionMatrix[yCoord][xCoord]]
#                 else:
#                     if positionMatrix[yCoord][xCoord] not in endDict[step]:
#                         endDict[step].append(positionMatrix[yCoord][xCoord])
#     return adjacencyArray, positionMatrix, endDict

# def parseInputs(file):
#     inputs = []
#     for line in f:
#         splitLine = line.strip().split(' ')
#         path = [int(coordinate) for coordinate in splitLine[0].split(',')]
#         try:
#             path.append(splitLine[1].split(','))
#         except:
#             path.append('')
#         inputs.append(path)
#     return inputs

# def expandPositionMatrix(array, xCoord, yCoord):
#     while len(array) <= yCoord:
#         array.append([])
#     while len(array[yCoord]) <= xCoord:
#         array[yCoord].append(None)
#     return array

# def moveDown(xCoord, yCoord):
#     return xCoord, yCoord + 1
# def moveUp(xCoord, yCoord):
#     return xCoord, yCoord - 1
# def moveRight(xCoord, yCoord):
#     return xCoord + 1, yCoord
# def moveLeft(xCoord, yCoord):
#     return xCoord - 1, yCoord

# directions = {
#     'D': moveDown,
#     'U': moveUp,
#     'R': moveRight,
#     'L': moveLeft
# }

# def addAdjacencies(adjacencyArray, positionMatrix, xCoord, yCoord):
#     for direction in directions:
#         currentVertex = len(adjacencyArray) - 1
#         xToCheck, yToCheck = directions[direction](xCoord, yCoord)
#         try:
#             if xToCheck > 0 and yToCheck > 0:
#                 adjVertex = positionMatrix[yToCheck][xToCheck]
#                 if adjVertex != None:
#                     adjacencyArray[currentVertex][1].append(adjVertex)
#                     adjacencyArray[adjVertex][1].append(currentVertex)
#         except:
#             pass
#     return adjacencyArray

# def updateAdjacencyAndMatrix(adjacencyArray, positionMatrix, xCoord, yCoord):
#     positionMatrix = expandPositionMatrix(positionMatrix, xCoord, yCoord)
#     if positionMatrix[yCoord][xCoord] == None:
#         positionMatrix[yCoord][xCoord] = len(adjacencyArray)
#         adjacencyArray.append([(xCoord, yCoord),[]])
#         adjacencyArray = addAdjacencies(adjacencyArray, positionMatrix, xCoord, yCoord)
#     return adjacencyArray, positionMatrix

# ###

# def addMark(marked, vertex):
#     while len(marked) <= vertex:
#         marked.append(False)
#     marked[vertex] = True
#     return marked

# def addEdge(edgeTo, adj, currentVertex):
#     while len(edgeTo) <= adj:
#         edgeTo.append(None)
#     edgeTo[adj] = currentVertex
#     return edgeTo

# def breadthFirstSearch(adjacencyArray, start):
#     marked = []
#     edgeTo = []
#     queue = []
#     queue.append(start)
#     marked = addMark(marked, start)
#     while len(queue) > 0:
#         currentVertex = queue.pop(0)
#         for adj in adjacencyArray[currentVertex][1]:
#             try:
#                 if not marked[adj]:
#                     queue.append(adj)
#                     marked = addMark(marked, adj)
#                     edgeTo = addEdge(edgeTo, adj, currentVertex)
#             except:
#                 queue.append(adj)
#                 marked = addMark(marked, adj)
#                 edgeTo = addEdge(edgeTo, adj, currentVertex)
#     return edgeTo

# def mapPathways(edgeTo, endDict):
#     pathways = []
#     for finish in endDict['F']:
#         pathway = [finish]
#         vertexBefore = edgeTo[finish]
#         while True:
#             if vertexBefore is None:
#                 break
#             pathway.append(vertexBefore)
#             vertexBefore = edgeTo[vertexBefore]
#         if pathway[-1] == endDict['S'][0]:
#             pathway.reverse()
#             pathways.append(pathway)
#     return pathways

# def makeDirections(curCoords, prevCoords):
#     if curCoords['x'] < prevCoords['x']:
#         return 'L'
#     elif curCoords['x'] > prevCoords['x']:
#         return 'R'
#     else:
#         if curCoords['y'] < prevCoords['y']:
#             return 'U'
#         elif curCoords['y'] > prevCoords['y']:
#             return 'D'
#     print('error')

# adjacencyArray, positionMatrix, endDict = constructGraphs(f)
# edgeTo = breadthFirstSearch(adjacencyArray, endDict['S'][0])
# pathways = mapPathways(edgeTo, endDict)

# answers = []
# for pathway in pathways:
#     for (idx, vertex) in enumerate(pathway):
#         curCoords = {
#             'x': adjacencyArray[vertex][0][0],
#             'y': adjacencyArray[vertex][0][1]
#         }
#         if idx == 0:
#             directions = str(curCoords['x']) + ',' + str(curCoords['y']) + ' '
#         else:
#             if idx > 1:
#                 directions += ','
#             directions += makeDirections(curCoords, prevCoords)

#         prevCoords = {
#             'x': curCoords['x'],
#             'y': curCoords['y']
#         }
#     answers.append(directions)


# with open('pathFile.csv', mode='w') as pathFile:
#     employee_writer = csv.writer(pathFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerows(positionMatrix)

# with open('solutions.txt', mode='w') as solutions:
#     for answer in answers:
#         solutions.write(answer + '\n')

# f.close()