import random
import time

import pygame.display
from random_stuff import *
from Button_creation import button

# Initialize Pygame
pygame.init()


occupied_squares = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]


class Character:
    def __init__(self, race, Class, name, image, position, movement,
                 damage_die, health, proficiency_bonus, total_spell_slots, player_number):
        self.name = name
        self.race = race
        self.Class = Class
        self.image = image
        self.modifiers = Modifiers(3, 0, 1, -1, 0, 3)
        self.position = position
        self.movement = movement
        self.damage = random.randint(1, damage_die) + self.modifiers.strength
        self.max_health = health
        self.current_health = self.max_health
        self.proficiency_bonus = proficiency_bonus
        self.attack_bonus = proficiency_bonus + self.modifiers.strength
        self.total_spell_slots = total_spell_slots
        self.spells_used = 0
        self.current_spell_slots = total_spell_slots - self.spells_used
        occupied_squares[player_number - 1] = self.position

    def draw_fighter(self, screen, position):
        screen.blit(self.image, (position[0] - 125, position[1] - 160))

    def attack(self, screen, position, attack_range, target):
        attacking = True
        attack_polygon = [(position[0], position[1] - 12 - attack_range / 5 * 24),
                          (position[0] + 23 + attack_range / 5 * 46, position[1]),
                          (position[0], position[1] + 12 + attack_range / 5 * 24),
                          (position[0] - 23 - attack_range / 5 * 46, position[1])]
        while attacking:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.draw.polygon(screen, RED, attack_polygon)
            for i in range(20):
                for j in range(20):
                    pygame.draw.polygon(screen, WHITE,
                                        [(500 - j * 23 + i * 23, 223 + 12 * j + i * 12),
                                         (523 - j * 23 + i * 23, 235 + 12 * j + i * 12),
                                         (500 - j * 23 + i * 23, 247 + 12 * j + i * 12),
                                         (477 - j * 23 + i * 23, 235 + 12 * j + i * 12)], 1)
            screen.blit(self.image, (position[0] - 125, position[1] - 160))
            self.draw_health_bar(screen, position)
            if self.attack_bonus + random.randint(1, 20) >= target.armor_class:
                target.current_health -= self.damage
            pygame.display.update()
            attacking = False

    def draw_health_bar(self, screen, position):
        pygame.draw.rect(screen, RED, (position[0] - 50, position[1] - 90, 100, 12))
        pygame.draw.rect(screen, YELLOW, (position[0] - 50, position[1] - 90,
                                          100 * (self.current_health / self.max_health), 12))

    def move(self, screen, position, player_number):
        pressed_1 = True
        polygon_points = [(position[0], position[1] - 156), (position[0] + 299, position[1]),
                          (position[0], position[1] + 156), (position[0] - 299, position[1])]
        back_button = button(700, 30, 180, 60, screen)
        pygame.draw.rect(screen,BLACK, (0, 0, 300, 330))
        while pressed_1 is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if back_button.clicked:
                pressed_1 = False
                back_button.clicked = False
            pygame.draw.polygon(screen, BLACK, (polygon_points[0],
                                                polygon_points[1],
                                                polygon_points[2],
                                                polygon_points[3]))
            back_button.draw()
            screen.blit(back_text, (760, 40))
            for i in range(20):
                for j in range(20):
                    pygame.draw.polygon(screen, WHITE,
                                        [(500 - j * 23 + i * 23, 223 + 12 * j + i * 12),
                                         (523 - j * 23 + i * 23, 235 + 12 * j + i * 12),
                                         (500 - j * 23 + i * 23, 247 + 12 * j + i * 12),
                                         (477 - j * 23 + i * 23, 235 + 12 * j + i * 12)], 1)
            screen.blit(self.image, (position[0] - 125, position[1] - 160))
            self.draw_health_bar(screen, position)
            if pygame.mouse.get_pressed()[0] == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                is_inside = False
                for i in range(len(polygon_points)):
                    p1 = polygon_points[i]
                    p2 = polygon_points[(i + 1) % len(polygon_points)]
                    if (
                            ((p1[1] > mouse_y) != (p2[1] > mouse_y)) and
                            (mouse_x < (p2[0] - p1[0]) * (mouse_y - p1[1]) / (p2[1] - p1[1]) + p1[0])
                    ):
                        is_inside = not is_inside
                if is_inside:
                    for i in polygon_cords:
                        for j in i:
                            if abs(j[0] - mouse_x) + abs(j[1] - mouse_y) < abs(closest[0] - mouse_x) + abs(
                                    closest[1] - mouse_y):
                                closest[0] = j[0]
                                closest[1] = j[1]
                    if (closest[0], closest[1]) not in occupied_squares:
                        self.position = closest
                        occupied_squares[player_number - 1] = self.position
                        pressed_1 = False
            pygame.display.update()


class Modifiers:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


class Armor:
    def __init__(self, name, armor_class, armor_type, dex_bonus_cap, modifiers):
        self.name = name
        self.dex_bonus_cap = dex_bonus_cap
        self.armor_class = armor_class
        self.type = armor_type
        if modifiers.dexterity > dex_bonus_cap:
            modifiers.dexterity = dex_bonus_cap
        self.armor_class = armor_class + modifiers.dexterity
