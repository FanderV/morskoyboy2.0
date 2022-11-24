import pygame

Window_size = 30
Left_field = 40
Up_field = 30

Black = (0, 0, 0)
White = (255, 255, 255)

Size = (Left_field + 26.5 * Window_size, Up_field + 12 * Window_size)  # размер окна

pygame.init()

Display = pygame.display.set_mode(Size)
pygame.display.set_caption("Sea Battle")

Font_size = int(Window_size // 1.5)
Font = pygame.font.SysFont('Times New Roman', Font_size)


def draw_cells():
    for y in range(11):
        for x in range(11):
            # горизонтальные линии
            pygame.draw.line(Display, Black, (Left_field, Up_field + y * Window_size),
                             (Left_field + 10 * Window_size, Up_field + y * Window_size), 1)
            # вертикальные линии
            pygame.draw.line(Display, Black, (Left_field + y * Window_size, Up_field),
                             (Left_field + y * Window_size, Up_field + 10 * Window_size), 1)
            # горизонтальные линии 2
            pygame.draw.line(Display, Black, (Left_field + 15 * Window_size, Up_field + y * Window_size),
                             (Left_field + 25 * Window_size, Up_field + y * Window_size), 1)
            # вертикальные линии 2
            pygame.draw.line(Display, Black, (Left_field + y * Window_size + 15 * Window_size, Up_field),
                             (Left_field + y * Window_size + 15 * Window_size, Up_field + 10 * Window_size),
                             1)


def main():
    game_over = False
    Display.fill(White)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        draw_cells()
        pygame.display.update()


main()
pygame.quit()
