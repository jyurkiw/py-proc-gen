import DrawApp
from Pythag import Geo


line_color = (255, 0, 0)


class LineBlitter(object):
    def __init__(self):
        self.lines = list()

    def add_line(self, x1, y1, x2, y2):
        self.lines.append(Geo.Line2D(Geo.Point2D(x1, y1), Geo.Point2D(x2, y2)))

    def draw_lines(self, screen):
        for line in self.lines:
            line.draw(screen)


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
