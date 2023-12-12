import pygame
import Day_Setup
import Decision_Scribe
import Ending
import Loading_Screens
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


# Setup frame regulation
FPS = 60
clock = pygame.time.Clock()

# Defining font
text_font = pygame.font.Font("Daydream.ttf", 30)
dia_font = pygame.font.Font("Daydream.ttf", 18)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))


# Day 1 Encounters
def char_1_screen():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('Y-Man:', text_font, black, 25, 25)
        draw_text('Hello, I am... well I was, a good man.', dia_font, black, 40, 75)
        draw_text('I used to be a surgeon.', dia_font, black, 40, 125)
        draw_text('A darn good one at that!', dia_font, black, 40, 175)
        draw_text('I saved any person...', dia_font, black, 40, 225)
        draw_text('Anybody who was willing to pay.', dia_font, black, 40, 275)
        draw_text('Be it a mob boss or murderer.', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_1()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_1_p2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_1_p2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_1_p2()

    pygame.quit()


def char_2_screen():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Granola:', text_font, black, 25, 25)
        draw_text('Hello, I am a bush fairy.', dia_font, black, 40, 75)
        draw_text('In my past life I...', dia_font, black, 40, 125)
        draw_text('ran my own charity!', dia_font, black, 40, 175)
        draw_text('The charity focused on,', dia_font, black, 40, 225)
        draw_text('Helping hungry people all over.', dia_font, black, 40, 275)
        draw_text('It was nice talking to you!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_1_p2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_1_p3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_1_p3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_1_p3()

    pygame.quit()


def char_3_screen():
    run = True

    while run:

        clock.tick(FPS)

        neutral_win_draw()

        draw_text('Doom Shroom:', text_font, black, 25, 25)
        draw_text('Hello there, I am Doom Shroom!', dia_font, black, 40, 75)
        draw_text('I do not have a past life.', dia_font, black, 40, 125)
        draw_text('I live in this reality and,', dia_font, black, 40, 175)
        draw_text('Always have.', dia_font, black, 40, 225)
        draw_text('I hope you find what you are', dia_font, black, 40, 275)
        draw_text('Looking for, Au revoir!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_1_p3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Loading_Screens.loading_screen_2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Loading_Screens.loading_screen_2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Loading_Screens.loading_screen_2()

    pygame.quit()


# Day 2 Encounters
def char_4_screen():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Manon:', text_font, black, 25, 25)
        draw_text("Aloha, I am a shark.", dia_font, black, 40, 75)
        draw_text('In my past life I was retail worker.', dia_font, black, 40, 125)
        draw_text('I lived my life to the fullest,', dia_font, black, 40, 175)
        draw_text('I made sure to enjoy every second!', dia_font, black, 40, 225)
        draw_text('I enjoyed talking to you!', dia_font, black, 40, 275)
        draw_text('Thank you for listening to me!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_2_p2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_2_p2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_2_p2()

    pygame.quit()


def char_5_screen():
    run = True

    while run:

        clock.tick(FPS)

        neutral_win_draw()

        draw_text('Escargot:', text_font, black, 25, 25)
        draw_text('Hello, I believe I am supposed...', dia_font, black, 40, 75)
        draw_text('To be a snail of some sort!', dia_font, black, 40, 125)
        draw_text('This shell feels strange!', dia_font, black, 40, 175)
        draw_text('I do not have a past life. ', dia_font, black, 40, 225)
        draw_text('I am thankful to you!', dia_font, black, 40, 275)
        draw_text('Thanks for listening! ', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_2_p2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_2_p3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_2_p3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_2_p3()

    pygame.quit()


def char_6_screen():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('Henry:', text_font, black, 25, 25)
        draw_text('Uhh, I hate this body!', dia_font, black, 40, 75)
        draw_text('I wish I could go back to my old life!', dia_font, black, 40, 125)
        draw_text('I used to be a politician!', dia_font, black, 40, 175)
        draw_text('I had power and influence.', dia_font, black, 40, 225)
        draw_text('You must give me my life back!', dia_font, black, 40, 275)
        draw_text('I will share my power with you!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_2_p3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Loading_Screens.loading_screen_3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Loading_Screens.loading_screen_3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Loading_Screens.loading_screen_3()

    pygame.quit()


# Day 3 Encounters
def char_7_screen():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('Korrupt:', text_font, black, 25, 25)
        draw_text('Hello!', dia_font, black, 40, 75)
        draw_text('I am Korrupt, a security bot!', dia_font, black, 40, 125)
        draw_text('I used to be security for clubs...', dia_font, black, 40, 175)
        draw_text("in my past life, I wasn't the best.", dia_font, black, 40, 225)
        draw_text('I used to accept bribes... ', dia_font, black, 40, 275)
        draw_text('I must go back to my duties!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_3_p2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_3_p2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_3_p2()

    pygame.quit()


def char_8_screen():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Strakur & Stelpa:', text_font, black, 25, 25)
        draw_text('Hello...Hello!', dia_font, black, 40, 75)
        draw_text('We are twins who both studied...', dia_font, black, 40, 125)
        draw_text('Stellar bodies!', dia_font, black, 40, 175)
        draw_text("We were planning to land a...", dia_font, black, 40, 225)
        draw_text('ship with passengers, on Mars!', dia_font, black, 40, 275)
        draw_text('Thank you for hearing us out!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_3_p2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_3_p3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_3_p3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_3_p3()

    pygame.quit()


def char_9_screen():
    run = True

    while run:

        clock.tick(FPS)

        neutral_win_draw()

        draw_text('Napaka:', text_font, black, 25, 25)
        draw_text('Hello I am Napaka!', dia_font, black, 40, 75)
        draw_text('I have lived here for my whole...', dia_font, black, 40, 125)
        draw_text('existence. I hope you like it.', dia_font, black, 40, 175)
        draw_text("The environment is a crowded,", dia_font, black, 40, 225)
        draw_text('But the people here are nice!', dia_font, black, 40, 275)
        draw_text('Have a good day!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_3_p3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Loading_Screens.loading_screen_4()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Loading_Screens.loading_screen_4()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Loading_Screens.loading_screen_4()

    pygame.quit()


# Day 4 Encounters
def char_10_screen():
    run = True

    while run:

        clock.tick(FPS)

        neutral_win_draw()

        draw_text('Kijanka:', text_font, black, 25, 25)
        draw_text('Hello I am Kijanka!', dia_font, black, 40, 75)
        draw_text('My name means tadpole!', dia_font, black, 40, 125)
        draw_text('I always have liked my name! ', dia_font, black, 40, 175)
        draw_text("I really like having a unique name!", dia_font, black, 40, 225)
        draw_text('Thank you for coming along!', dia_font, black, 40, 275)
        draw_text('Have a good one!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_4()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_4_p2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_4_p2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_4_p2()

    pygame.quit()


def char_11_screen():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('Kusi:', text_font, black, 25, 25)
        draw_text('Kusi? What kinda name is that!', dia_font, black, 40, 75)
        draw_text('Why do I have tobe given such...', dia_font, black, 40, 125)
        draw_text('A bad name. ', dia_font, black, 40, 175)
        draw_text("I want my old life of riches.", dia_font, black, 40, 225)
        draw_text('You did this to me!!!', dia_font, black, 40, 275)
        draw_text('I will get my revenge!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_4_p2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_4_p3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_4_p3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_4_p3()

    pygame.quit()


def char_12_screen():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Baya:', text_font, black, 25, 25)
        draw_text('Baya is my name!!', dia_font, black, 40, 75)
        draw_text('Wildlife conservation...', dia_font, black, 40, 125)
        draw_text('That used to be my profession!', dia_font, black, 40, 175)
        draw_text("I used to run multiple charities!", dia_font, black, 40, 225)
        draw_text('Thank you for hearing my story!', dia_font, black, 40, 275)
        draw_text('Have a good day!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_4_p3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Loading_Screens.loading_screen_5()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Loading_Screens.loading_screen_5()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Loading_Screens.loading_screen_5()

    pygame.quit()


# Day 5 Encounters
def char_13_screen():
    run = True

    while run:

        clock.tick(FPS)

        neutral_win_draw()

        draw_text('Nisse:', text_font, black, 25, 25)
        draw_text('Hello I am Nisse!', dia_font, black, 40, 75)
        draw_text('I am a goblin!', dia_font, black, 40, 125)
        draw_text('My species thrives on jelly.', dia_font, black, 40, 175)
        draw_text("I really like jelly, especially", dia_font, black, 40, 225)
        draw_text('strawberry jelly!', dia_font, black, 40, 275)
        draw_text('Have a jamtastic day!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_5()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_5_p2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_5_p2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_5_p2()

    pygame.quit()


def char_14_screen():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('Multo:', text_font, black, 25, 25)
        draw_text('Multo is my name!', dia_font, black, 40, 75)
        draw_text('I am a ghost in this world.', dia_font, black, 40, 125)
        draw_text('I used to hold a monopoly.', dia_font, black, 40, 175)
        draw_text("a monopoly on eggs.", dia_font, black, 40, 225)
        draw_text('I made eggs the most expensive!', dia_font, black, 40, 275)
        draw_text('Do what you must!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_5_p2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_5_p3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_5_p3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_5_p3()

    pygame.quit()


def char_15_screen():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Trolio:', text_font, black, 25, 25)
        draw_text('Hello, good fellow!!', dia_font, black, 40, 75)
        draw_text("I am a troll, but I wasn't...", dia_font, black, 40, 125)
        draw_text('Always one, I was a family man once!', dia_font, black, 40, 175)
        draw_text("I had 3 kids, 2 girls, 1 boy!", dia_font, black, 40, 225)
        draw_text('Please save me!', dia_font, black, 40, 275)
        draw_text('Please!!!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_5_p3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Loading_Screens.loading_screen_6()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Loading_Screens.loading_screen_6()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Loading_Screens.loading_screen_6()

    pygame.quit()


# Day 6 Encounters
def char_16_screen():
    run = True

    while run:

        clock.tick(FPS)

        neutral_win_draw()

        draw_text('Tywod:', text_font, black, 25, 25)
        draw_text('I am but a mere sand bug.', dia_font, black, 40, 75)
        draw_text('I have always lived in this land.', dia_font, black, 40, 125)
        draw_text('I am neither good nor evil.', dia_font, black, 40, 175)
        draw_text("I just am!", dia_font, black, 40, 225)
        draw_text('Thank you for listening!', dia_font, black, 40, 275)
        draw_text('Find your truth.', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_6()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_6_p2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_6_p2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_6_p2()

    pygame.quit()


def char_17_screen():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('Kwaya:', text_font, black, 25, 25)
        draw_text('I have turned to a nut!', dia_font, black, 40, 75)
        draw_text('How can this be?', dia_font, black, 40, 125)
        draw_text('I used to be an assassin,', dia_font, black, 40, 175)
        draw_text("but now i am nothing , but a nut!", dia_font, black, 40, 225)
        draw_text('Bring me back to life.', dia_font, black, 40, 275)
        draw_text('You loser!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_6_p2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_6_p3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_6_p3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_6_p3()

    pygame.quit()


def char_18_screen():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Suppe:', text_font, black, 25, 25)
        draw_text('Hello!', dia_font, black, 40, 75)
        draw_text('I am a talking bowl of soup!', dia_font, black, 40, 125)
        draw_text('I wish I could go back to my life!', dia_font, black, 40, 175)
        draw_text("I used to have 2 adopted children.", dia_font, black, 40, 225)
        draw_text('They are my world, please...', dia_font, black, 40, 275)
        draw_text('Get me back to them!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_6_p3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Loading_Screens.loading_screen_7()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Loading_Screens.loading_screen_7()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Loading_Screens.loading_screen_7()

    pygame.quit()


# Day 7 Encounters
def char_19_screen():
    run = True

    while run:

        clock.tick(FPS)

        bad_win_draw()

        draw_text('Alkoholiker:', text_font, black, 25, 25)
        draw_text('Hey you, you there!', dia_font, black, 40, 75)
        draw_text('I somehow turned into wine!', dia_font, black, 40, 125)
        draw_text('You must not return me...', dia_font, black, 40, 175)
        draw_text("To my old life.", dia_font, black, 40, 225)
        draw_text("I hate my family! I'm bad!", dia_font, black, 40, 275)
        draw_text('So just erase me!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_7()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_7_p2()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_7_p2()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_7_p2()

    pygame.quit()


def char_20_screen():
    run = True

    while run:

        clock.tick(FPS)

        neutral_win_draw()

        draw_text('Gland:', text_font, black, 25, 25)
        draw_text('Bonjour!', dia_font, black, 40, 75)
        draw_text('I am but a measly acorn!', dia_font, black, 40, 125)
        draw_text('I like my life as it is.', dia_font, black, 40, 175)
        draw_text("There are ups and downs but,", dia_font, black, 40, 225)
        draw_text("I love it nonetheless!", dia_font, black, 40, 275)
        draw_text('Thank you for caring!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_7_p2()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Day_Setup.day_7_p3()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Day_Setup.day_7_p3()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Day_Setup.day_7_p3()

    pygame.quit()


def char_21_screen():
    run = True

    while run:

        clock.tick(FPS)

        good_win_draw()

        draw_text('Taimi:', text_font, black, 25, 25)
        draw_text('Hello, fellow passenger.', dia_font, black, 40, 75)
        draw_text('Passenger of life I mean.', dia_font, black, 40, 125)
        draw_text('I wish for you to take me back to,', dia_font, black, 40, 175)
        draw_text("my reality.", dia_font, black, 40, 225)
        draw_text("I have people to take care of!", dia_font, black, 40, 275)
        draw_text('So please help me!', dia_font, black, 40, 325)

        draw_text('P = Remember', dia_font, yellow, 40, 400)
        draw_text('A = Erase', dia_font, yellow, 40, 425)
        draw_text('I = Immortalize', dia_font, yellow, 40, 450)

        draw_text('Press N to Return!', text_font, yellow, 50, 550)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset_Files.reset_f()
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    Day_Setup.day_7_p3()

                if event.key == pygame.K_p:
                    Decision_Scribe.write_remember()
                    Ending.pre_ending()

                if event.key == pygame.K_a:
                    Decision_Scribe.write_erase()
                    Ending.pre_ending()

                if event.key == pygame.K_i:
                    Decision_Scribe.write_immortalize()
                    Ending.pre_ending()

    pygame.quit()
