import pygame


class Alien(pygame.sprite.Sprite):
    # class of one alien
    def __init__(self, screen):
        # initialization of starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def draw(self):
        # drawing alien
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # moving aliens
        self.y += 0.05
        self.rect.y = self.y