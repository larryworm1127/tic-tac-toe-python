import pygame
import time

pygame.init()

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic Tac Toe')

clock = pygame.time.Clock()

# color variables
black = (0, 0, 0)
white = (255, 255, 255)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    screen.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 100)
        text_surf, text_rect = text_objects("Tic Tac Toe", large_text)
        text_rect.center = ((display_width / 2), (display_height / 2))
        screen.blit(text_surf, text_rect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def button(message, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))

        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(message, small_text)
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)


def game_loop():
    game_exit = True
    while game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = False
                quit_game()

        screen.fill(white)

        pygame.display.update()
        clock.tick(60)


def quit_game():
    pygame.quit()
    quit()


game_intro()
game_loop()
pygame.quit()
quit()
