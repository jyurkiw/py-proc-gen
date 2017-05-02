import DrawApp
from Pythag.Grid import *
from Pythag import Geo


screen_dim = [640, 480]






def draw_grid_parabola(screen, delta_t):



if __name__ == "__main__":
    cp = CartesianPlane()

    app = DrawApp.App([cp.draw_grid, draw_grid_parabola], screen_height=screen_dim[1], screen_width=screen_dim[0])
    cp.set_screen(screen_dim)


    app.run()
