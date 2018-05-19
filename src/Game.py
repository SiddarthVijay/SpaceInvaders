from main import *
from Display import *
from Missiles import *
from Aliens import *
# from Collisions import *
from TextOutput import *

def quitGame():
    message_display('Game Over')
    scoreCounter = 0
    pygame.quit()
    quit()

def checkCollisions(aliens, missiles):
    scoreCounter = 0
    for a in aliens:
        for m in missiles:
            if ((m.y > a.y) and (m.y < a.y + alien_height)) or ((m.y + missile_height) > a.y and (m.y + missile_height) < (a.y + alien_height)):
                if (((m.x > a.x) and (m.x < a.x + alien_width)) or ((m.x + missile_width) > a.x and (m.x + missile_width) < (a.x + alien_width))):
                    m.alive = False
                    if m.type == 'A':
                        a.alive = False
                        a.hitA = True
                        aliens.remove(a)
                        scoreCounter += 1
                    else:
                        a.hitB = True
                        a.lifetime += 100
                    missiles.remove(m)
    return scoreCounter


def gameLoop():
    spaceShip_x = (display_width * 0.45)
    spaceShip_y = (display_height * 0.80)

    spaceShipMove_x = 0
    spaceShipMove_y = 0

    gameExit = False

    counter = 0
    scoreCounter = 0

    while not gameExit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT):
                    spaceShipMove_x = -15
                elif (event.key == pygame.K_RIGHT):
                    spaceShipMove_x = 15
                elif (event.key == pygame.K_UP):
                    spaceShipMove_y = -15
                elif (event.key == pygame.K_DOWN):
                    spaceShipMove_y = 15
                elif (event.key == pygame.K_SPACE):
                    m = Missile_A(spaceShip_x, spaceShip_y - missile_height)
                    missiles.append(m)
                elif (event.key == pygame.K_s):
                    m = Missile_B (spaceShip_x, spaceShip_y - missile_height)
                    missiles.append(m)

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or(event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                    spaceShipMove_x = 0
                    spaceShipMove_y = 0

        if spaceShip_x <= 0 - spaceShip_width:
            spaceShip_x = display_width
        elif spaceShip_x >= display_width:
            spaceShip_x = -spaceShip_width

        if spaceShip_y <= 0 - spaceShip_height:
            spaceShip_y = display_height
        elif spaceShip_y >= display_height:
            spaceShip_y = -spaceShip_height

        spaceShip_x += spaceShipMove_x
        spaceShip_y += spaceShipMove_y

        displayElements(spaceShip_x, spaceShip_y)

        s = 0
        s = checkCollisions(aliens, missiles)

        for m in missiles:
            if m.alive is True:
                m.display()
                if m.type == 'A':
                    m.y -= 5
                else:
                    m.y -= 10

        if counter == 60:
            counter = 0
            a = Aliens()
            aliens.append(a)
        counter += 1

        for a in aliens:
            if a.alive is True:
                if a.hitB is True:
                    gameDisplay.blit(alienImageB, (a.x, a.y))
                elif a.hitB is False:
                    gameDisplay.blit(alienImageA, (a.x, a.y))
                    a.lifetime -= 1
                    if a.lifetime <= 0:
                        aliens.remove(a)
        scoreCounter += s
        score(scoreCounter)

        pygame.display.update()

        gameClock.tick(60)

gameLoop()
