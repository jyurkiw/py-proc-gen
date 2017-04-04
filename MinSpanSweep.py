import pygame
import DrawApp
import DrawWords
import DrawLines
import random
import RandomPoints
import NearestNeighbors

if __name__ == "__main__":
    app = DrawApp.App([RandomPoints.draw_points, DrawWords.draw_words], [], screen_width=800)
    random.seed(a=40)
    RandomPoints.gen_points(10, 640, 480)

    nearestPoints = NearestNeighbors.NearestPoints(RandomPoints.points)
    nearestPoints.get_all_distances()

    app.run()
