import pygame, handler
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    pygame.display.set_caption('space invaders')
    screen = pygame.display.set_mode((700, 700))
    background_color = (9, 2, 24)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    handler.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        handler.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            handler.update(background_color, screen, gun, aliens, bullets, stats, sc)
            handler.update_bullets(screen, aliens, bullets, stats, sc)
            handler.update_aliens(screen, gun, aliens, bullets, stats, sc)


if __name__ == '__main__':
        run()