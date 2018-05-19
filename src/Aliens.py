from main import *

class Aliens:
    def __init__(self):
        self.alive = True
        self.hitA = False
        self.hitB = False
        self.lifetime = 200
        self.x = random.randrange(0, display_width)
        self.y = random.randrange(200)

    def missileA(self):
        self.hitA = True
        self.alive = False

    def missileB(self):
        self.hitB = True
        self.lifetime += 2

    def display(self):
        if not self.hitB:
            gameDisplay.blit(alienImageA, (self.x, self.y))
        else:
            gameDisplay.blit(alienImageB, (self.x, self.y))
