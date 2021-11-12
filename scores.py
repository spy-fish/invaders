import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    # game information
    def __init__(self, screen, stats):
        # scores
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Arial', 20)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    # text -> img
    def image_score(self):
        self.score_img = self.font.render('score: ' + str(self.stats.score), True, self.text_color, (9, 2, 24))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.screen_rect.top + 20
    
    # text -> img
    def image_high_score(self):
        self.high_score_image = self.font.render('high score: ' + str(self.stats.high_score), True, self.text_color, (9, 2, 24))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 50
        self.high_score_rect.top = 20

    # scores
    def show_scores(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)
    
    # count of lifes
    def image_guns(self):
        self.guns = Group()

        for gun_num in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 10 + gun_num * (gun.rect.width + 20)
            gun.rect.y = 10

            self.guns.add(gun)