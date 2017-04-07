import math
from Geo import Point2D, Line2D


class Parabola(object):
    def __init__(self, vertex, focus=None, directrix_distance=None, is_vertical=True):
        self.vertex = vertex
        self.focus = focus
        self.directrixDistance = directrix_distance
        self.is_vertical = is_vertical

        if focus is None:

        elif directrix_distance is None:


    def get_val_at(self, val):
        """
        Get the x or y val for this parabola at val 
        :param val: An x or y value. Should be x if vertical, and y if horizontal
        :return: The corrisponding y or x val
        """
        if self.is_vertical:
