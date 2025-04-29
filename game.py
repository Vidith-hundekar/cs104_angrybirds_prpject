import pygame
from resources.characters import *
import random

pygame.init()
pygame.mixer.init()
 
#time    
run = True
clock = pygame.time.Clock()

#
sound=False
sound_on=pygame.transform.scale(pygame.image.load('./resources/images/sound_on.png'),(40,40))
sound_off=pygame.transform.scale(pygame.image.load('./resources/images/sound_off.png'),(40,40))
pygame.mixer.music.load("angry_song.mpeg")  # Replace with your music file

# Play background music
pygame.mixer.music.play(-1)  # Loop indefinitely

#info
info = pygame.display.Info()

## get the default size
x, y = info.current_w, info.current_h
screen_wid, screen_height = int((9*x/10)), int((9*y/10))
screen = pygame.display.set_mode((screen_wid, screen_height))
print(screen_wid,screen_height)

#mul_fac
Nx,Ny=screen_wid/1536,screen_height/960

#scaling and loading background
background = pygame.image.load('./resources/images/background.png')
background = pygame.transform.scale(background, (screen_wid, screen_height))

#UI
ui_status = True
ui_image = pygame.image.load('./resources/images/ui.png')
ui_image = pygame.transform.scale(ui_image, (screen_wid, screen_height))
font = pygame.font.SysFont("Arial", 64, italic=True)
active = False  # Whether text input is active
Name_active_p_1=False
Name_active_p_2=False
small_font= pygame.font.SysFont("Arial",50 , italic=True)
smaller_font=pygame.font.SysFont("Arial", 32, italic=True)
text3="Enter_name"
text4="Max(10 characters)"


#player1
p_1 = True
ui_x_p1 = 350*Nx
ui_y_p1 = 175*Ny
na_x_p1 = 350*Nx
na_y_p1 = 145*Ny
ma_x_p1 = 340*Nx
ma_y_p1 = 220*Ny
text1 = ""
Boxes_p1=[[240,370],[170,370],[100,370],[100,440],[100,510],[100,580],[100,650],[170,650],[240,650],[520,370],[450,370],[380,370],[380,440],[380,510],[450,510],[520,510],[520,580],[520,650],[450,650],[380,650]]
box_obj_p1=[]
for box in Boxes_p1:
    box[0]*=Nx
    box[1]*=Ny
for box in Boxes_p1:
    fill= [Wood, Stone, Ice]
    random_selection = random.choice(fill)
    boxx=random_selection(box[0],box[1])
    box_obj_p1.append(boxx)
    
#player2
p_2 = False 
ui_x_p2 = 925*Nx
ui_y_p2 = 175*Ny
na_x_p2 = 925*Nx
na_y_p2 = 145*Ny
ma_x_p2 = 915*Nx
ma_y_p2 = 220*Ny
text2 = ""
Boxes_p2=[[1296,370],[1366,370],[1436,370],[1436,440],[1436,510],[1436,580],[1436,650],[1366,650],[1296,650],[1016,370],[1086,370],[1156,370],[1156,440],[1156,510],[1086,510],[1016,510],[1016,580],[1016,650],[1086,650],[1156,650]]
box_obj_p2=[]
for box in Boxes_p2:
    box[0]*=Nx
    box[1]*=Ny
    
for box in Boxes_p2:
    fill= [Wood, Stone, Ice]
    random_selection = random.choice(fill)
    boxx=random_selection(box[0],box[1])
    box_obj_p2.append(boxx)
    
#sling
sling = pygame.image.load('./resources/images/sling.png')
sling = pygame.transform.scale(sling, (int(x/20), int(y/12)))
sling_1_pos = int(((14/15)-(1/20))*(screen_wid)), int((11/12)*(screen_height))
sling_2_pos = int((1/15)*(screen_wid)), int((11/12)*(screen_height))

#Flying_bird
Visible = False
slin1_bird_x = int((1/15)*(screen_wid))
slin1_bird_y = int((8/9)*(screen_height))
slin2_bird_x = int((89/100)*(screen_wid))
slin2_bird_y = int((8/9)*(screen_height))

#launch_variables
launch_state = False
flying = False
V_factor = (2.3/50)*(1300/2.65)
x_lau_b = 0    #before launch
x_lau_a = 0    #after launch
y_lau_b = 0    #before launch
y_lau_a = 0    #after launch 

#random generation
rand_birds_p1 = ["RED", "CHUCKS", "BOMB", "BLUE"]
random.shuffle(rand_birds_p1)
rand_birds_p2 = ["RED", "CHUCKS", "BOMB", "BLUE"]
random.shuffle(rand_birds_p2)

# deck_to_choose
bird_sprites_p1 = []
for i in range(4):
    bird_sprites_p1.append(None)
    
bird_sprites_p2 = []
for i in range(4):
    bird_sprites_p2.append(None)

#to regenerate bird objects
birds_update = True

#path_traj
dots_path = False

#collision
collide_list=[]
iscol=False