import pygame


class App(object):
    def __init__(self, draw_func, control_func=None, screen_height=480, screen_width=640):
        self.draw_func = draw_func
        self.control_func = control_func
        self.screen_height = screen_height
        self.screen_width = screen_width

        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.done = False

    def run(self):
        clock = pygame.time.Clock()

        while not self.done:
            clock.tick()

            if self.control_func is not None and type(self.control_func) is not list:
                self.control_func(clock.get_time())
            elif self.control_func is not None:
                for control_func in self.control_func:
                    control_func(clock.get_time())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.screen.fill((0,0,0))

            if type(self.draw_func) is not list:
                self.draw_func(self.screen, clock.get_time())
            else:
                for draw_func in self.draw_func:
                    draw_func(self.screen, clock.get_time())

            pygame.display.flip()
