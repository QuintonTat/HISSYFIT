import pygame, random

pygame.init() # initalises pygame

width, height = 950, 500 # establishes width and height variables
screen = pygame.display.set_mode((width, height)) # creates the screen
pygame.display.set_caption("HissyFit") # game name

surface = pygame.image.load("background.png")
icon = pygame.image.load('_ICON.png')
molly = pygame.image.load('_MOLLY.png')
pygame.display.set_icon(icon)
money = 0

while True:
    # makes the screen stay up without it it wont work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    # game logic here
    screen.blit(surface, (0,0))
    screen.blit(molly, (350, 100))
    pygame.display.update()


    