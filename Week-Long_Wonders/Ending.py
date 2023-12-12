import pygame
import Decision_Scribe
import Final_Ending_Selection
import Reset_Files


pygame.init()


# Setup Display
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week-Long Wonders")

# Setup Colors
green = (204, 255, 204)
red = (255, 204, 204)
purple = (229, 204, 255)
yellow = (255, 255, 204)
black = (0, 0, 0)
white = (255, 255, 255)


def bad_win_draw():
    WIN.fill(red)


def good_win_draw():
    WIN.fill(green)


def neutral_win_draw():
    WIN.fill(purple)


def win_draw():
    WIN.fill(black)


# Setup frame regulation
FPS = 60
clock = pygame.time.Clock()

# Defining font
big_font = pygame.font.Font("Daydream.ttf", 80)
text_font = pygame.font.Font("Daydream.ttf", 30)
dia_font = pygame.font.Font("Daydream.ttf", 18)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))


def pre_ending():
    run = True

    while run:

        clock.tick(FPS)

        win_draw()

        draw_text('FIN', big_font, white, 130, 200)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Decision_Scribe.close_file()
                    Final_Ending_Selection.write_file()
                    Final_Ending_Selection.read_file()
                    Final_Ending_Selection.answer_number()
                    Final_Ending_Selection.end()
                    with open('Ending_Selec.txt', 'r') as es:
                        if es.readline() == 'G':
                            good_ending()
                        else:
                            bad_ending()

    pygame.quit()


def good_ending():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('The Good Ending', text_font, black, 25, 25)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    thanks()

    pygame.quit()


def bad_ending():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('The Bad Ending', text_font, black, 25, 25)

        draw_text('Press N to Continue!', text_font, yellow, 20, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    thanks()

    pygame.quit()


def thanks():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Thank', big_font, black, 25, 25)

        draw_text('You!', big_font, black, 25, 225)

        draw_text('Press N to Close!', text_font, yellow, 45, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    d = open('Decisions.txt', 'r+')
                    d.truncate(0)
                    d.close()
                    e = open('Endings.txt', 'r+')
                    e.truncate(0)
                    e.close()
                    r = open('Right.txt', 'r+')
                    r.truncate(0)
                    r.close()
                    w = open('Wrong.txt', 'r+')
                    w.truncate(0)
                    w.close()
                    es = open('Ending_Selec.txt', 'r+')
                    es.truncate(0)
                    es.close()
                    run = False
                    break

    pygame.quit()
