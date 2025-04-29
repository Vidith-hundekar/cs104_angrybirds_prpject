import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, name, Nx, Ny, x, y, Vx=0, Vy=0):
        super().__init__()
        self.name = name
        self.position = [x, y]  # store position as a tuple
        self.velocity = [Vx, Vy]
        self.Nx = Nx  # Store scaling factors
        self.Ny = Ny
        self.size = (55*Nx, 55*Ny)  # Store bird size
        self.center = [self.position[0] + self.size[0]/2, self.position[1] + self.size[1]/2]
        self.count = 0
        
        # Load the appropriate bird image
        if name == "RED":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/red.png'), self.size)
        elif name == "CHUCKS":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/chucks.png'), self.size)
        elif name == "BOMB":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/Bombs.png'), self.size)
        elif name == "BLUE":
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/blue.png'), self.size)
            
        self.rect = self.img.get_rect(topleft=(self.position[0], self.position[1]))
        # Create a proper collision rect that scales with screen size
        self.collision_rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def update(self, Nx, Ny):
        self.rect.topleft = (self.position[0], self.position[1])
        # Update collision rect
        self.collision_rect.topleft = (self.position[0], self.position[1])
        # Update center when position changes
        self.center = [self.position[0] + self.size[0]/2, self.position[1] + self.size[1]/2]
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def flip(self, screen):
        screen.blit(pygame.transform.flip(self.img, True, False), self.rect)
    
class Wood(pygame.sprite.Sprite):
    def __init__(self, cen_x, cen_y, Nx, Ny):
        super().__init__()
        self.health = 100
        self.position = [cen_x, cen_y] 
        self.Nx = Nx  # Store scaling factors as object properties
        self.Ny = Ny
        self.size = (70*Nx, 70*Ny)  # Store obstacle size
        
        # Load image based on health
        self.update_image()
        
        self.rect = self.img.get_rect(center=(self.position[0], self.position[1]))
        # Create proper collision rect that scales with screen size
        self.collision_rect = pygame.Rect(
            self.position[0] - self.size[0]/2,
            self.position[1] - self.size[1]/2,
            self.size[0],
            self.size[1]
        )
        
    def update_image(self):
        if self.health > 75:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_100.png'), self.size)
        elif self.health > 50:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_75.png'), self.size)
        elif self.health > 25:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_50.png'), self.size)
        elif self.health > 0:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/wood_25.png'), self.size)
        
    def update(self, Nx, Ny):
        self.update_image()
        self.rect.center = (self.position[0], self.position[1])
        # Update collision rect
        self.collision_rect.x = self.position[0] - self.size[0]/2
        self.collision_rect.y = self.position[1] - self.size[1]/2
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def damage(self, amount, Nx, Ny):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.update_image()
    
class Stone(pygame.sprite.Sprite):
    def __init__(self, cen_x, cen_y, Nx, Ny):
        super().__init__()
        self.health = 100
        self.position = [cen_x, cen_y]
        self.Nx = Nx  # Store scaling factors as object properties
        self.Ny = Ny
        self.size = (70*Nx, 70*Ny)  # Store obstacle size
        
        # Load image based on health
        self.update_image()
        
        self.rect = self.img.get_rect(center=(self.position[0], self.position[1]))
        # Create proper collision rect that scales with screen size
        self.collision_rect = pygame.Rect(
            self.position[0] - self.size[0]/2,
            self.position[1] - self.size[1]/2,
            self.size[0],
            self.size[1]
        )
        
    def update_image(self):
        if self.health > 75:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_100.png'), self.size)
        elif self.health > 50:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_75.png'), self.size)
        elif self.health > 25:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_50.png'), self.size)
        elif self.health > 0:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/stone_25.png'), self.size)
        
    def update(self, Nx, Ny):
        self.update_image()
        self.rect.center = (self.position[0], self.position[1])
        # Update collision rect
        self.collision_rect.x = self.position[0] - self.size[0]/2
        self.collision_rect.y = self.position[1] - self.size[1]/2
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def damage(self, amount, Nx, Ny):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.update_image()
  
class Ice(pygame.sprite.Sprite):
    def __init__(self, cen_x, cen_y, Nx, Ny):
        super().__init__()
        self.health = 100
        self.position = [cen_x, cen_y]
        self.Nx = Nx  # Store scaling factors as object properties
        self.Ny = Ny
        self.size = (70*Nx, 70*Ny)  # Store obstacle size
        
        # Load image based on health
        self.update_image()
        
        self.rect = self.img.get_rect(center=(self.position[0], self.position[1]))
        # Create proper collision rect that scales with screen size
        self.collision_rect = pygame.Rect(
            self.position[0] - self.size[0]/2,
            self.position[1] - self.size[1]/2,
            self.size[0],
            self.size[1]
        )
        
    def update_image(self):
        if self.health > 75:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_100.png'), self.size)
        elif self.health > 50:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_75.png'), self.size)
        elif self.health > 25:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_50.png'), self.size)
        elif self.health > 0:
            self.img = pygame.transform.scale(pygame.image.load('./resources/images/ice_25.png'), self.size)
        
    def update(self, Nx, Ny):
        self.update_image() 
        self.rect.center = (self.position[0], self.position[1])
        # Update collision rect
        self.collision_rect.x = self.position[0] - self.size[0]/2
        self.collision_rect.y = self.position[1] - self.size[1]/2
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def damage(self, amount, Nx, Ny):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.update_image()