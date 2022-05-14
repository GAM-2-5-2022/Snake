from asyncio import events
from math import fabs
from turtle import Turtle
import pygame 
from pygame.locals import * 

hight  = int(input("Enter hight: "))
width  = int(input("Enter width: "))

pokretanje = True

#sve vezano za igraca


while pokretanje == True:

    
    #display
    window = pygame.display.set_mode((hight, width))

    window.fill((255, 0, 0))


    #igrac
    igrac = pygame.image.load("ase64.png").convert()
    window.blit(igrac, (hight/2, width/2))
    
    pygame.display.flip()


    for event in pygame.event.get():

        #provjerava koja je tipka pritisnuta
        if(event.type == KEYDOWN):

            #ako je ovo pritisnuto zaustavlja igru
            if(event.key == K_ESCAPE):
                pokretanje = False