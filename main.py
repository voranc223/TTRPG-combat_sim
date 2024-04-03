from Fighters import *
from random_stuff import *
from Button_creation import button

pygame.init()


move_button = button(30, 40, 180, 50, screen)
action_button = button(30, 115, 180, 50, screen)
attack_button = button(30, 50, 180, 80, screen)
spell_button = button(30, 160, 180, 80, screen)
bonus_action = button(30, 190, 180, 50, screen)
clock = pygame.time.Clock()
p_1 = Character(fighter_1_scaled, [500, 233], 30, 10, 30, 0, 3, 1, f_1_offsets[0], f_1_offsets[1], f_1_offsets[2])
p_2 = Character(fighter_2_scaled, [937, 463], 30, 10, 30, 0, 3, 2, f_2_offsets[0], f_2_offsets[1], f_2_offsets[2])
p_3 = Character(fighter_3_scaled, [63, 463], 30, 10, 30, 0, 3, 3, f_3_offsets[0], f_3_offsets[1], f_3_offsets[2])
p_4 = Character(fighter_4_scaled, [500, 691], 30, 10, 30, 0, 3, 4, f_4_offsets[0], f_4_offsets[1], f_4_offsets[2])


def action_menu(player):
    action = True
    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = False
        screen.fill("light blue")
        basic_field()
        draw_fighters()
        draw_health_bars()
        pygame.draw.rect(screen, LIGHT_BLUE, actions_rect, 0, 10)
        attack_button.draw()
        spell_button.draw()
        screen.blit(attack_text, (40, 60))
        screen.blit(spell_text, (40, 160))
        if attack_button.clicked:
            player.attack(player.position, 10, p_2)
            attack_button.clicked = False
        pygame.display.update()


fps = 60
# Main loop
running = True
if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("light blue")
        basic_field()
        draw_fighters()
        draw_health_bars()
        pygame.draw.rect(screen, LIGHT_BLUE, actions_rect, 0, 10)
        move_button.draw()
        action_button.draw()
        bonus_action.draw()
        if move_button.clicked:
            p_1.move(p_1.position, 1)
            move_button.clicked = False
        elif action_button.clicked:
            action_menu(p_1)
        screen.blit(move_text, (80, 40))
        screen.blit(action_text, (75, 115))
        screen.blit(bonus_action_text, (28, 190))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
