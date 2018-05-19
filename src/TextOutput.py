from main import *

def text_objects(text, font):

    # The arguments are (what we want to render, anti-aliasing, colour)
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(textToPrint):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(textToPrint, largeText)
    TextRect.center = ((display_width/2), (display_height/2))

    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    # Wait for 2 seconds before restarting the game
    time.sleep(1)

def score(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score: " + str(count), True, white)
    gameDisplay.blit(text, (0, 0))
