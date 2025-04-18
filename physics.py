from game import *
T1=0
def launch (name,Ux,Uy,red_x,red_y,t):
    global T1
    if(name == "RED"):
        A=600
        Vx=Ux
        Vy=Uy +A*t
        del_t=t-T1
        rel_x=Vx*del_t
        rel_y=Vy*del_t
        red_x+=rel_x
        red_y+=rel_y
        T1=t
        return red_x,red_y,Vx,Vy