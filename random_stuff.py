import pygame
from shapely.geometry import Polygon
pygame.init()

screen = pygame.display.set_mode((1000, 800))
grass_image = pygame.image.load("images/grass_image.png").convert_alpha()
grass_image = pygame.transform.scale(grass_image, (100, 100))
fighter_1 = pygame.image.load("images/Idle_ninja.png").convert_alpha()
fighter_2 = pygame.image.load("images/Idle_wizzard.png").convert_alpha()
fighter_3 = pygame.image.load("images/Idle_wizard.png").convert_alpha()
fighter_4 = pygame.image.load("images/Idle_fighter.png").convert_alpha()
fighter_1_idle = fighter_1.subsurface((0, 0, 200, 200))
fighter_2_idle = fighter_2.subsurface((0, 0, 150, 150))
fighter_3_idle = fighter_3.subsurface((0, 0, 250, 250))
fighter_4_idle = fighter_4.subsurface((0, 0, 162, 162))
fighter_1_scaled = pygame.transform.scale(fighter_1_idle, (250, 250))
fighter_2_scaled = pygame.transform.scale(fighter_2_idle, (230, 230))
fighter_3_scaled = pygame.transform.scale(fighter_3_idle, (250, 250))
fighter_4_scaled = pygame.transform.scale(fighter_4_idle, (250, 250))
fighter_images = [fighter_1_scaled, fighter_2_scaled, fighter_3_scaled, fighter_4_scaled]
f_1_offsets = [0, 0, 0]
f_2_offsets = [10, 8, 0]
f_3_offsets = [0, -5, 0]
f_4_offsets = [0, 6, 7]
closest = [500, 223]
LIGHT_BLUE = (59, 85, 162)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
TRANSPARENT_RED = (0, 0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
actions_rect = (20, 20, 200, 250)
clock = pygame.time.Clock()
field_polygon = Polygon([(500, 223), (960, 463), (500, 703), (40, 463)])
font = pygame.font.SysFont("comicsans", 30)
big_font = pygame.font.SysFont("comicsans", 40)
move_text = font.render("Move", True, WHITE)
back_text = font.render("Back", True, WHITE)
action_text = font.render("Action", True, WHITE)
bonus_action_text = font.render("Bonus Action", True, WHITE)
attack_text = big_font.render("Attack", True, WHITE)
spell_text = big_font.render("Spellcast", True, WHITE)
polygon_cords = []
for i in range(20):
    new_row = []
    for j in range(20):
        new_row.append((500-23*j+23*i, 235+12*j+12*i))
    polygon_cords.append(new_row)


def basic_field():
    for i in range(20):
        for j in range(20):
            screen.blit(grass_image, (450 - j * 23 + i * 23, 200 + 12 * j + i * 12))
            pygame.draw.polygon(screen, WHITE,
                                [(500 - j * 23 + i * 23, 223 + 12 * j + i * 12),
                                 (523 - j * 23 + i * 23, 235 + 12 * j + i * 12),
                                 (500 - j * 23 + i * 23, 247 + 12 * j + i * 12),
                                 (477 - j * 23 + i * 23, 235 + 12 * j + i * 12)], 1)


def borders():
    for i in range(20):
        for j in range(20):
            pygame.draw.polygon(screen, WHITE,
                                [(500 - j * 23 + i * 23, 223 + 12 * j + i * 12),
                                 (523 - j * 23 + i * 23, 235 + 12 * j + i * 12),
                                 (500 - j * 23 + i * 23, 247 + 12 * j + i * 12),
                                 (477 - j * 23 + i * 23, 235 + 12 * j + i * 12)], 1)
