import DrawApp
import pygame


line_color = (255, 0, 0)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)


class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw_line(self, screen):
        pygame.draw.aaline(screen, line_color, self.p1.get(), self.p2.get(), 2)


class LineBlitter(object):
    def __init__(self):
        self.lines = list()

    def add_line(self, x1, y1, x2, y2):
        self.lines.append(Line(Point(x1, y1), Point(x2, y2)))

    def draw_lines(self, screen):
        for line in self.lines:
            line.draw_line(screen)


_line_blitter = LineBlitter()


def draw_lines(screen, delta_t):
    _line_blitter.draw_lines(screen)

if __name__ == "__main__":
    app = DrawApp.App(draw_lines)

    _line_blitter.add_line(5, 100, 100, 100)
    _line_blitter.add_line(50, 200, 100, 100)
    _line_blitter.add_line(30, 300, 100, 100)
    _line_blitter.add_line(90, 400, 100, 100)

    app.run()
