import DrawApp
from Pythag.Grid import *
from Pythag import Geo


screen_dim = [640, 480]

p1 = [-1, -1]
p2 = [1, 2]

p1_p2_line = None


def draw_grid_line(screen, delta_t):
    p1_p2_line.draw(screen)


if __name__ == "__main__":
    cp = CartesianPlane()

    app = DrawApp.App([cp.draw_grid, draw_grid_line], screen_height=screen_dim[1], screen_width=screen_dim[0])
    cp.set_screen(screen_dim)

    p1 = cp.grid_pos_to_screen_pos(p1)
    p2 = cp.grid_pos_to_screen_pos(p2)

    p1 = Geo.Point2D(p1[0], p1[1])
    p2 = Geo.Point2D(p2[0], p2[1])

    p1_p2_line = Geo.Line2D(p1, p2)

    app.run()
