import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

player_surf = pygame.image.load("graphics/Player/player_walk_1.png")
player_rect = player_surf.get_rect(midbottom = (100,300))
snail_surf = pygame.image.load("graphics/snail/snail1.png")
snail_rect = snail_surf.get_rect(midbottom = (700,300))
tile_surf = pygame.image.load("graphics/tile.jpeg")
tile_rect = tile_surf.get_rect(midbottom= (400,200))


snail_speed = 5
player_gravity = 0
game_active = True
player_speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
                elif event.key == pygame.K_RIGHT:
                    player_rect.right += player_speed
                elif event.key == pygame.K_LEFT:
                    player_rect.left -= player_speed


    if game_active == True:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        screen.blit(player_surf, player_rect)
        screen.blit(snail_surf, snail_rect)
        screen.blit(tile_surf, tile_rect)
    else:
        screen.fill((119, 172, 237))



    player_gravity += 1
    player_rect.bottom += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    snail_rect.left -= snail_speed
    if snail_rect.right <= 0:
        snail_rect.left = 810

    if player_rect.bottom >= snail_rect.top and player_rect.bottom <= snail_rect.bottom:
        screen.fill('Red')

    if player_rect.colliderect(snail_rect):
        game_active = False


    pygame.display.update()
    clock.tick(60)
