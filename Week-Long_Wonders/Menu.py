import pygame
import Introduction_Screen
import Reset_Files

pygame.init()


# Setup Display
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week-Long Wonders")

# Setup Background
BG_Color = (255, 255, 204)

# Setup frame regulation
FPS = 60
clock = pygame.time.Clock()


def win_draw():
    WIN.fill(BG_Color)


# Defining font & text
menu_font = pygame.font.Font("Daydream.ttf", 60)
title_piece_1 = "Week-Long"
title_piece_2 = "Wonders"
start = "PRESS N TO"
start2 = "START"


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))


def start_menu():

    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text(title_piece_1, menu_font, (0, 0, 0), 20, 50)
        draw_text(title_piece_2, menu_font, (0, 0, 0), 65, 120)

        draw_text(start, menu_font, (0, 0, 0), 30, 400)
        draw_text(start2, menu_font, (0, 0, 0), 135, 470)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Introduction_Screen.intro()

    pygame.quit()
