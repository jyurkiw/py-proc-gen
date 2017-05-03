import pygame


class Grid(object):
    def __init__(self, grid_size=[40,30], screen_dimensions=[640,480], color_atlas=[(0,0,0), (139,69,19)]):
        self.width = grid_size[0]
        self.height = grid_size[1]
        self.screen_width = screen_dimensions[0]
        self.screen_height = screen_dimensions[1]
        self.color_atlas = color_atlas

        self.square_width = int(self.screen_width / self.width)
        self.square_height = int(self.screen_height / self.height)

        # create basic fill-squares
        # do this once for each atlas entry, and then blit them over, and over, and over
        self._set_fill_atlas()

        # create the base grid. All squares start closed
        self._grid = list()
        for x in range(0, self.width):
            self._grid.append([0] * self.height)

    def _set_fill_atlas(self):
        self.fill_atlas = list()
        for color in self.color_atlas:
            fill_square = pygame.Surface((16, 16))
            fill_square.fill(color)
            self.fill_atlas.append(fill_square)

    def get(self, x, y):
        return self._grid[x][y]

    def set(self, x, y, value):
        self._grid[x][y] = value

    def set_grid(self, grid):
        self._grid = grid

    def blit(self, dest_surface):
        for x in range(0, self.width):
            for y in range(0, self.height):
                dest_surface.blit(self.fill_atlas[self._grid[x][y]], (x * self.square_width, y * self.square_height))
