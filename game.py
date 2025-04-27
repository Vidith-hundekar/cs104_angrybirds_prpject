import pygame
import pygame.locals
from resources.characters import *

pygame.init()
    
run=True

clock = pygame.time.Clock()

#info
info = pygame.display.Info()

# # get the default size
x, y = info.current_w, info.current_h
screen_wid,screen_height=int((9*x/10)),int((9*y/10))
screen= pygame.display.set_mode((screen_wid,screen_height))

#UI
ui_status=True
ui_image=pygame.image.load('./resources/images/ui.png')
ui_image=pygame.transform.scale(ui_image,(screen_wid,screen_height))
font = pygame.font.SysFont("Arial", 72 , italic=True)
active = False  # Whether text input is active

#player1
p_1=False
ui_x_p1=325
ui_y_p1=150
text1=""
#player2
p_2=True
ui_x_p2=900
ui_y_p2=150
text2=""

#scaling and loading background
background =pygame.image.load('./resources/images/background3.png')
background=pygame.transform.scale(background,(screen_wid,screen_height))


#sling
sling=pygame.image.load('./resources/images/sling.png')
sling=pygame.transform.scale(sling,(int(x/20),int(y/12)))
sling_1_pos=int(((14/15)-(1/20))*(screen_wid)),int((11/12)*(screen_height))
sling_2_pos=int((1/15)*(screen_wid)),int((11/12)*(screen_height))


#red
red_b=Bird(name="RED",x=int((1/15)*(screen_wid)),y=int((8/9)*(screen_height)))
red_x=red_b.position[0]
red_y=red_b.position[1]
red=pygame.image.load('./resources/images/red-bird.png')
red=pygame.transform.scale(red,(int(x/30),int(y/14)))


#launch
launch_state=False
x_lau_b=0    #before launch
x_lau_a=0    #after launch
y_lau_b=0    #before launch
y_lau_a=0    #after launch 
