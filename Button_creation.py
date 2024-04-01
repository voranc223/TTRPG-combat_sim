import pygame
from random_stuff import RED
pygame.init()


class button:
    def __init__(self, x, y, button_width, button_height, surface):
        self.rect = pygame.Rect(x, y, button_width, button_height)
        self.surface = surface
        self.clicked = False

    def draw(self):
        action = False
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        pygame.draw.rect(self.surface, RED, self.rect, 0, 10)
        return action
