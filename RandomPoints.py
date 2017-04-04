import DrawApp
import pygame
import random
import DrawWords

points = list()
_color = (255, 128, 0)


def gen_points(num_points, x_max, y_max):
    for p in range(0, num_points):
        loc = (random.randint(0, x_max), random.randint(0, y_max))
        num_loc = (loc[0] + 5, loc[1] + 5)
        points.append(loc)
        DrawWords.add_word(str(p + 1) + " x:" + str(loc[0]) + ", y:" + str(loc[1]), num_loc)


def draw_points(screen, delta):
    for p in points:
        pygame.draw.circle(screen, _color, p, 5, 4)

if __name__ == "__main__":
    random.seed(a=40)
    gen_points(5, 300, 300)
    app = DrawApp.App([draw_points, DrawWords.draw_words])
    app.run()