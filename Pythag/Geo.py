import pygame
from math import sqrt


class Point2D(object):
    default_col_val = (255, 165, 0)

    def __init__(self, x, y, col_val=None):
        self.x = int(x)
        self.y = int(y)

        if col_val is not None:
            self.col_val = col_val
        else:
            self.col_val = Point2D.default_col_val

    def get(self):
        return [self.x, self.y]

    def get_dist(self, p_other):
        return sqrt(self.get_dist2(p_other))

    def get_dist2(self, p_other):
        return pow(p_other.x - self.x, 2) + pow(p_other.y - self.y, 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.col_val, self.get(), 5, 3)


class Line2D(object):
    default_col_val = (0, 0, 255)

    def __init__(self, p1, p2, col_val=None):
        self.p1 = p1
        self.p2 = p2

        if col_val is not None:
            self.col_val = col_val
        else:
            self.col_val = Line2D.default_col_val

    def get_length(self):
        return self.p1.get_dist(self.p2)

    def get_length2(self):
        return self.p1.get_dist2(self.p2)

    def draw(self, screen):
        pygame.draw.aaline(screen, self.col_val, self.p1.get(), self.p2.get())
