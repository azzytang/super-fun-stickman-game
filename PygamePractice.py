import pygame
from sys import exit
import random


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = stickman_font.render(
        f'Score {int(current_time/1000)}', False, 'black')
    score_rect = score_surface.get_rect(topleft=(0, 0))
    screen.blit(score_surface, score_rect)
    return int(current_time/1000)


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.height == 110:
                screen.blit(tophat_player, obstacle_rect)
            elif obstacle_rect.height == 96:
                screen.blit(girlplayer_surface, obstacle_rect)
            else:
                screen.blit(player2, obstacle_rect)
        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


pygame.init()  # initializes pygame

game_active = False
game_start = True
instructions = False
start_time = 0
highscore = 0

# set window display length and height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('MY FIRST PYGAME')  # sets the title of the window
clock = pygame.time.Clock()
stickman_font = pygame.font.Font('Stickman-Regular.ttf', 50)

title_surface = stickman_font.render("super fun stickman game", False, 'black')
title_rect = title_surface.get_rect(center=(400, 200))

happy_player = pygame.image.load('happy_player.png').convert_alpha()
happy_player_rect = happy_player.get_rect(center=(400, 100))

start_surface = stickman_font.render("click anywhere to start", False, 'black')
start_surface = pygame.transform.rotozoom(start_surface, 0, 1/2)
start_rect = start_surface.get_rect(center=(400, 300))

help_surface = stickman_font.render("press h for help", False, 'black')
help_surface = pygame.transform.rotozoom(help_surface, 0, 1/2)
help_rect = help_surface.get_rect(topleft=(10, 10))

helpback_surface = stickman_font.render("press h to go back", False, 'black')
helpback_surface = pygame.transform.rotozoom(helpback_surface, 0, 1/2)
helpback_rect = helpback_surface.get_rect(topleft=(10, 10))

instruct_title = stickman_font.render("instructions", False, 'black')
instruct_title_rect = instruct_title.get_rect(center=(400, 100))

instruct_surface = stickman_font.render(
    "pretty simple      jump over stickman      if you hit stickman game over", False, 'black')
instruct_surface = pygame.transform.rotozoom(instruct_surface, 0, 1/2)
instruct_rect = instruct_surface.get_rect(center=(400, 200))
controls_surface = stickman_font.render("controls", False, 'black')
controls_surface = pygame.transform.rotozoom(controls_surface, 0, 2/3)
controls_rect = controls_surface.get_rect(center=(100, 300))
controls2_surface = stickman_font.render(
    "to move                         to jump", False, 'black')
controls2_surface = pygame.transform.rotozoom(controls2_surface, 0, 1/2)
controls2_rect = controls2_surface.get_rect(center=(500, 300))
wasd_surface = pygame.image.load('WASD.png').convert_alpha()
wasd_rect = wasd_surface.get_rect(center=(250, 300))
spacebar_surface = pygame.image.load('spacebar.png').convert_alpha()
spacebar_rect = spacebar_surface.get_rect(center=(500, 300))

mainmenu_surface = stickman_font.render(
    "esc to go back to main menu", False, 'black')
mainmenu_surface = pygame.transform.rotozoom(mainmenu_surface, 0, .5)
mainmenu_rect = mainmenu_surface.get_rect(topright=(790, 10))
# test_surface = pygame.Surface((100, 200))  # creates a new plain surface
# test_surface.fill('gold')  # changes color

sky_surface = pygame.image.load('sky.png').convert_alpha()  # imports image
ground_surface = pygame.image.load('ground.png').convert_alpha()

player = pygame.image.load('player1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(200, 300))
player2 = pygame.image.load('player.png').convert_alpha()
player2_rect = player2.get_rect(midbottom=(400, 300))

girlplayer_surface = pygame.image.load('girlplayer.png').convert_alpha()
tophat_player = pygame.image.load('tophat_player.png').convert_alpha()

gameover_surface = stickman_font.render("game over", False, 'black')
gameover_rect = gameover_surface.get_rect(center=(400, 200))

restart_surface = stickman_font.render(
    "click anywhere to restart", False, 'black')
restart_surface = pygame.transform.rotozoom(restart_surface, 0, 1/2)
restart_rect = restart_surface.get_rect(center=(400, 300))


score = 0
player_gravity = 0

sad_player = pygame.image.load('sad_player.png').convert_alpha()
sad_player = pygame.transform.scale(sad_player, (40, 100))
sad_player_rect = sad_player.get_rect(center=(400, 100))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)
obstacle_rect_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # uninitializes pygame
            exit()  # exits code
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active and not instructions:
                game_active = True
                game_start = False
                start_time = pygame.time.get_ticks()
                player_rect.x = 100
                player_rect.bottom = 300
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300 and game_active:
                player_gravity = -20
            if event.key == pygame.K_h:
                if instructions:
                    instructions = False
                else:
                    instructions = True
            if event.key == pygame.K_ESCAPE:
                game_start = True
                game_active = False

        if event.type == obstacle_timer and game_active:
            random_num = random.randint(0, 3)
            if not random_num:
                obstacle_rect_list.append(player2.get_rect(
                    midbottom=(random.randint(900, 1100), 300)))
            elif random_num == 2:
                obstacle_rect_list.append(tophat_player.get_rect(
                    midbottom=(random.randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(girlplayer_surface.get_rect(
                    midbottom=(random.randint(900, 1100), 300)))

    if game_start:
        screen.fill('white')
        screen.blit(title_surface, title_rect)
        screen.blit(start_surface, start_rect)
        screen.blit(happy_player, happy_player_rect)
        screen.blit(help_surface, help_rect)
        obstacle_rect_list.clear()
        if instructions:
            screen.fill('white')
            screen.blit(instruct_title, instruct_title_rect)
            screen.blit(instruct_surface, instruct_rect)
            screen.blit(helpback_surface, helpback_rect)
            screen.blit(controls_surface, controls_rect)
            screen.blit(controls2_surface, controls2_rect)
            screen.blit(wasd_surface, wasd_rect)
            screen.blit(spacebar_surface, spacebar_rect)

    elif game_active:
        # places surface on display surface at (x,y)
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        score = display_score()
        # pygame.draw.rect(screen, 'Pink', text_rect)
        # pygame.draw.line(screen, (random.randint(0, 255), random.randint(
        #     0, 255), random.randint(0, 255)), (0, 0), mouse_pos, 10)
        # screen.blit(text_surface, text_rect)
        # text_rect.x += 1
        # text_rect.y += 1

        # screen.blit(player2, player2_rect)
        # player2_rect.x -= 5

        screen.blit(player, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        # if player2_rect.x < -50:
        #     player2_rect.x = random.randint(400, 800)

        game_active = collisions(player_rect, obstacle_rect_list)

        if player_rect.x < -50:
            score += 100
            player_rect.x = 500

        # if player_rect.colliderect(player2_rect):
        #     game_active = False

        # if player_rect.collidepoint(mouse_pos):
        #     if pygame.mouse.get_pressed()[0]:
        #         player2_rect.x += 10
        #     if pygame.mouse.get_pressed()[2]:
        #         print("you right clicked the player!")

        keys = pygame.key.get_pressed()

        # if keys[pygame.K_SPACE]:
        #     score += 2

        if keys[pygame.K_a] and player_rect.x > 0:
            player_rect.x -= 4
        if keys[pygame.K_d] and player_rect.x < 400:
            player_rect.x += 4
    else:
        screen.fill('white')
        screen.blit(gameover_surface, gameover_rect)
        screen.blit(restart_surface, restart_rect)
        screen.blit(sad_player, sad_player_rect)
        score_message = stickman_font.render(
            f"your score is {score}", False, 'black')
        score_message = pygame.transform.rotozoom(score_message, 0, 1/2)
        score_rect = score_message.get_rect(center=(400, 250))
        highscore = max(highscore, score)
        highscore_message = stickman_font.render(
            f"your highscore is {highscore}", False, 'black')
        highscore_message = pygame.transform.rotozoom(
            highscore_message, 0, 1/2)
        highscore_rect = highscore_message.get_rect(topleft=(10, 10))
        screen.blit(score_message, score_rect)
        screen.blit(highscore_message, highscore_rect)
        screen.blit(mainmenu_surface, mainmenu_rect)
        obstacle_rect_list.clear()

    pygame.display.update()
    clock.tick(60)  # max frame rate
