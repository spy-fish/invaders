import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        # creation bullet in gun position
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 6, 10)
        self.color = 240, 98, 146
        self.speed = 10
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
    
    def update(self):
        # moving bullet up
        self.y -= self.speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        # drawing bullet
        pygame.draw.rect(self.screen, self.color, self.rect)