import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, name, x, y, Vx=0, Vy=0):
        super().__init__()
        self.name = name
        self.position = [x, y]  # store position as a tuple
        self.velocity = [Vx, Vy]
        self.center = [self.position[0]+27.5, self.position[1]+27.5]
        self.count = 0
        
        # Load the appropriate bird image
        if name == "RED":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/red.png'), (55, 55))
        elif name == "CHUCKS":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/chucks.png'), (55, 55))
        elif name == "BOMB":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/Bombs.png'), (55, 55))
        elif name == "BLUE":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/blue.png'), (55, 55))
            
        self.rect = self.img.get_rect(topleft=(self.position[0], self.position[1]))

    def update(self):
        self.rect.topleft = (self.position[0], self.position[1])
        # Update center when position changes
        self.center = [self.position[0]+27.5, self.position[1]+27.5]
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def flip(self, screen):
        screen.blit(pygame.transform.flip(self.img, True, False), self.rect)
    
class Wood(pygame.sprite.Sprite):
    def __init__(self, cen_x, cen_y):
        super().__init__()
        self.health = 100
        self.position = [cen_x, cen_y] 
        
        # Load image based on health
        self.update_image()
        
        self.rect = self.img.get_rect(center=(self.position[0], self.position[1]))
        
    def update_image(self):
        if self.health >= 75:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_100.png'), (70, 70))
        elif self.health >= 50:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_75.png'), (70, 70))
        elif self.health >= 25:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_50.png'), (70, 70))
        elif self.health > 0:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_25.png'), (70, 70))
        
    def update(self):
        self.update_image()
        self.rect.center = (self.position[0], self.position[1])
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.update_image()
    
class Stone(pygame.sprite.Sprite):
    def __init__(self, cen_x, cen_y):
        super().__init__()
        self.health = 100
        self.position = [cen_x, cen_y] 
        
        # Load image based on health
        self.update_image()
        
        self.rect = self.img.get_rect(center=(self.position[0], self.position[1]))
        
    def update_image(self):
        if self.health >= 75:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_100.png'), (70, 70))
        elif self.health >= 50:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_75.png'), (70, 70))
        elif self.health >= 25:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_50.png'), (70, 70))
        elif self.health > 0:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_25.png'), (70, 70))
        
    def update(self):
        self.update_image()
        self.rect.center = (self.position[0], self.position[1])
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.update_image()
  
class Ice(pygame.sprite.Sprite):
    def __init__(self, cen_x, cen_y):
        super().__init__()
        self.health = 100
        self.position = [cen_x, cen_y] 
        
        # Load image based on health
        self.update_image()
        
        self.rect = self.img.get_rect(center=(self.position[0], self.position[1]))
        
    def update_image(self):
        if self.health >= 75:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_100.png'), (70, 70))
        elif self.health >= 50:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_75.png'), (70, 70))
        elif self.health >= 25:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_50.png'), (70, 70))
        elif self.health > 0:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_25.png'), (70, 70))
        
    def update(self):
        self.update_image() 
        self.rect.center = (self.position[0], self.position[1])
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.update_image()