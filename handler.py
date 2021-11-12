import pygame, sys, time, main
from bullet import Bullet
from alien import Alien

# event handling
def events(screen, gun, bullets):
    for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT:
            sys.exit(0)
        
        # pressed
        elif event.type == pygame.KEYDOWN:
            # moving left
            if event.key == pygame.K_h:
                gun.move_left = True
            # moving right
            elif event.key == pygame.K_l:
                gun.move_right = True
            elif event.key == pygame.K_j:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
            
        
        # not pressed
        elif event.type == pygame.KEYUP:
            # moving left
            if event.key == pygame.K_h:
                gun.move_left = False
            # moving right
            elif event.key == pygame.K_l:
                gun.move_right = False


# screen updating
def update(background_color, screen, gun, aliens, bullets, stats, sc):
        screen.fill(background_color)
        sc.show_scores()

        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        gun.output()
        aliens.draw(screen)
        pygame.display.flip()

# updating positions of bullets
def update_bullets(screen, aliens, bullets, stats, sc):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    

    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        
        sc.image_score()
        check_high_scores(stats, sc)
        sc.image_guns()

    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)
        

# creating army of aliens
def create_army(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    num_of_aliens_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    num_of_aliens_y = int((700 - 100 - 2 * alien_height) / alien_height)

    def drawing_rows():
      for num_of_aliens in range(num_of_aliens_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * num_of_aliens
            alien.y = alien_height + alien_height * row_num
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_num
            aliens.add(alien)


    if len(sys.argv) == 2:
        for row_num in range(int(sys.argv[1])):
            drawing_rows()
    else:
        for row_num in range(num_of_aliens_y - 7):
            drawing_rows()
    

# updating aliens positions
def update_aliens(screen, gun, aliens, bullets, stats, sc):
    aliens.update()

    if pygame.sprite.spritecollideany(gun, aliens):
        gun_die(screen, gun, aliens, bullets, stats, sc)
    
    aliens_check(screen, gun, aliens, bullets, stats, sc)


# checking when army has reached the end of the screen
def aliens_check(screen, gun, aliens, bullets, stats, sc):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_die(screen, gun, aliens, bullets, stats, sc)
            break
    


# gun and army clashing
def gun_die(screen, gun, aliens, bullets, stats, sc):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        aliens.empty()
        bullets.empty()

        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        time.sleep(1)
        main.run()


# checking new hight scores
def check_high_scores(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()

        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))