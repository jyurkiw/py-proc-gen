import DrawApp
import pygame
from pygame import freetype


class Phrase(object):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class WordBlitter(object):
    def __init__(self):
        self.font = pygame.freetype.Font('./OxygenMono-Regular.ttf', 10)
        self.phrases = list()
        self.acc_phrases = dict()

    def add(self, text, loc, key=None):
        if key is None:
            self.phrases.append(Phrase(text, loc))
        else:
            self.acc_phrases[key] = Phrase(text, loc)

if not pygame.freetype.was_init():
    pygame.freetype.init()
_word_blitter = WordBlitter()
t_color = (255,255,255)


def add_word(text, loc, key=None):
    _word_blitter.add(text, loc, key)


def draw_words(screen, delta):
    for p in _word_blitter.phrases + _word_blitter.acc_phrases.values():
        _word_blitter.font.render_to(screen, p.loc, p.text, t_color, None)


if __name__ == "__main__":
    app = DrawApp.App(draw_words)
    add_word("test", (10, 10))
    add_word("test", (30, 30))
    add_word("test", (60, 60))
    add_word("test", (120, 120))
    add_word("new Test", (70, 30), "two")
    add_word("new Test2", (70, 30), "two")

    app.run()
