from Fighters import *
from random_stuff import *
from Button_creation import button

pygame.init()


screen = pygame.display.set_mode((1000, 800))
grass_image = pygame.image.load("images/grass_image.png").convert_alpha()
grass_image = pygame.transform.scale(grass_image, (100, 100))
fighter_1 = pygame.image.load("images/Idle.png").convert_alpha()
fighter_1_idle = fighter_1.subsurface((0, 0, 200, 200))
fighter_1_scaled = pygame.transform.scale(fighter_1_idle, (250, 250))
move_button = button(30, 40, 180, 50, screen)
action_button = button(30, 115, 180, 50, screen)
attack_button = button(30, 50, 180, 80, screen)
spell_button = button(30, 160, 180, 80, screen)
bonus_action = button(30, 190, 180, 50, screen)
rect_width = 10
clock = pygame.time.Clock()
closest = [500, 223]
closest_1 = [0, 0]
mouse_pressed = False
p_1 = Character("Harold", "Dragonborn", "paladin", fighter_1_scaled, [500, 233], 30, 10, 30, 0, 3, 1)
p_2 = Character("eragon", "half_elf", "warlock", fighter_1_scaled, [477, 245], 30, 10, 30, 0, 3, 2)
game_field = []
for i in range(20):
    new_row = []
    for j in range(20):
        new_row.append(j+i*20)
    game_field.append(new_row)


def action_menu(player):
    action = True
    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = False
        pygame.draw.rect(screen, LIGHT_BLUE, actions_rect, 0, 10)
        attack_button.draw()
        spell_button.draw()
        screen.blit(attack_text, (40, 60))
        screen.blit(spell_text, (40, 160))
        if attack_button.clicked:
            player.attack(screen, player.position, 10, p_2)
        pygame.display.update()
        clock.tick(fps)


fps = 60
# Main loop
running = True
if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        for i in range(20):
            for j in range(20):
                screen.blit(grass_image, (450-j*23+i*23, 200+12*j+i*12))
                pygame.draw.polygon(screen, WHITE,
                                    [(500 - j * 23 + i * 23, 223 + 12 * j + i * 12),
                                     (523 - j * 23 + i * 23, 235 + 12 * j + i * 12),
                                     (500 - j * 23 + i * 23, 247 + 12 * j + i * 12),
                                     (477 - j * 23 + i * 23, 235 + 12 * j + i * 12)], 1)
        p_1.draw_fighter(screen, p_1.position)
        p_1.draw_health_bar(screen, p_1.position)
        pygame.draw.rect(screen, LIGHT_BLUE, actions_rect, 0, 10)
        move_button.draw()
        action_button.draw()
        bonus_action.draw()
        if move_button.clicked:
            p_1.move(screen, p_1.position, 1)
            move_button.clicked = False
        elif action_button.clicked:
            action_menu(p_1)
        screen.blit(move_text, (80, 40))
        screen.blit(action_text, (75, 115))
        screen.blit(bonus_action_text, (28, 190))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
