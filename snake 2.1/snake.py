#!/bin/bash
#python ./snake.py
from asyncio.format_helpers import _format_callback_source
from doctest import FAIL_FAST
from tokenize import Triple
from pygame import mixer
import pygame
import time
import random

gamer_mode = str(input("Input \"g\" for gamer mode: "))
if(gamer_mode == "g"):
    gamer_mode_b = True
    snake_speed = 30

    #background
    background = pygame.image.load("snakeGamer.jpg")
else:
    gamer_mode_b = False
    snake_speed = 15

    #background
    background = pygame.image.load("trava.jpg")

epilepsija = input("Type \"Yˇ\" for epilepsija mod: ")
epilesija_mode = False
if(epilepsija == "y" or epilepsija == "Y"):
    epilepsija_mode = True

else:
    epilepsija_mode = False

#window size
x = int(input("Horizontal: "))
y = int(input("Vertical: "))
background = pygame.transform.scale(background, (x, y))
 
#built in colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(109, 188, 252)
yellow = pygame.Color(100,255,0)
player_color_real = pygame.Color(0, 0, 0)

#player colore 
snake_color = str(input("Player color: "))
if(snake_color == "green"):
    player_color_real = green

elif(snake_color == "white"):
    player_color_real = white

elif(snake_color == "red"):
    player_color_real = red

elif(snake_color == "blue"):
    player_color_real = blue

elif(snake_color == "yellow"):
    player_color_real = yellow

else:
    player_color_real == green


#pygame summon
pygame.init()
mixer.init()

#song
#There will be error "Failed loading libmpg123-0.dll: The specified module could not be found." if limpg was not automatically installed with pygame
volume = float(input("Set your volume:"))
pygame.mixer.music.load("gas.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()



#window
pygame.display.set_caption("Snake that loves milk")
window = pygame.display.set_mode((x, y))


# FPS
fps = pygame.time.Clock()

snake_dash = False
dash_smije  = True

snake_position = [100, 50]
 
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]


fruit_position = [random.randrange(1, (x//10)) * 10,
                  random.randrange(1, (y//10)) * 10]
 
fruit_spawn = True
 

direction = "RIGHT"
change_to = direction
 
#score info
lucky = random.randrange(0, 10)
score = 0
 

def show_score(choice, color, font, size):
   

    score_font = pygame.font.SysFont(font, size)
     
    score_surface = score_font.render("Score : " + str(score), True, color)
     
    score_rect = score_surface.get_rect()
     
    window.blit(score_surface, score_rect)

def game_over():
   
    my_font = pygame.font.SysFont("times new roman", 50)
     

    game_over_surface = my_font.render(
        "Your Score is : " + str(score), True, red)
     

    game_over_rect = game_over_surface.get_rect()
     
    game_over_rect.midtop = (x/2, y/4)
     
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    time.sleep(2)
     
    pygame.quit()
     
    quit()

epilesija_integer = 0

        
 
while True:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            #move
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                change_to = "UP"

            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                change_to = "DOWN"

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                change_to = "LEFT"

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                change_to = "RIGHT"


            #exit
            if(event.key == pygame.K_ESCAPE):
                exit()


    if (change_to == "UP" and direction != "DOWN"):
        direction = "UP"

    elif (change_to == "DOWN" and direction != "UP"):
        direction = "DOWN"

    elif (change_to == "LEFT" and direction != "RIGHT"):
        direction = "LEFT"

    elif (change_to == "RIGHT" and direction != "LEFT"):
        direction = "RIGHT"
 
    # Moving the snake
    if (direction == "UP"):
        snake_position[1] -= 10

    elif (direction == "DOWN"):
        snake_position[1] += 10

    elif (direction == "LEFT"):
        snake_position[0] -= 10

    elif (direction == "RIGHT"):
        snake_position[0] += 10
 

    snake_body.insert(0, list(snake_position))
    if (snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]):
        lucky = random.randrange(0, 10)
        if(lucky == 5):
            if(gamer_mode_b == True):
                snake_speed += 60
            score += 10
            

        else:
            if(gamer_mode_b == True):
                snake_speed += 10
            score += 1


        fruit_spawn = False


    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (x//10)) * 10,
                          random.randrange(1, (y//10)) * 10]
         
    fruit_spawn = True
    window.fill(black)
    window.blit(background, (0, 0))
     
    for pos in snake_body:
        pygame.draw.rect(window, player_color_real,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    #GameOver
    if (snake_position[0] < 0 or snake_position[0] > x-10):
        game_over()
        
    if (snake_position[1] < 0 or snake_position[1] > y-10):
        game_over()
 
    #if snake tuch self
    for block in snake_body[1:]:
        if (snake_position[0] == block[0] and snake_position[1] == block[1]):
            game_over()

    if(epilepsija_mode == True):
        if(epilesija_integer == 0):
            player_color_real = white
            epilesija_integer += 1
    
        elif(epilesija_integer == 1):
            player_color_real = red
            epilesija_integer += 1

        elif(epilesija_integer == 2):
            player_color_real= yellow
            epilesija_integer += 1

        elif(epilesija_integer == 3):
             player_color_real = blue
             epilesija_integer += 1

        elif(epilesija_integer == 4):
            player_color_real = green
            epilesija_integer = 0
        
 
    show_score(1, white, "times new roman", 20)
    pygame.display.update()
    fps.tick(snake_speed)   
