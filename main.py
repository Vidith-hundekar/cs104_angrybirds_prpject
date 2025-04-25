from game import *
from physics import *
import time

run=True
while run:
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(background,(0,0))
    screen.blit(sling,(int(((14/15)-(1/20))*(screen_wid)),int((11/12)*(screen_height))))
    screen.blit(sling,(int((1/15)*(screen_wid)),int((11/12)*(screen_height))))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse released at:", pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:             
            if event.key == pygame.K_ESCAPE:           
                run = False
        if mouse_pos[0] > screen_wid/30 and mouse_pos[0] < screen_wid*2/15 and mouse_pos[1] > (7/9)*(screen_height) and  mouse_pos[1] < screen_height: 
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
                del_x=x_lau_b-x_lau_a
                del_y=y_lau_b-y_lau_a
                Vx=del_x*(2.3/50)*(1300/2.65)
                Vy=del_y*(2.3/50)*(1300/2.65)
                
    if launch_state:   
        t=time.time()-start_time
        if(red_y>screen_height - ((y/14)*4/5)):
            if(Vy>0):
                Vy*=-0.8
        if (red_x<=-(x/150) and Vx <0 ) or (red_x >= screen_wid -((x/30)*4/5) and Vx>0):
            Vx*=-0.8
        red_x,red_y,Vx,Vy=launch("RED",Vx,Vy,red_x,red_y,t)
    screen.blit(red,(red_x,red_y))
    red_b.position[0]=red_x
    red_b.position[1]=red_y
    pygame.display.update()
   
pygame.quit()