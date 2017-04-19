import random
import Geo


def gen_rand_points(num_points, bound_rect):
    point_list = list()

    for pi in range(0, num_points):
        point_list.append(Geo.Point2D(random.randint(bound_rect.left, bound_rect.right),
                                      random.randint(bound_rect.top, bound_rect.bottom)))

    return point_list
