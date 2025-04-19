class Bird():
    def __init__(self,name, x, y,Vx=0,Vy=0):
        # self.life = 20# use the parameter passed
        self.position = [x,y] # store position as a tuple
        self.velocity=[Vx,Vy]