class Point:
    def __init__(self, x,y):
        self.coordX = x
        self.coordY = y
        
    def affichage(self):
        print("Le point", self.coordX ," et ", self.coordY)
        
        
point1 = Point(10,12)
point1.affichage()