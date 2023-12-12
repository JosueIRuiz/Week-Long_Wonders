import pygame


class Character():
    def __init__(self, x, y, image, scale):
        character_width = image.get_width()
        character_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(character_width * scale), int(character_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def sprite_draw(self, surface):
        action = False
        #Get mouse position
        pos = pygame.mouse.get_pos()

        #Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Draw sprite on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
