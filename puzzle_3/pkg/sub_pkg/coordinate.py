class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def getAdjacent(self, d):
        directions = {
            'D': Coordinate(self.x, self.y + 1),
            'U': Coordinate(self.x, self.y - 1),
            'R': Coordinate(self.x + 1, self.y),
            'L': Coordinate(self.x - 1, self.y)
        }
        return directions[d]

    def mapDirectionFrom(self, other):
        if self.x < other.x:
            return 'L'
        elif self.x > other.x:
            return 'R'
        else:
            if self.y < other.y:
                return 'U'
            elif self.y > other.y:
                return 'D'
