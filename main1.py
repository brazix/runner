import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
music = pygame.mixer.music.load('audio/music.wav')
pygame.mixer.music.play(-1)

#in game screen

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
#text_surface = test_font.render('Click space to jump', False, (201, 132, 71))
#text_rect = text_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(topleft = (850, 265) )

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(topleft = (50, 218))
player_gravity = 0

snail_speed = 10

score = 0

#score_surface = test_font.render(str(score), False, (201, 132, 71))
#score_rect = score_surface.get_rect(center = (400,50))

#game over screen

gameover_surface = test_font.render('Game over...', False, (201, 132, 71))
gameover_rect = gameover_surface.get_rect(center = (400,50))
playagain_surface = test_font.render('> Play again <', False, (201, 132, 71))
playagain_rect = playagain_surface.get_rect(center = (400,200))




while True:
    score_surface = test_font.render(str(score), False, (201, 132, 71))
    score_rect = score_surface.get_rect(center=(400, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playagain_rect.collidepoint(event.pos):
                    game_active = True
                    score = 0
            snail_rect.left = 800
            snail_speed = 10


    if snail_rect.left<-80 :
        snail_rect.left = 850
        snail_speed += 1.5
        score += 1




    if game_active == True:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, (96, 209, 92), score_rect)
        pygame.draw.rect(screen, (96, 209, 92), score_rect, 10)
        screen.blit(score_surface, score_rect)
        screen.blit(snail_surface, snail_rect)
        screen.blit(player_surface, player_rect)


        snail_rect.left -= snail_speed


        player_gravity +=1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(gameover_surface, gameover_rect)
        screen.blit(playagain_surface, playagain_rect)
        screen.blit(score_surface, (400, 125))


    pygame.display.update()
    clock.tick(60)

