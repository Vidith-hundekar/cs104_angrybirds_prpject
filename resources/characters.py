import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self,name, x, y,Vx=0,Vy=0):
        super().__init__()
        # self.life = 20# use the parameter passed
        self.name=name
        self.position = [x,y] # store position as a tuple
        self.velocity=[Vx,Vy]
        self.center=[self.position[0]+27.5,self.position[1]+27.5]
        if name=="RED":
            self.img=pygame.transform.scale(pygame.image.load('./resources/images/red.png'),(55,55))
        if name=="CHUCKS":
            self.img=pygame.transform.scale(pygame.image.load('./resources/images/chucks.png'),(55,55))
        if name=="BOMB":
            self.img=pygame.transform.scale(pygame.image.load('./resources/images/Bombs.png'),(55,55))
        if name=="BLUE":
            self.img=pygame.transform.scale(pygame.image.load('./resources/images/blue.png'),(55,55))
        self.rect=self.img.get_rect(topleft=(self.position[0],self.position[1]))

    def update(self):
        self.rect.topleft=(self.position[0],self.position[1])
        
    def draw ( self, screen):
        screen.blit(self.img,self.rect)
        
    def flip(self,screen):
        screen.blit(pygame.transform.flip(self.img,True,False),self.rect)
    