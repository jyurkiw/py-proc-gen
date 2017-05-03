from PlayGrid import Grid
import DrawApp


class PlayGridTest(object):
    def __init__(self):
        self._grid = Grid.Grid()

    def draw_grid(self, screen, delta_t):
        self._grid.blit(screen)

if __name__ == "__main__":
    pg = PlayGridTest()
    pg._grid.set(4, 3, 1)
    pg._grid.set(4, 4, 1)
    pg._grid.set(3, 3, 1)
    pg._grid.set(3, 4, 1)
    pg._grid.set(4, 5, 1)

    app = DrawApp.App([pg.draw_grid])

    app.run()
