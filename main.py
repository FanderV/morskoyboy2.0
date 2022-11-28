import pygame

Window_size = 30 #block_size
Left_field = 40
Up_field = 30

Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (51, 153, 255)
Size = (Left_field + 26.5 * Window_size, Up_field + 12 * Window_size)  # размер окна

pygame.init()

Display = pygame.display.set_mode(Size)
pygame.display.set_caption("Sea Battle")

Font_size = int(Window_size // 1.5)
Font = pygame.font.SysFont('Times New Roman', Font_size)


def draw_cells():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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
        if y < 10:
            num_ver = Font.render(str(y+1), True, Blue)
            letters_hor = Font.render(letters[y], True, Blue)
            num_ver_width = num_ver.get_width()
            num_ver_height = num_ver.get_height()
            letters_hor_width = letters_hor.get_width()
            #вертикальные сетки 1
            Display.blit(num_ver, (Left_field - (Window_size//2+num_ver_width//2), Up_field + y*Window_size + (Window_size//2 - num_ver_height//2)))
            #вертикальные сетки 1
            Display.blit(letters_hor, (Left_field + y*Window_size+(Window_size//2 - letters_hor_width//2), Up_field + 10 * Window_size))

            # вертикальные сетки 2
            Display.blit(num_ver, (Left_field - (Window_size // 2 + num_ver_width // 2) +15 * Window_size, Up_field + y * Window_size + (Window_size // 2 - num_ver_height // 2)))
            # вертикальные сетки 2
            Display.blit(letters_hor, (Left_field + y * Window_size + (Window_size // 2 - letters_hor_width // 2) + 15 * Window_size, Up_field + 10 * Window_size))

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
