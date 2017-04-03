import DrawApp
import pygame

_start_x = 20
_start_x2 = 240
_start_y = 20
line_len = 200


def draw_lines(screen, delta):
    start_y = _start_y
    for i in range(1, 11):
        for n in range(1, i):
            pygame.draw.line(screen, (255, 0, 0), (_start_x, start_y), (_start_x + line_len, start_y + 10), 2)
            pygame.draw.aaline(screen, (255, 0, 0), (_start_x2, start_y), (_start_x2 + line_len, start_y + 10), 2)
        start_y += 20


if __name__ == "__main__":
    app = DrawApp.App(draw_lines)
    app.run()
