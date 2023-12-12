import pygame
import Loading_Screens
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


def win_draw():
    WIN.fill(BG)


# Setup frame regulation
FPS = 60
clock = pygame.time.Clock()

# Defining font
text_font = pygame.font.Font("Daydream.ttf", 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))


def intro():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('In this game you will', text_font, black, 30, 50)
        draw_text('meet 3 characters', text_font, black, 45, 100)
        draw_text('across 7 days.', text_font, black, 80, 150)

        draw_text('There are three', text_font, black, 50, 250)
        draw_text('character types:', text_font, black, 35, 300)
        draw_text('Good, Bad, Neutral', text_font, black, 25, 350)

        draw_text('You are tasked with...', text_font, black, 10, 450)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    intro2()

    pygame.quit()


def intro2():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('finding out who the', text_font, black, 30, 50)
        draw_text('good character is', text_font, black, 45, 100)
        draw_text('and choosing to', text_font, black, 55, 150)
        draw_text('!IMMORTALIZE!', text_font, black, 100, 200)
        draw_text('them.', text_font, black, 200, 250)

        draw_text('You are given 3', text_font, black, 90, 350)
        draw_text('choices every day:', text_font, black, 40, 400)
        draw_text('IMMORTALIZE, FORGET', text_font, black, 30, 450)
        draw_text('and ERASE!', text_font, black, 135, 500)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    intro3()

    pygame.quit()


def intro3():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('You should:', text_font, black, 135, 100)
        draw_text('IMMORTALIZE good', text_font, black, 60, 150)
        draw_text('characters,', text_font, black, 130, 200)
        draw_text('REMEMBER neutral', text_font, black, 50, 250)
        draw_text('characters,', text_font, black, 130, 300)
        draw_text('and ERASE bad ', text_font, black, 105, 350)
        draw_text('characters!', text_font, black, 130, 400)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    intro4()

    pygame.quit()


def intro4():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('Think your ready...', text_font, black, 30, 200)
        draw_text('ready to BEGIN!', text_font, black, 65, 250)

        draw_text('If so...', text_font, black, 200, 450)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Loading_Screens.loading_screen_1()

    pygame.quit()
