import pygame

pygame.init()

mouse_x, mouse_y = 0, 0
closest = [0, 0]
LIGHT_BLUE = (59, 85, 162)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
actions_rect = (20, 20, 200, 250)
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 30)
big_font = pygame.font.SysFont("comicsans", 40)
move_text = font.render("Move", True, WHITE)
back_text = font.render("Back", True, WHITE)
action_text = font.render("Action", True, WHITE)
bonus_action_text = font.render("Bonus Action", True, WHITE)
attack_text = big_font.render("Attack", True, WHITE)
spell_text = big_font.render("Spellcast", True, WHITE)
blocks = []
for i in range(20):
    new_row = []
    for j in range(20):
        new_row.append((373-23*j+23*i, 76+12*j+12*i))
    blocks.append(new_row)
polygon_cords = []
for i in range(20):
    new_row = []
    for j in range(20):
        new_row.append((500-23*j+23*i, 235+12*j+12*i))
    polygon_cords.append(new_row)
