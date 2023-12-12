# Week-Long Wonders
# Josue I Ruiz
# November 18 2023

import pygame
import Clickable_Character
import Character_Dialogue
import Reset_Files


pygame.init()

# Setup Display
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week-Long Wonders")

# Setup Colors
yellow = (255, 255, 204)

# Setup Backgrounds
BG1 = pygame.transform.scale(pygame.image.load("Game_Backgrounds/Sprite-0022.jpeg"), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load("Game_Backgrounds/Sprite-0023.jpeg"), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load("Game_Backgrounds/Sprite-0024.jpeg"), (WIDTH, HEIGHT))
BG4 = pygame.transform.scale(pygame.image.load("Game_Backgrounds/Sprite-0025.jpeg"), (WIDTH, HEIGHT))
BG5 = pygame.transform.scale(pygame.image.load("Game_Backgrounds/Sprite-0026.jpeg"), (WIDTH, HEIGHT))
BG6 = pygame.transform.scale(pygame.image.load("Game_Backgrounds/Sprite-0027.jpeg"), (WIDTH, HEIGHT))
BG7 = pygame.transform.scale(pygame.image.load("Game_Backgrounds/Sprite-0028.jpeg"), (WIDTH, HEIGHT))


def win_draw_1():
    WIN.blit(BG1, (0, 0))


def win_draw_2():
    WIN.blit(BG2, (0, 0))


def win_draw_3():
    WIN.blit(BG3, (0, 0))


def win_draw_4():
    WIN.blit(BG4, (0, 0))


def win_draw_5():
    WIN.blit(BG5, (0, 0))


def win_draw_6():
    WIN.blit(BG6, (0, 0))


def win_draw_7():
    WIN.blit(BG7, (0, 0))


# Load in the character sprite
character_1 = pygame.image.load('Game_Sprites/Sprite-0001.png').convert_alpha()
character_2 = pygame.image.load('Game_Sprites/Sprite-0002.png').convert_alpha()
character_3 = pygame.image.load('Game_Sprites/Sprite-0003.png').convert_alpha()

character_4 = pygame.image.load('Game_Sprites/Sprite-0004.png').convert_alpha()
character_5 = pygame.image.load('Game_Sprites/Sprite-0005.png').convert_alpha()
character_6 = pygame.image.load('Game_Sprites/Sprite-0006.png').convert_alpha()

character_7 = pygame.image.load('Game_Sprites/Sprite-0007.png').convert_alpha()
character_8 = pygame.image.load('Game_Sprites/Sprite-0008.png').convert_alpha()
character_9 = pygame.image.load('Game_Sprites/Sprite-0009.png').convert_alpha()

character_10 = pygame.image.load('Game_Sprites/Sprite-0010.png').convert_alpha()
character_11 = pygame.image.load('Game_Sprites/Sprite-0011.png').convert_alpha()
character_12 = pygame.image.load('Game_Sprites/Sprite-0012.png').convert_alpha()

character_13 = pygame.image.load('Game_Sprites/Sprite-0013.png').convert_alpha()
character_14 = pygame.image.load('Game_Sprites/Sprite-0014.png').convert_alpha()
character_15 = pygame.image.load('Game_Sprites/Sprite-0015.png').convert_alpha()

character_16 = pygame.image.load('Game_Sprites/Sprite-0016.png').convert_alpha()
character_17 = pygame.image.load('Game_Sprites/Sprite-0017.png').convert_alpha()
character_18 = pygame.image.load('Game_Sprites/Sprite-0018.png').convert_alpha()

character_19 = pygame.image.load('Game_Sprites/Sprite-0019.png').convert_alpha()
character_20 = pygame.image.load('Game_Sprites/Sprite-0020.png').convert_alpha()
character_21 = pygame.image.load('Game_Sprites/Sprite-0021.png').convert_alpha()


# Create character instances
# Day 1 Encounters
character_1_sprite = Clickable_Character.Character(0, 175, character_1, 8)
character_12_sprite = Clickable_Character.Character(200, 175, character_12, 8)
character_19_sprite = Clickable_Character.Character(400, 175, character_19, 8)

# Day 2 Encounters
character_17_sprite = Clickable_Character.Character(0, 175, character_17, 8)
character_10_sprite = Clickable_Character.Character(200, 175, character_10, 8)
character_13_sprite = Clickable_Character.Character(400, 175, character_13, 8)

# Day 3 Encounters
character_3_sprite = Clickable_Character.Character(0, 175, character_3, 8)
character_21_sprite = Clickable_Character.Character(200, 175, character_21, 8)
character_15_sprite = Clickable_Character.Character(400, 175, character_15, 8)

# Day 4 Encounters
character_5_sprite = Clickable_Character.Character(0, 175, character_5, 8)
character_6_sprite = Clickable_Character.Character(200, 175, character_6, 8)
character_11_sprite = Clickable_Character.Character(400, 175, character_11, 8)

# Day 5 Encounters
character_2_sprite = Clickable_Character.Character(0, 175, character_2, 8)
character_7_sprite = Clickable_Character.Character(200, 175, character_7, 8)
character_18_sprite = Clickable_Character.Character(400, 175, character_18, 8)

# Day 6 Encounters
character_4_sprite = Clickable_Character.Character(0, 175, character_4, 8)
character_8_sprite = Clickable_Character.Character(200, 175, character_8, 8)
character_20_sprite = Clickable_Character.Character(400, 175, character_20, 8)

# Day 7 Encounters
character_16_sprite = Clickable_Character.Character(0, 175, character_16, 8)
character_14_sprite = Clickable_Character.Character(200, 175, character_14, 8)
character_9_sprite = Clickable_Character.Character(400, 175, character_9, 8)


# Setup frame regulation
FPS = 60
clock = pygame.time.Clock()

# Defining font
text_font = pygame.font.Font("Daydream.ttf", 30)
dia_font = pygame.font.Font("Daydream.ttf", 14)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))


def day_1():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_1()

        draw_text('Day 1', dia_font, (0, 0, 0), 25, 25)

        character_1_sprite.sprite_draw(WIN)
        character_12_sprite.sprite_draw(WIN)
        character_19_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_1_screen()

    pygame.quit()


def day_1_p2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_1()

        draw_text('Day 1', dia_font, (0, 0, 0), 25, 25)

        character_12_sprite.sprite_draw(WIN)
        character_19_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_2_screen()

    pygame.quit()


def day_1_p3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_1()

        draw_text('Day 1', dia_font, (0, 0, 0), 25, 25)

        character_19_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_3_screen()

    pygame.quit()


def day_2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_2()

        draw_text('Day 2', dia_font, (0, 0, 0), 25, 25)

        character_17_sprite.sprite_draw(WIN)
        character_10_sprite.sprite_draw(WIN)
        character_13_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_4_screen()

    pygame.quit()


def day_2_p2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_2()

        draw_text('Day 2', dia_font, (0, 0, 0), 25, 25)

        character_10_sprite.sprite_draw(WIN)
        character_13_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_5_screen()

    pygame.quit()


def day_2_p3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_2()

        draw_text('Day 2', dia_font, (0, 0, 0), 25, 25)

        character_13_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_6_screen()

    pygame.quit()


def day_3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_3()

        draw_text('Day 3', dia_font, (0, 0, 0), 25, 25)

        character_3_sprite.sprite_draw(WIN)
        character_21_sprite.sprite_draw(WIN)
        character_15_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_7_screen()

    pygame.quit()


def day_3_p2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_3()

        draw_text('Day 3', dia_font, (0, 0, 0), 25, 25)

        character_21_sprite.sprite_draw(WIN)
        character_15_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_8_screen()

    pygame.quit()


def day_3_p3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_3()

        draw_text('Day 3', dia_font, (0, 0, 0), 25, 25)

        character_15_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_9_screen()

    pygame.quit()


def day_4():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_4()

        draw_text('Day 4', dia_font, (0, 0, 0), 25, 25)

        character_5_sprite.sprite_draw(WIN)
        character_6_sprite.sprite_draw(WIN)
        character_11_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_10_screen()

    pygame.quit()


def day_4_p2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_4()

        draw_text('Day 4', dia_font, (0, 0, 0), 25, 25)

        character_6_sprite.sprite_draw(WIN)
        character_11_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_11_screen()

    pygame.quit()


def day_4_p3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_4()

        draw_text('Day 4', dia_font, (0, 0, 0), 25, 25)

        character_11_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_12_screen()

    pygame.quit()


def day_5():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_5()

        draw_text('Day 5', dia_font, (0, 0, 0), 25, 25)

        character_2_sprite.sprite_draw(WIN)
        character_7_sprite.sprite_draw(WIN)
        character_18_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_13_screen()

    pygame.quit()


def day_5_p2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_5()

        draw_text('Day 5', dia_font, (0, 0, 0), 25, 25)

        character_7_sprite.sprite_draw(WIN)
        character_18_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_14_screen()

    pygame.quit()


def day_5_p3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_5()

        draw_text('Day 5', dia_font, (0, 0, 0), 25, 25)

        character_18_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_15_screen()

    pygame.quit()


def day_6():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_6()

        draw_text('Day 6', dia_font, (0, 0, 0), 25, 25)

        character_4_sprite.sprite_draw(WIN)
        character_8_sprite.sprite_draw(WIN)
        character_20_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_16_screen()

    pygame.quit()


def day_6_p2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_6()

        draw_text('Day 6', dia_font, (0, 0, 0), 25, 25)

        character_8_sprite.sprite_draw(WIN)
        character_20_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_17_screen()

    pygame.quit()


def day_6_p3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_6()

        draw_text('Day 6', dia_font, (0, 0, 0), 25, 25)

        character_20_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_18_screen()

    pygame.quit()


def day_7():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_7()

        draw_text('Day 7', dia_font, (0, 0, 0), 25, 25)

        character_16_sprite.sprite_draw(WIN)
        character_14_sprite.sprite_draw(WIN)
        character_9_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_19_screen()

    pygame.quit()


def day_7_p2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_7()

        draw_text('Day 7', dia_font, (0, 0, 0), 25, 25)

        character_14_sprite.sprite_draw(WIN)
        character_9_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_20_screen()

    pygame.quit()


def day_7_p3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw_7()

        draw_text('Day 7', dia_font, (0, 0, 0), 25, 25)

        character_9_sprite.sprite_draw(WIN)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Character_Dialogue.char_21_screen()

    pygame.quit()
