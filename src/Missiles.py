from main import *

class Missiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True


class Missile_A(Missiles):
    def __init__(self, x, y):
        self.type = 'A'
        Missiles.__init__(self, x, y)

    def display(self):
        gameDisplay.blit(missileA_Image, (self.x, self.y))

    def move(self):
        self.y -= 5


class Missile_B(Missiles):
    def __init__(self, x, y):
        self.type = 'B'
        Missiles.__init__(self, x, y)

    def display(self):
        gameDisplay.blit(missileB_Image, (self.x, self.y))

    def move(self):
        self.y -= 10
