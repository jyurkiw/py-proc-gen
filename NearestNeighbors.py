import pygame
import DrawApp
import SqrtShortcut
import random
import RandomPoints
import DrawWords
from operator import attrgetter

tri1_color = (0, 0, 125)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance_list = list()

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def get_array(self):
        return [self.x, self.y]


class Distance(object):
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __str__(self):
        return "[" + str(self.index) + "]: " + str(self.distance)


class NearestPoints(object):
    def __init__(self, points):
        self.points = list()

        for xy_pair in points:
            self.points.append(Point(xy_pair[0], xy_pair[1]))

        self.sqrt = SqrtShortcut.Roots()

    def find_distance(self, p_index_a, p_index_b):
        distance = abs(pow(self.points[p_index_a].x - self.points[p_index_b].x, 2) +
                       pow((-1 * self.points[p_index_a].y) - (-1 * self.points[p_index_b].y), 2))
        return self.sqrt.get(distance)

    def get_distance_list_for_point(self, p_index):
        for o_p_index in [i for i in range(0, len(self.points)) if i is not p_index]:
            self.points[p_index].distance_list.append(Distance(o_p_index, self.find_distance(p_index, o_p_index)))

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

    sub_list = [nearestPoints.points[draw_point_idx].get_array()]
    for t in [nearestPoints.points[d.index].get_array() for d in
              nearestPoints.points[draw_point_idx].distance_list[0:2]]:
        sub_list.append(t)

    triangle_list.append(sub_list)


if __name__ == "__main__":
    app = DrawApp.App([RandomPoints.draw_points, draw_triangles, DrawWords.draw_words], control_space, screen_width=800)

    random.seed(a=40)
    RandomPoints.gen_points(10, 640, 480)

    DrawWords.add_word("1", page_loc, "page")

    nearestPoints = NearestPoints(RandomPoints.points)
    nearestPoints.get_all_distances()

    # assemble triangle list
    set_triangle_list()

    app.run()
