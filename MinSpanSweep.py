import pygame
import DrawApp
import DrawWords
import DrawLines
import random
import RandomPoints
import NearestNeighbors
from Pythag import Geo, RandGeo


class Sweeper(object):
    def __init__(self, points):
        return 0

if __name__ == "__main__":
    app = DrawApp.App([RandomPoints.draw_points, DrawWords.draw_words], [], screen_width=800)
    random.seed(a=40)
    RandomPoints.points = RandGeo.gen_rand_points(10, pygame.Rect(0, 0, 640, 480))
    RandomPoints.set_point_markers()

    nearestPoints = NearestNeighbors.NearestPoints(RandomPoints.points)
    nearestPoints.get_all_distances()

    app.run()
