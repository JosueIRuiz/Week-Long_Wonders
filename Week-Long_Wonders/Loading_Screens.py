import pygame
import Day_Setup
import Reset_Files

pygame.init()

# Setup Display
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week-Long Wonders")

# Setup Background Color
BG = (255, 204, 229)

# Setup Text Color
black = (0, 0, 0)
yellow = (255, 255, 204)
white = (255, 255, 255)


def win_draw():
    WIN.fill(black)


# Setup frame regulation
FPS = 60
clock = pygame.time.Clock()

# Defining font
new_text_font = pygame.font.Font("Daydream.ttf", 100)
text_font = pygame.font.Font("Daydream.ttf", 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))


def loading_screen_1():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('DAY 1', new_text_font, white, 80, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_1()

    pygame.quit()


def loading_screen_2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('DAY 2', new_text_font, white, 80, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_2()

    pygame.quit()


def loading_screen_3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('DAY 3', new_text_font, white, 80, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_3()

    pygame.quit()


def loading_screen_4():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('DAY 4', new_text_font, white, 80, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_4()

    pygame.quit()


def loading_screen_5():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('DAY 5', new_text_font, white, 80, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_5()

    pygame.quit()


def loading_screen_6():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('DAY 6', new_text_font, white, 80, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_6()

    pygame.quit()


def loading_screen_7():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('DAY 7', new_text_font, white, 80, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_7()

    pygame.quit()
