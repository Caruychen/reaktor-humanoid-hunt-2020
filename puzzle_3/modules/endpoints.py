class EndPoints:
    def __init__(self):
        self.endPoints = {}

    def setEndPoint(self, step, pointIndex):
        if step not in self.endPoints:
            self.endPoints[step] = [pointIndex]
        else:
            if pointIndex not in self.endPoints[step]:
                self.endPoints[step].append(pointIndex)
    
    def getEndPoints(self):
        return self.endPoints