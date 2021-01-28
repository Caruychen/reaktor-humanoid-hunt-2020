class EndPoints:
    ''' 
    Holds a collection of point indices at the X (wall), F (finishing point)
    and S (start point) locations.
    '''
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