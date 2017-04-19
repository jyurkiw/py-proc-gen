import pygame
from pygame import freetype


class CPConfiguration(object):
    def __init__(self):
        self.min_x = -10
        self.min_y = -10
        self.max_x = 10
        self.max_y = 10
        self.x_increment = 1
        self.y_increment = 1
        self.line_color = (128, 128, 128)
        self.num_font_size = 8
        self.num_font_color = (128, 0, 0)


class CPScreenConfiguration(object):
    def __init__(self, screen_dim, conf):
        self.min_x = 10
        self.min_y = 10
        self.max_x = screen_dim[0] - 10
        self.max_y = screen_dim[1] - 10
        self.screen_x = screen_dim[0]
        self.screen_y = screen_dim[1]
        self.grid_screen_width = self.max_x - self.min_x
        self.grid_screen_height = self.max_y - self.min_y
        self.x_lines = int((conf.max_x - conf.min_x) / conf.x_increment)
        self.y_lines = int((conf.max_y - conf.min_y) / conf.y_increment)
        self.x_increment = self.max_x / self.x_lines
        self.y_increment = self.max_y / self.y_lines


class CartesianPlane(object):
    def __init__(self, conf=None):
        if conf is None:
            conf = CPConfiguration()

        self.min_x = conf.min_x
        self.min_y = conf.min_y
        self.max_x = conf.max_x
        self.max_y = conf.max_y
        self.x_range = (abs(self.min_x) + abs(self.max_x))
        self.y_range = (abs(self.min_y) + abs(self.max_y))
        self.x_increment = conf.x_increment
        self.y_increment = conf.y_increment
        self.line_color = conf.line_color
        self.num_font_size = conf.num_font_size
        self.num_font_color = conf.num_font_color
        self.screen_conf = None

        if not pygame.freetype.was_init():
            pygame.freetype.init()
        self.font = pygame.freetype.Font('./OxygenMono-Regular.ttf', self.num_font_size)

    def screen_pos_to_grid_pos(self, position):
        if self.screen_conf is not None:
            screen_x = float(position[0])
            screen_y = float(position[1])

            screen_x = screen_x / self.screen_conf.screen_x
            screen_y = screen_y / self.screen_conf.screen_y

            screen_x = self.min_x + (self.x_range * screen_x)
            screen_y = self.min_y + (self.y_range * screen_y)

            return [screen_x, screen_y]
        else:
            raise "Cannot translate screen position before screen data has been loaded"

    def grid_pos_to_screen_pos(self, position):
        if self.screen_conf is not None:
            screen_x = position[0] - float(self.min_x)
            screen_x = screen_x / (self.max_x - self.min_x)
            screen_x = screen_x * self.screen_conf.grid_screen_width + self.screen_conf.min_x

            distance_from_min_y = abs(float(self.min_y) - float(position[1]))
            distance_from_grid_top = (self.y_range - distance_from_min_y) / self.y_range
            screen_y = self.screen_conf.grid_screen_height * distance_from_grid_top + self.screen_conf.min_y

            return [screen_x, screen_y]
        else:
            raise "Cannot translate to screen position before screen data has been loaded"

    def set_screen(self, screen_size):
        self.screen_conf = CPScreenConfiguration(screen_size, self)

    def get_screen_grid_dimenstions(self):
        return pygame.Rect((self.screen_conf.min_y, self.screen_conf.min_x),
                           (self.screen_conf.max_x, self.screen_conf.max_y))

    def draw_grid(self, screen, delta_t):
        if self.screen_conf is None:
            self.screen_conf = CPScreenConfiguration(screen.get_size(), self)

        y_values = range(self.screen_conf.min_y, self.screen_conf.max_y + self.screen_conf.y_increment, self.screen_conf.y_increment)
        y_mid_value = y_values[int(round(float(self.screen_conf.y_lines) / 2))]
        for i in range(0, len(y_values)):
            if y_values[i] is not y_mid_value:
                pygame.draw.line(screen, self.line_color, (self.screen_conf.min_x, y_values[i]), (self.screen_conf.max_x, y_values[i]))
            else:
                pygame.draw.line(screen, self.line_color, (self.screen_conf.min_x, y_values[i]),
                                 (self.screen_conf.max_x, y_values[i]), 3)

        x_values = range(self.screen_conf.min_x, self.screen_conf.max_x + self.screen_conf.x_increment, self.screen_conf.x_increment)
        x_mid_value = x_values[int(round(float(self.screen_conf.x_lines) / 2))]
        for i in range(len(x_values)):
            if x_values[i] is not x_mid_value:
                pygame.draw.line(screen, self.line_color, (x_values[i], self.screen_conf.min_y),
                                 (x_values[i], self.screen_conf.max_y))
            else:
                pygame.draw.line(screen, self.line_color, (x_values[i], self.screen_conf.min_y),
                                 (x_values[i], self.screen_conf.max_y), 3)

        # Lines are drawn. Now draw the graph numbers
        y_line_values = range(self.max_y, self.min_y - self.y_increment, -self.y_increment)
        for i in range(0, len(y_values)):
            y_text = str(int(round(y_line_values[i])))
            y_dim = self.font.get_rect(y_text)

            if y_values[i] is not y_mid_value:
                self.font.render_to(screen,
                                (x_mid_value - 5 - y_dim.width, y_values[i] + y_dim.height - 2),
                                y_text, self.num_font_color)

        x_line_values = range(self.min_x, self.max_x + self.x_increment, self.x_increment)
        for i in range(0, len(x_values)):
            self.font.render_to(screen, (x_values[i] + 3, y_mid_value + 5),
                                str(int(round(x_line_values[i]))), self.num_font_color)

if __name__ == "__main__":
    grid = CartesianPlane()
    grid.set_screen((640, 480))

    original_position = (0, 0)

    print "Converting grid_pos to screen_pos for " + str(original_position)
    pos = grid.grid_pos_to_screen_pos(original_position)
    print pos

    print "Converting screen_pos back to grid_pos"
    n_pos = grid.screen_pos_to_grid_pos(pos)
    print n_pos

    print "Original position == New position"
    print original_position == n_pos

    print "------------------------------------"

    original_position = (2, 4)

    print "Converting grid_pos to screen_pos for " + str(original_position)
    pos = grid.grid_pos_to_screen_pos(original_position)
    print pos

    print "Converting screen_pos back to grid_pos"
    n_pos = grid.screen_pos_to_grid_pos(pos)
    print n_pos

    print "Original position == New position"
    print original_position == n_pos

    print "------------------------------------"

    original_position = (-2, -4)

    print "Converting grid_pos to screen_pos for " + str(original_position)
    pos = grid.grid_pos_to_screen_pos(original_position)
    print pos

    print "Converting screen_pos back to grid_pos"
    n_pos = grid.screen_pos_to_grid_pos(pos)
    print n_pos

    print "Original position == New position"
    print original_position == n_pos

    print grid.get_screen_grid_dimenstions()