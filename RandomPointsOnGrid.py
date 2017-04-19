from Pythag.Grid import *
import DrawApp
from pygame import Rect
import random
import DrawWords
from Pythag import Geo, RandGeo


points = None
screen_points = None
grid = None


def draw_points(screen, delta):
    for point in screen_points:
        point.draw(screen)


def build_screen_points():
    global screen_points
    screen_points = list()

    for point in points:
        coordinates = grid.grid_pos_to_screen_pos(point.get())
        screen_points.append(Geo.Point2D(coordinates[0], coordinates[1]))


def set_point_markers():
    for p_idx in range(0, len(screen_points)):
        loc = screen_points[p_idx].get()
        grid_loc = points[p_idx].get()
        loc[0] += 5
        loc[1] += 5
        DrawWords.add_word("(" + "{0:.2f}".format(grid_loc[0]) + ", " + "{0:.2f}".format(grid_loc[1]) + ")", loc)


if __name__ == "__main__":
    random.seed(a=40)

    grid = CartesianPlane()
    grid.set_screen((640, 480))

    points = RandGeo.gen_rand_points(10, Rect((grid.min_x, grid.min_y), (grid.x_range, grid.y_range)))
    build_screen_points()
    set_point_markers()

    app = DrawApp.App([grid.draw_grid, draw_points, DrawWords.draw_words], screen_height=600, screen_width=800)
    app.run()
