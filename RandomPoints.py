import DrawApp
import pygame
import random
import DrawWords
from Pythag import RandGeo

points = None


def draw_points(screen, delta):
    for point in points:
        point.draw(screen)


def set_point_markers():
    for p_idx in range(0, len(points)):
        loc = points[p_idx].get()
        loc[0] += 5
        loc[1] += 5
        DrawWords.add_word(str(p_idx + 1), loc)

if __name__ == "__main__":
    random.seed(a=40)

    points = RandGeo.gen_rand_points(10, pygame.Rect(0, 0, 640, 480))
    set_point_markers()

    app = DrawApp.App([draw_points, DrawWords.draw_words])
    app.run()
