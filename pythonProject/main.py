import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fighter")

background_surface = pygame.image.load('background.png')

#player_animation
player_fight_index=0
player_walk_index=0
is_fighting = False
is_walking_right = False
is_walking_left = False
is_flipped = False # added a new variable to track the flipping
def animate_player_walk():
    global player_walk_index
    global player_walk, player_surf, is_walking_right, is_walking_left, is_flipped

    if is_walking_right:
        if player_walk_index >= 7:
            player_walk_index = 0
        player_walk_index += 0.1
        player_surf = pygame.image.load(player_walk[int(player_walk_index)])
        if is_flipped: # added a new condition to check the flipping
            player_surf = pygame.transform.flip(player_surf, True, False) # flip the surface horizontally
            is_flipped = False # reset the flipping status
    else:
        if player_walk_index >= 7 :
            player_walk_index = 0
        player_walk_index += 0.1
        player_surf = pygame.image.load(player_walk[int(player_walk_index)])
        player_surf=pygame.transform.flip(player_surf, True, False)
        if not is_flipped: # added a new condition to check the flipping
            player_surf = pygame.transform.flip(player_surf, True, False) # flip the surface horizontally
            is_flipped = True # set the flipping status

def animate_player_fight():
    global player_fight_index, player_fight, player_surf, is_fighting
    if player_fight_index >= 5:
        player_fight_index = 0
        is_fighting = False
        player_surf = pygame.image.load(player_fight[int(player_walk_index)])

    player_fight_index += 0.1
    player_surf = pygame.image.load(player_fight[int(player_fight_index)])

#image imports
player_fight=['player/fight/tile000.png', 'player/fight/tile001.png', 'player/fight/tile002.png', 'player/fight/tile003.png', 'player/fight/tile004.png', 'player/fight/tile005.png']
player_walk=['player/walk/tile000.png', 'player/walk/tile001.png', 'player/walk/tile002.png', 'player/walk/tile003.png', 'player/walk/tile004.png', 'player/walk/tile005.png', 'player/walk/tile006.png', 'player/walk/tile007.png', ]
player_surf = pygame.image.load(player_walk[player_walk_index])

#player rectangle
player_rect = player_surf.get_rect(center=(20, 430))

clock = pygame.time.Clock()

while True:
    if is_fighting:
        player_rect.x += 1
        animate_player_fight()
    if is_walking_right:
        player_rect.x += 1
        animate_player_walk()
    if is_walking_left:
        player_rect.x -= 1
        animate_player_walk()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                is_walking_right = True
            elif event.key == pygame.K_LEFT:
                is_walking_left = True
            elif event.key == pygame.K_SPACE:
                    is_fighting = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                is_walking_right=False
            elif event.key == pygame.K_LEFT:
                is_walking_left = False



    screen.blit(background_surface,(0,0))

    screen.blit(player_surf, player_rect)

    clock.tick(60)
    pygame.display.update()
