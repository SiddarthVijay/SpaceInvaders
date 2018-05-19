from main import *


class SpaceShip:
    def __init__(self, SpaceShip_x, SpaceShip_y):
        self.x = SpaceShip_x
        self.y = SpaceShip_y

    def displayShip(self):
        gameDisplay.blit(shipImage, (self.x, self.y))
