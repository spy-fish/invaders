import pygame
from pygame.sprite import Sprite

class Gun(Sprite):
    # gun initialization
    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/images/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_left = False
        self.move_right = False

    # drawing gun
    def output(self):
        self.screen.blit(self.image, self.rect)

    # updating position of gun
    def update_gun(self):
        if self.move_left and self.rect.left > 0:
            self.center -= 0.7

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 0.7

        self.rect.centerx = self.center
    
    # creating gun
    def create_gun(self):
        self.center = self.screen_rect.centerx