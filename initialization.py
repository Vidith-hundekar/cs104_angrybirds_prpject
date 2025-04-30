import pygame
from characters import *
import random

pygame.init()
pygame.mixer.init()
 
#time    
run = True
clock = pygame.time.Clock()

#sound
sound=False
pygame.mixer.music.load("./resources/audio/angry_song.mpeg") 
pygame.mixer.music.play(-1) 

#info
info = pygame.display.Info()

## get the default size
x, y = info.current_w, info.current_h
screen_wid, screen_height = int((9*x/10)), int((9*y/10))
screen = pygame.display.set_mode((screen_wid, screen_height))
print(screen_wid,screen_height)

#multiplying_fac
Nx,Ny=screen_wid/1536,screen_height/960

#scaling and loading backgrounds
background1 = pygame.image.load('./resources/images/background.png')   #customization
background1 = pygame.transform.scale(background1, (screen_wid, screen_height))
background2 = pygame.image.load('./resources/images/Easy_img.png')          #easy
background2 = pygame.transform.scale(background2, (screen_wid, screen_height))
background3 = pygame.image.load('./resources/images/Med_img.png')           #hard
background3 = pygame.transform.scale(background3, (screen_wid, screen_height))
background4 = pygame.image.load('./resources/images/end.png')           #end
background4 = pygame.transform.scale(background4, (screen_wid, screen_height))

#Level
level=False
level_bac=pygame.transform.scale(pygame.image.load('./resources/images/Level.png'),(screen_wid,screen_height))
#instruction_images for all levels
level_easy=pygame.transform.scale(pygame.image.load('./resources/images/Easy.png'),(screen_wid,screen_height))
level_med=pygame.transform.scale(pygame.image.load('./resources/images/Medium.png'),(screen_wid,screen_height))
level_cus=pygame.transform.scale(pygame.image.load('./resources/images/Customization.png'),(screen_wid,screen_height))

#stage(level)
Stage=None

#UI
ui_status = True
ui_image = pygame.image.load('./resources/images/ui.png')
ui_image = pygame.transform.scale(ui_image, (screen_wid, screen_height))
font = pygame.font.SysFont("Arial", 60, italic=True)
font_e = pygame.font.SysFont("Arial", 100, italic=True)
active = False  # Whether text input is active
Name_active_p_1=False
Name_active_p_2=False
small_font= pygame.font.SysFont("Arial",50 , italic=True)
smaller_font=pygame.font.SysFont("Arial", 32, italic=True)
text3="Enter_name"
text4="Max(10 characters)"


#player1
p_1 = True
#Enter_name_condition
ui_x_p1 = 350*Nx 
ui_y_p1 = 175*Ny
na_x_p1 = 340*Nx
na_y_p1 = 145*Ny
#Actual_name
ma_x_p1 = 340*Nx
ma_y_p1 = 220*Ny
text1 = ""

    
#player2
p_2 = False 
#Enter_name_condition
ui_x_p2 = 925*Nx
ui_y_p2 = 175*Ny
na_x_p2 = 925*Nx
na_y_p2 = 145*Ny
#actual_name
ma_x_p2 = 915*Nx
ma_y_p2 = 220*Ny
text2 = ""

#customized_boxes
Boxes_p1=[[240,370],[170,370],[100,370],[100,440],[100,510],[100,580],[100,650],[170,650],[240,650],[520,370],[450,370],[380,370],[380,440],[380,510],[450,510],[520,510],[520,580],[520,650],[450,650],[380,650]]
box_obj_p1=[]
for box in Boxes_p1:
    box[0]*=Nx
    box[1]*=Ny
for box in Boxes_p1:
    fill= [Wood, Stone, Ice]
    random_selection = random.choice(fill)
    boxx=random_selection(box[0],box[1],Nx,Ny)
    box_obj_p1.append(boxx)
Boxes_p2=[[1296,370],[1366,370],[1436,370],[1436,440],[1436,510],[1436,580],[1436,650],[1366,650],[1296,650],[1016,370],[1086,370],[1156,370],[1156,440],[1156,510],[1086,510],[1016,510],[1016,580],[1016,650],[1086,650],[1156,650]]
box_obj_p2=[]
for box in Boxes_p2:
    box[0]*=Nx
    box[1]*=Ny
    
for box in Boxes_p2:
    fill= [Wood, Stone, Ice]
    random_selection = random.choice(fill)
    boxx=random_selection(box[0],box[1],Nx,Ny)
    box_obj_p2.append(boxx)
    
#easy,medium
Box_p1=[Boxes_p1[2],Boxes_p1[8],Boxes_p1[11],Boxes_p1[17]]
box_em_obj_p1=[]
for box in Boxes_p1:
    box[0]*=Nx
    box[1]*=Ny
for box in Box_p1:
    fill= [Wood, Stone, Ice]
    random_selection = random.choice(fill)
    boxx=random_selection(box[0],box[1],Nx,Ny)
    box_em_obj_p1.append(boxx)
box_em_obj_p2=[]
Box_p2=[Boxes_p2[2],Boxes_p2[8],Boxes_p2[11],Boxes_p2[17]]
for box in Box_p2:
    box[0]*=Nx
    box[1]*=Ny
for box in Box_p2:
    fill= [Wood, Stone, Ice]
    random_selection = random.choice(fill)
    boxx=random_selection(box[0],box[1],Nx,Ny)
    box_em_obj_p2.append(boxx)
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

score_p1=0
score_p2=0

Score_p1_x=648*Nx
Score_p1_y=20*Ny
Score_p2_x=830*Nx
Score_p2_y=20*Ny
font_s = pygame.font.SysFont("Arial", 48, italic=True)

