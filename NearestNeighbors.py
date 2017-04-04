import pygame
import DrawApp
import random
import RandomPoints
import DrawWords
from Pythag import Geo, RandGeo
from operator import attrgetter

tri1_color = (0, 0, 125)


class Point(Geo.Point2D):
    def __init__(self, x, y):
        self.distance_list = list()
        super(Point, self).__init__(x, y, None)

class Distance(object):
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __str__(self):
        return "[" + str(self.index) + "]: " + str(self.distance)


class NearestPoints(object):
    def __init__(self, points):
        self.points = list()

        for point in points:
            self.points.append(Point(point.x, point.y))

    def get_distance_list_for_point(self, p_index):
        for o_p_index in [i for i in range(0, len(self.points)) if i is not p_index]:
            self.points[p_index].distance_list.append(
                Distance(o_p_index, self.points[p_index].get_dist(self.points[o_p_index])))

        self.points[p_index].distance_list = sorted(self.points[p_index].distance_list, key=attrgetter('distance'))

    def get_all_distances(self):
        for p_index in range(0, len(self.points)):
            self.get_distance_list_for_point(p_index)


triangle_list = list()
time_since_last_space = 0
draw_point_idx = 0
can_shift = True
nearestPoints = None
page_loc = (620, 460)


def draw_triangles(screen, delta):
    for point_cluster in triangle_list:
        pygame.draw.lines(screen, tri1_color, True, point_cluster, 5)


def control_space(delta):
    global time_since_last_space
    global draw_point_idx
    global can_shift
    global triangle_list
    global nearestPoints

    time_since_last_space += delta

    if not can_shift and time_since_last_space > 250:
        can_shift = True

    if can_shift:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            can_shift = False
            time_since_last_space = 0
            draw_point_idx += 1

            if draw_point_idx >= len(nearestPoints.points):
                draw_point_idx = 0

            DrawWords.add_word(str(draw_point_idx + 1), page_loc, "page")
            set_triangle_list()


def set_triangle_list():
    global triangle_list
    triangle_list = list()

    sub_list = [nearestPoints.points[draw_point_idx].get()]
    for t in [nearestPoints.points[d.index].get() for d in
              nearestPoints.points[draw_point_idx].distance_list[0:2]]:
        sub_list.append(t)

    triangle_list.append(sub_list)


if __name__ == "__main__":
    app = DrawApp.App([RandomPoints.draw_points, draw_triangles, DrawWords.draw_words], control_space, screen_width=800)

    random.seed(a=40)

    DrawWords.add_word("1", page_loc, "page")

    RandomPoints.points = RandGeo.gen_rand_points(10, pygame.Rect(0, 0, 640, 480))
    RandomPoints.set_point_markers()
    nearestPoints = NearestPoints(RandomPoints.points)
    nearestPoints.get_all_distances()

    # assemble triangle list
    set_triangle_list()

    app.run()
