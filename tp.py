import pygame
import random

pygame.init()

info = pygame.display.Info()

# # get the default size
x, y = info.current_w, info.current_h
screen_wid,screen_height=int((9*x/10)),int((9*y/10))
screen= pygame.display.set_mode((screen_wid,screen_height))

#scaling and loading background
background =pygame.image.load('./resources/images/background.png')
background=pygame.transform.scale(background,(screen_wid,screen_height))
run=True
#random generation

print(selected)

while(run):
    screen.blit(background, (0, 0))  # Pass the surface and a tuple for position
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                run=False         
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())    
    pygame.display.update()
pygame.quit()