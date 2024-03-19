import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600)) # flags=pygame.NOFRAME
pygame.display.set_caption('Pygame IT GAME')
icon = pygame.image.load('1337497_game_go_play_pikachu_pokemon_icon.png')
pygame.display.set_icon(icon)

running = True
while running:

    # screen.fill((0, 237, 255))

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
            