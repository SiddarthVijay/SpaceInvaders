#!/bin/usr/env python3

# Imports
import pygame
import random
import time
import threading

pygame.init()

# Define colours
black = (0, 0, 0)
white = (255, 255, 255)

# Dispaly Settings
display_width = 1920
display_height = 1080

# Spaceship image
spaceShip_width = 100
spaceShip_height = 146

# Missile image
missile_width = 100
missile_height = 100

# Alien Image
alien_width = 80
alien_height = 75

# Data arrays
missiles = []
aliens = []

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Invaders')

# Images
shipImage = pygame.image.load('../files/SpaceShip.png')
alienImageA = pygame.image.load('../files/AlienA.png')
alienImageB = pygame.image.load('../files/AlienB.png')
missileA_Image = pygame.image.load('../files/Missile1.png')
missileB_Image = pygame.image.load('../files/Missile2.png')
backgroundImage = pygame.image.load('../files/Background.png')

# Game clock
gameClock = pygame.time.Clock()
