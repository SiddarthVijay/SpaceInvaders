from main import *
from Game import *


def checkCollisions(aliens, missiles, scoreCounter):
    for a in aliens:
        for m in missiles:
            if ((m.y >= a.y) and (m.y <= a.y + alien_height)) or ((m.y + missile_height) >= a.y and (m.y + missile_height) <= (a.y + alien_height)):
                if (((m.x >= a.x) and (m.x <= a.x + alien_width)) or ((m.x + missile_width) >= a.x and (m.x + missile_width) <= (a.x + alien_width))):
                    m.alive = False
                    if m.type == 'A':
                        a.alive == False
                        a.hitA == True
                        aliens.remove(a)
                        scoreCounter += 1
                    else:
                        a.hitB == True
                        a.lifetime += 100
                    missiles.remove(m)
