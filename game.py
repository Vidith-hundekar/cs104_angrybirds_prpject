import pygame
from resources.characters import *

pygame.init()
    
#setting screen size
screen = pygame.display.set_mode((1500,900))

#scaling and loading background
background =pygame.image.load('./resources/images/background1.jpeg')
background=pygame.transform.scale(background,(1500,900))

#sling
sling=pygame.image.load('./resources/images/sling.png')
sling=pygame.transform.scale(sling,(75,75))

#red
red_b=Bird(name="RED",x=200,y=800)
red_x=red_b.position[0]
red_y=red_b.position[1]
red=pygame.image.load('./resources/images/red-bird.png')
red=pygame.transform.scale(red,(50,50))

#launch
launch_state=False
x_lau_b=0    #before launch
x_lau_a=0    #after launch
y_lau_b=0    #before launch
y_lau_a=0    #after launch 
