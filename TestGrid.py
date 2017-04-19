import DrawApp
from Pythag.Grid import *

if __name__ == "__main__":
    cp = CartesianPlane()

    app = DrawApp.App(cp.draw_grid)

    app.run()
