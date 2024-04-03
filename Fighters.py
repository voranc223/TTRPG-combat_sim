import random
import pygame.display
from random_stuff import *
from Button_creation import button

# Initialize Pygame
pygame.init()


occupied_positions = [(0, 0), (0, 0), (0, 0), (0, 0)]
fighter_offsets = [(0, 0), (10, 8), (0, -5), (0, 6)]  # Example offsets for each fighter
fighter_images = [fighter_1_scaled, fighter_2_scaled, fighter_3_scaled, fighter_4_scaled]
fighters_health = [30, 30, 30, 30]


def draw_fighters():
    sorted_data = sorted(zip(occupied_positions, fighter_offsets, fighter_images), key=lambda data: data[0][1])
    for (x, y), (offset_x, offset_y), fighter_image in sorted_data:
        screen.blit(fighter_image, (x + offset_x - 125, y + offset_y - 160))


def draw_health_bars():
    for i in range(4):
        pygame.draw.rect(screen, "red", (occupied_positions[i][0] - 50,
                                         occupied_positions[i][1] - 100, 100, 15))
        pygame.draw.rect(screen, "yellow", (occupied_positions[i][0] - 50,
                                            occupied_positions[i][1] - 100, 100 / 30 * fighters_health[i], 15))


class Character:
    def __init__(self, image, position, movement,
                 damage_die, health, proficiency_bonus,
                 total_spell_slots, player_number, x_offset, y_offset, health_offset):
        self.image = image
        self.x = x_offset
        self.y = y_offset
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
        self.health_offset = health_offset
        occupied_positions[player_number - 1] = (self.position[0], self.position[1])

    def draw_health_bar(self, position):
        pygame.draw.rect(screen, RED, (position[0] - 50, position[1] - 90 - self.health_offset, 100, 12))
        pygame.draw.rect(screen, YELLOW, (position[0] - 50, position[1] - 90 - self.health_offset,
                                          100 * (self.current_health / self.max_health), 12))

    def attack(self, position, attack_range, target):
        attacking = True
        attack_polygon = Polygon([(position[0], position[1] - 12 - attack_range / 5 * 24),
                                 (position[0] + 23 + attack_range / 5 * 46, position[1]),
                                 (position[0], position[1] + 12 + attack_range / 5 * 24),
                                 (position[0] - 23 - attack_range / 5 * 46, position[1])])
        intersection = attack_polygon.intersection(field_polygon)
        while attacking:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.draw.polygon(screen, RED, intersection.exterior.coords)
            borders()
            draw_fighters()
            draw_health_bars()
            """if self.attack_bonus + random.randint(1, 20) >= target.armor_class:
                target.current_health -= self.damage"""
            pygame.display.update()
            attacking = False

    def move(self, position, player_number):
        pressed_1 = True
        polygon_points_1 = Polygon([(position[0], position[1] - 156), (position[0] + 299, position[1]),
                                   (position[0], position[1] + 156), (position[0] - 299, position[1])])
        polygon_points = [(position[0], position[1] - 156), (position[0] + 299, position[1]),
                          (position[0], position[1] + 156), (position[0] - 299, position[1])]
        back_button = button(700, 30, 180, 60, screen)
        pygame.draw.rect(screen, "light blue", (0, 0, 300, 330))
        while pressed_1:
            intersection = polygon_points_1.intersection(field_polygon)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if back_button.clicked:
                pressed_1 = False
                back_button.clicked = False
            pygame.draw.polygon(screen, "silver", intersection.exterior.coords)
            back_button.draw()
            screen.blit(back_text, (760, 40))
            borders()
            draw_fighters()
            draw_health_bars()
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
                    if (closest[0], closest[1]) not in occupied_positions:
                        occupied_positions[player_number - 1] = (closest[0], closest[1])
                        self.position = [closest[0], closest[1]]
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
