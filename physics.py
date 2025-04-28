from game import *

def drag_velocity(x_lau_b,y_lau_b):
    global V_factor
    mouse_pos=pygame.mouse.get_pos()
    x_lau_a=mouse_pos[0]
    y_lau_a=mouse_pos[1]
    del_x=x_lau_b-x_lau_a
    del_y=y_lau_b-y_lau_a
    Vx=del_x*V_factor
    Vy=del_y*V_factor 
    return Vx,Vy

def launch_gravity (Vx,Vy,red_x,red_y,t,T1):
    A=600
    del_t=t-T1
    rel_x=Vx*del_t
    rel_y=Vy*del_t
    red_x+=rel_x
    red_y+=rel_y
    Vy+=A*del_t
    T1=t
    return red_x,red_y,Vx,Vy,T1

def draw_dots(screen,proj_x,proj_y,Vx,Vy,A,num,dot_size):  #proj_x=bird.center[0]  , #proj_y=bird.center[1]
    dot_list=[]
    for i in range(1,num+1):
        t=(1.5/num)*i
        dot=[None,None]
        dot[0]=Vx*t
        dot[1]=Vy*t + 0.5*A*t*t
        dot_list.append(dot)
    for dots in dot_list:
        pygame.draw.circle(screen,(255,255,255),(int(proj_x+dots[0]),int(proj_y+dots[1])),dot_size)
    
    