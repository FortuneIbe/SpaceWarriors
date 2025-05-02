import pygame
from pygame.locals import *
import random
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Warriors')
icon = pygame.image.load('Player 1.png')
pygame.display.set_icon(icon)

welcome_page = pygame.image.load('Spaceship.png')

level_1_background = pygame.image.load('Level 1.png')
level_2_background = pygame.image.load('Level 2.png')
level_3_background = pygame.image.load('Level 3.png')
instructions = pygame.image.load('Instructions.png')

title = pygame.image.load('Space Warriors.png')
click_space = pygame.image.load('click space.png')
to_play = pygame.image.load('to play.png')
font = pygame.font.Font('Robot Monster Italic.ttf', 32)

player_one = pygame.image.load('Player 1.png')
player_one_X = 400
player_one_Y = 400
player_one_X_change = 0
player_one_Y_change = 0

player_two = pygame.image.load('Player 2.png')
player_two_X = 300
player_two_Y = 400
player_two_X_change = 0
player_two_Y_change = 0

score_value_player_one = 0
score_value_player_two = 0
player_one_overall = 0
player_two_overall = 0

field1 = [None]
field2 = [None]
field3 = [None]
field4 = [None]

starts = True
winner_score = field1

starImg = []
star_X = []
star_Y = []
star_X_change = []
star_Y_change = []
num_of_stars = 50

planetImg = []
planet_X = []
planet_Y = []
planet_X_change = []
planet_Y_change = []
num_of_planets = 15

for i in range(num_of_stars):
    starImg.append(pygame.image.load('star.png'))
    star_X.append(random.randint(0, 735))  #loads stars in random places everytime it plays
    star_Y.append(random.randint(25, 535))
    star_X_change.append(2)
    star_Y_change.append(40)

for i in range(num_of_planets):
    planetImg.append(pygame.image.load('planet.png'))
    planet_X.append(random.randint(0, 735))  #loads planet in random places everytime it plays
    planet_Y.append(random.randint(25, 535))
    planet_X_change.append(2)
    planet_Y_change.append(40)

def stars(x, y, i):
    screen.blit(starImg[i], (x, y))

def planets(x, y, i):
    screen.blit(planetImg[i], (x, y))

def player_one_start_position(x, y):
    screen.blit(player_one, (x, y))

def player_two_start_position(x, y):
    screen.blit(player_two, (x, y))

def space_warrior_title():
    screen.blit(title, (50, 100))
    screen.blit(click_space, (200, 300))
    screen.blit(to_play, (410, 300))

def show_score_one(x, y):
    score = font.render("Score: " + str(score_value_player_one), True, (0, 0, 0))
    screen.blit(score, (x, y))

text_player_one_X = 50
text_player_one_Y = 10

def hide_score_one(x,y):
    score = font.render(" ", True, (0, 0, 0))
    screen.blit(score, (x, y))

def show_score_two(x, y):
    score = font.render("Score: " + str(score_value_player_two), True, (0, 0, 0))
    screen.blit(score, (x, y))

text_player_two_X = 595
text_player_two_Y = 10

def hide_score_two(x,y):
    score = font.render(" ", True, (0, 0, 0))
    screen.blit(score, (x, y))

def Collison_Player_One(player_one_X, player_one_Y, star_X, star_Y): #distance formula calulate distance from player one and the stars
    distance = math.sqrt((math.pow(player_one_X - star_X, 2)) + (math.pow(player_one_Y - star_Y, 2)))
    if distance < 27:
        return True
    else:
        return False

def Collison_Player_Two(player_two_X, player_two_Y, star_X, star_Y): #distance formula calulate distance from player two and the stars
    distance = math.sqrt((math.pow(player_two_X - star_X, 2)) + (math.pow(player_two_Y - star_Y, 2)))
    if distance < 27:
        return True
    else:
        return False

missle_one_Img = pygame.image.load('missile.png') # Player One's Missile
missle_one_X = 0
missle_one_Y = 480
missle_one_X_change = 0
missle_one_Y_change = 15
missle_one_state = "ready"

def fire_one_missle(x, y): #Firing Player One's Missile
    global missle_one_state
    missle_one_state = "fire"
    screen.blit(missle_one_Img, (x, y))

missle_two_Img = pygame.image.load('missile.png') #Player Two's Missile
missle_two_X = 0
missle_two_Y = 480
missle_two_X_change = 0
missle_two_Y_change = 15
missle_two_state = "ready"

def fire_two_missle(x, y): #Firing Player Two's Missile
    global missle_two_state
    missle_two_state = "fire"
    screen.blit(missle_two_Img, (x, y))

def bullet_one_collison(player_one_X, player_one_Y, missle_one_X, missle_one_Y): # Collision with Player One's Missile
    distance = math.sqrt((math.pow(player_one_X - missle_one_X, 2)) + (math.pow(player_one_Y - missle_one_Y, 2)))
    if distance < 27:
        return True
    else:
        return False

def bullet_two_collison(player_two_X, player_two_Y, missle_two_X, missle_two_Y): # Collision with Player Two's Missile
    distance = math.sqrt((math.pow(player_two_X - missle_two_X, 2)) + (math.pow(player_two_Y - missle_two_Y, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(welcome_page, (0, 0))
    space_warrior_title()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  #Instructions Page
                field1[0] = instructions
            if event.key == pygame.K_1:      #Switch to Level One
                field2[0] = level_1_background
                starts = False
                winner_score = field2
            if event.key == pygame.K_2:      #Switch to Level Two
                field3[0] = level_2_background
                starts = False
                winner_score = field3
                score_value_player_one = 0
                score_value_player_two = 0
            if event.key == pygame.K_3:       #Switch to Level Three
                field4[0] = level_3_background
                starts = False
                winner_score = field4
                score_value_player_one = 0
                score_value_player_two = 0
            if event.key == pygame.K_RCTRL:
                if missle_one_state == "ready":
                    missle_one_X = player_one_X
                    missle_one_Y = player_one_Y
                    fire_one_missle(missle_one_X, missle_one_Y)
            if event.key == pygame.K_CAPSLOCK:
                if missle_two_state == "ready":
                    missle_two_X = player_two_X
                    missle_two_Y = player_two_Y
                    fire_two_missle(missle_two_X, missle_two_Y)

            #Player One & Two Movements
            if event.key == pygame.K_LEFT:
                player_one_X_change = -15
            if event.key == pygame.K_RIGHT:
                player_one_X_change = 15
            if event.key == pygame.K_DOWN:
                player_one_Y_change = 15
            if event.key == pygame.K_UP:
                player_one_Y_change = -15
            if event.key == pygame.K_a:
                player_two_X_change = -15
            if event.key == pygame.K_d:
                player_two_X_change = 15
            if event.key == pygame.K_s:
                player_two_Y_change = 15
            if event.key == pygame.K_w:
                player_two_Y_change = -15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_one_X_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_one_Y_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_two_X_change = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player_two_Y_change = 0

    player_one_X += player_one_X_change
    player_one_Y += player_one_Y_change
    player_two_X += player_two_X_change
    player_two_Y += player_two_Y_change

    #Helps Switch Levels
    for i, img in enumerate(field1):
        if img:
            column = i % 3
            row = i // 3
            screen.blit(img, (column, row))
    for i, img in enumerate(field2):
        if img:
            column = i % 3
            row = i // 3
            screen.blit(img, (column, row))
    for i, img in enumerate(field3):
        if img:
            column = i % 3
            row = i // 3
            screen.blit(img, (column, row))
    for i, img in enumerate(field4):
        if img:
            column = i % 3
            row = i // 3
            screen.blit(img, (column, row))

    #Player one boundary
    if player_one_X <= 0:
        player_one_X = 0
    elif player_one_X >= 736:
        player_one_X = 736
    if player_one_Y <= 0:
        player_one_Y = 0
    elif player_one_Y >= 536:
        player_one_Y = 536

    #Player two boundary
    if player_two_X <= 0:
        player_two_X = 0
    elif player_two_X >= 736:
        player_two_X = 736
    if player_two_Y <= 0:
        player_two_Y = 0
    elif player_two_Y >= 536:
        player_two_Y = 536

    #Collisions of players and stars moves stars when collided
    for i in range(num_of_stars):
        if starts == False:
            collision_player_one = Collison_Player_One(player_one_X, player_one_Y, star_X[i], star_Y[i])
            collision_player_two = Collison_Player_Two(player_two_X, player_two_Y, star_X[i], star_Y[i])
            if collision_player_one:
                score_value_player_one += 1
                star_X[i] = random.randint(0, 735)
                star_Y[i] = random.randint(25, 535)
            if collision_player_two:
                score_value_player_two += 1
                star_X[i] = random.randint(0, 735)
                star_Y[i] = random.randint(25, 535)
            stars(star_X[i], star_Y[i], i) # Makes sure stars show up

        else:# Moves stars away from display
            x = 1000
            y = 1000
            stars(x,y,i)

    for i in range(num_of_planets): # Collisions of players and stars moves planets when collided and decrease players scores
        if winner_score == field4:
            if starts == False:
                planet_X[i] += planet_X_change[i]

                if planet_X[i] <= 0:
                    planet_X_change[i] = 10
                    planet_Y[i] += planet_Y_change[i]  # move the planets down
                elif planet_X[i] >= 736:
                    planet_X_change[i] = -10
                    planet_Y[i] += planet_Y_change[i]
                if planet_Y[i] >= 536:
                    planet_X[i] = random.randint(0, 735)
                    planet_Y[i] = random.randint(25, 350)

                collision_player_one = Collison_Player_One(player_one_X, player_one_Y, planet_X[i], planet_Y[i])
                collision_player_two = Collison_Player_Two(player_two_X, player_two_Y, planet_X[i], planet_Y[i])
                if collision_player_one:
                    score_value_player_one -= 1
                    planet_X[i] = random.randint(0, 735)
                    planet_Y[i] = random.randint(25, 535)
                if collision_player_two:
                    score_value_player_two -= 1
                    planet_X[i] = random.randint(0, 735)
                    planet_Y[i] = random.randint(25, 535)

                planets(planet_X[i], planet_Y[i], i) # Makes sure planets show up

        else: # Moves stars away from display
            x = 1000
            y = 1000
            planets(x,y,i)

    # Will show who wins and prompt user to move to next level
    if (score_value_player_one == 100 or score_value_player_two == 100) and winner_score == field2:
        starts = True
        winner_font = pygame.font.Font('Robot Monster Italic.ttf', 64)
        if score_value_player_one > score_value_player_two:
            winner = winner_font.render("WINNER PLAYER ONE ", True, (255, 255, 255))
            click = winner_font.render("Click two to continue ", True, (0, 0, 0))
            screen.blit(winner, (80, 200))
            screen.blit(click, (30, 250))
            show_score_one(text_player_one_X, text_player_one_Y)
            show_score_two(text_player_two_X, text_player_one_Y)
        if score_value_player_two > score_value_player_one:
            winner = winner_font.render("WINNER PLAYER TWO ", True, (255, 255, 255))
            click = winner_font.render("Click two to continue ", True, (0, 0, 0))
            screen.blit(winner, (80, 200))
            screen.blit(click, (30, 250))
            show_score_one(text_player_one_X, text_player_one_Y)
            show_score_two(text_player_two_X, text_player_one_Y)
    if (score_value_player_one == 100 or score_value_player_two == 100) and winner_score == field3:
        starts = True
        winner_font = pygame.font.Font('Robot Monster Italic.ttf', 64)
        if score_value_player_one > score_value_player_two:
            player_one_overall += 1
            winner = winner_font.render("WINNER PLAYER ONE ", True, (255, 255, 255))
            click = winner_font.render("Click three to continue ", True, (0, 0, 0))
            screen.blit(winner, (80, 200))
            screen.blit(click, (0, 250))
            show_score_one(text_player_one_X, text_player_one_Y)
            show_score_two(text_player_two_X, text_player_one_Y)
        if score_value_player_two > score_value_player_one:
            winner = winner_font.render("WINNER PLAYER TWO ", True, (255, 255, 255))
            click = winner_font.render("Click three to continue ", True, (0, 0, 0))
            screen.blit(winner, (80, 200))
            screen.blit(click, (0, 250))
            show_score_one(text_player_one_X, text_player_one_Y)
            show_score_two(text_player_two_X, text_player_one_Y)
    if (score_value_player_one == 100 or score_value_player_two == 100) and winner_score == field4:
        starts = True
        winner_font = pygame.font.Font('Robot Monster Italic.ttf', 64)
        if score_value_player_one > score_value_player_two:
            winner = winner_font.render("WINNER PLAYER ONE ", True, (255, 255, 255))
            click = winner_font.render("Thanks for playing bye ", True, (0, 0, 0))
            screen.blit(winner, (80, 200))
            screen.blit(click, (0, 250))
            show_score_one(text_player_one_X, text_player_one_Y)
            show_score_two(text_player_two_X, text_player_one_Y)
        if score_value_player_two > score_value_player_one:
            winner = winner_font.render("WINNER PLAYER TWO ", True, (255, 255, 255))
            click = winner_font.render("Thanks for playing bye ", True, (0, 0, 0))
            screen.blit(winner, (80, 200))
            screen.blit(click, (0, 250))
            show_score_one(text_player_one_X, text_player_one_Y)
            show_score_two(text_player_two_X, text_player_one_Y)


    if starts == False: # Shows Scores/ Hide Score if starts == True
        show_score_one(text_player_one_X, text_player_one_Y)
        show_score_two(text_player_two_X, text_player_one_Y)

    if winner_score == field3 or winner_score == field4:
    # Bullet Collsion with player two
        player_one_collision = bullet_one_collison(player_two_X, player_two_Y, missle_one_X, missle_one_Y)
        if player_one_collision:
            missle_one_Y = 480
            missle_one_state = "ready"
            score_value_player_one += 1
            score_value_player_two -= 1

    # Bullet Collsion with player one
        player_two_collision = bullet_two_collison(player_one_X, player_one_Y, missle_two_X, missle_two_Y)
        if player_two_collision:
            missle_two_Y = 480
            missle_two_state = "ready"
            score_value_player_one -= 1
            score_value_player_two += 1

        if missle_one_Y <= 0:
            missle_one_Y = 480
            missle_one_state = "ready"
        if missle_one_state == "fire":
            fire_one_missle(missle_one_X, missle_one_Y)
            missle_one_Y -= missle_one_Y_change

        if missle_two_Y <= 0:
            missle_two_Y = 480
            missle_two_state = "ready"
        if missle_two_state == "fire":
            fire_two_missle(missle_two_X, missle_two_Y)
            missle_two_Y -= missle_two_Y_change

    # Starting Position of Players
    player_one_start_position(player_one_X, player_one_Y)
    player_two_start_position(player_two_X, player_two_Y)
    pygame.display.update()
pygame.quit()
