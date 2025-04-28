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