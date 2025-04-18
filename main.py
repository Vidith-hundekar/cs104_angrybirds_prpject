from game import *
from physics import *
import time

run=True
while run:
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(background,(0,0))
    screen.blit(sling,(1200,825))
    screen.blit(sling,(200,825))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse released at:", pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:             
            if event.key == pygame.K_ESCAPE:           
                run = False
        if mouse_pos[0]>150 and mouse_pos[0]<250 and mouse_pos[1]>750 and  mouse_pos[1] <900:
            print("y")
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("hi")
                x_lau_b=mouse_pos[0]
                y_lau_b=mouse_pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                print("yes")
                x_lau_a=mouse_pos[0]
                y_lau_a=mouse_pos[1]
                launch_state=True
                start_time=time.time()
    if launch_state:   
        del_x=x_lau_b-x_lau_a
        del_y=y_lau_b-y_lau_a
        red_x,red_y,Vx,Vy=launch("RED",(del_x*(1.8/50)*(1300/2.65)),(del_y*(1.8/50)*(1300/2.65)),red_x,red_y,(time.time()-start_time))
    screen.blit(red,(red_x,red_y))
    pygame.display.update()
   
pygame.quit()