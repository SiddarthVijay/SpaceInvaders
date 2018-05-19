from main import *


def displayElements(spaceShip_x, spaceShip_y):
    gameDisplay.blit(backgroundImage, (0, 0))
    gameDisplay.blit(shipImage, (spaceShip_x, spaceShip_y))
