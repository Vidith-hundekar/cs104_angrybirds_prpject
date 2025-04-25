import pygame
from resources.characters import *

pygame.init()
    

#info
info = pygame.display.Info()

# # get the default size
x, y = info.current_w, info.current_h
screen_wid,screen_height=int((9*x/10)),int((9*y/10))
screen= pygame.display.set_mode((screen_wid,screen_height))


#scaling and loading background
background =pygame.image.load('./resources/images/background1.jpeg')
# background=pygame.transform.scale(background,(1500,900))
background=pygame.transform.scale(background,(screen_wid,screen_height))


#sling
sling=pygame.image.load('./resources/images/sling.png')
# sling=pygame.transform.scale(sling,(75,75))
sling=pygame.transform.scale(sling,(int(x/20),int(y/12)))


#red
# red_b=Bird(name="RED",a=200,b=800)
red_b=Bird(name="RED",x=int((1/15)*(screen_wid)),y=int((8/9)*(screen_height)))
red_x=red_b.position[0]
red_y=red_b.position[1]
red=pygame.image.load('./resources/images/red-bird.png')
# red=pygame.transform.scale(red,(50,50))
red=pygame.transform.scale(red,(int(x/30),int(y/14)))


#launch
launch_state=False
x_lau_b=0    #before launch
x_lau_a=0    #after launch
y_lau_b=0    #before launch
y_lau_a=0    #after launch 
