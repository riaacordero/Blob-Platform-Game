"""
This module loads images.
"""

import pygame.image
import pygame.transform

bg_img = pygame.image.load('assets/img/bg_img.png')
bg_game_over_img = pygame.image.load("assets/img/bg_img.png")
bg_game_clear_img = pygame.image.load("assets/img/bg_img.png")
bg_level_img = pygame.image.load("assets/img/bg_img.png")

game_over_img = pygame.image.load("assets/img/game_over.png")
death_img = pygame.image.load("assets/img/dead.png")
pause_img = pygame.transform.scale(pygame.image.load("assets/img/pause.png"), (35, 35))
pause_hov_img = pygame.transform.scale(pygame.image.load("assets/img/pause_hov.png"), (35, 35))

enemy_img = pygame.image.load("assets/img/enemy.png")
gem_img = pygame.transform.scale(pygame.image.load("assets/img/gem.png"), (35, 35))
key_img = pygame.transform.scale(pygame.image.load("assets/img/key.png"), (35, 35))
key_inactive = pygame.transform.scale(pygame.image.load("assets/img/key_mono.png"), (35, 35))
door_img = pygame.image.load("assets/img/door.png")
platform_img = pygame.image.load("assets/img/ground.png")
fireball_img = pygame.image.load("assets/img/ball-atk.png")

potion_blue_img = pygame.image.load("assets/img/potion-blue.png")
potion_red_img = pygame.image.load("assets/img/potion-red.png")
potion_yellow_img = pygame.image.load("assets/img/potion-yellow.png")

player_default_left_images = []
player_default_right_images = []
player_atk_left_images = []
player_atk_right_images = []
player_health_left_images = []
player_health_right_images = []
player_jump_left_images = []
player_jump_right_images = []

player_size = (40, 40)
for num in range(1, 4):
    player_img = pygame.image.load(f"assets/img/player/player-{num}.png")
    player_right_img = pygame.transform.scale(player_img, player_size)
    player_left_img = pygame.transform.flip(player_right_img, True, False)
    player_default_right_images.append(player_right_img)
    player_default_left_images.append(player_left_img)

    player_atk_img = pygame.image.load(f"assets/img/player/player-atk-{num}.png")
    player_atk_right_img = pygame.transform.scale(player_atk_img, player_size)
    player_atk_left_img = pygame.transform.flip(player_atk_right_img, True, False)
    player_atk_right_images.append(player_atk_right_img)
    player_atk_left_images.append(player_atk_left_img)

    player_health_img = pygame.image.load(f"assets/img/player/player-health-{num}.png")
    player_health_right_img = pygame.transform.scale(player_health_img, player_size)
    player_health_left_img = pygame.transform.flip(player_health_right_img, True, False)
    player_health_right_images.append(player_health_right_img)
    player_health_left_images.append(player_health_left_img)

    player_jump_img = pygame.image.load(f"assets/img/player/player-jump-{num}.png")
    player_jump_right_img = pygame.transform.scale(player_jump_img, player_size)
    player_jump_left_img = pygame.transform.flip(player_jump_right_img, True, False)
    player_jump_left_images.append(player_jump_left_img)
    player_jump_right_images.append(player_jump_right_img)
