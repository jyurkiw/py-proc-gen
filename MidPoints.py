import pygame
import DrawApp
import DrawWords
import DrawLines
import random
import RandomPoints
import NearestNeighbors


page_loc = (620, 460)

if __name__ == "__main__":
    app = DrawApp.App([RandomPoints.draw_points, DrawWords.draw_words], [], screen_width=800)
    random.seed(a=40)
    RandomPoints.gen_points(10, 640, 480)

    nearestPoints = NearestNeighbors.NearestPoints(RandomPoints.points)
    nearestPoints.get_all_distances()

    DrawWords.add_word("1", page_loc, "page")

    app.run()
