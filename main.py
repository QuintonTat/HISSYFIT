import pygame, random

pygame.init() # initalises pygame

width, height = 1000, 500 # establishes width and height variables
screen = pygame.display.set_mode((width, height)) # creates the screen

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit



    