# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pygame.mouse

    from random_stuff import *

    # Initialize Pygame
    pygame.init()

    screen = pygame.display.set_mode((1000, 800))
    grass_image = pygame.image.load("images/grass_image.png").convert_alpha()
    grass_image = pygame.transform.scale(grass_image, (100, 100))
    fighter_1 = pygame.image.load("images/Idle.png").convert_alpha()
    fighter_1_idle = fighter_1.subsurface((0, 0, 200, 200))
    fighter_1_scaled = pygame.transform.scale(fighter_1_idle, (250, 250))
    clock = pygame.time.Clock()
    game_field = []
    for i in range(20):
        new_row = []
        for j in range(20):
            new_row.append(j + i * 20)
        game_field.append(new_row)


    def movement():
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1 and mouse:
            pass


    def draw_fighter(row, column):
        screen.blit(fighter_1_scaled, (blocks[row - 1][column - 1]))


    fps = 60
    # Main loop
    running = True
    if __name__ == "__main__":
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            for i in range(20):
                for j in range(20):
                    screen.blit(grass_image, (450 - j * 23 + i * 23, 200 + 12 * j + i * 12))
                    pygame.draw.polygon(screen, (255, 255, 255),
                                        [(500 - j * 23 + i * 23, 223 + 12 * j + i * 12),
                                         (523 - j * 23 + i * 23, 235 + 12 * j + i * 12), (500 - j * 23 + i * 23,
                                                                                          247 + 12 * j + i * 12),
                                         (477 - j * 23 + i * 23, 235 + 12 * j + i * 12)], 1)
            draw_fighter(20, 20)
            movement()
            pygame.display.flip()
            clock.tick(fps)
        # Quit Pygame
        pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
