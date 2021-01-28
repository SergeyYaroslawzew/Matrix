import pygame as pg 
import random

class MatrixLetters:
    def __init__(self, app):
        self.app = app
        self.letters = "1234567890"
        self.font_size = 16
        self.font = pg.font.SysFont('arial', self.font_size, bold=True)
        self.columns = app.razmer.current_w // self.font_size
        self.drops = [1 for i in range(0, self.columns)]
        
    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0,255,0))
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.razmer.current_h and random.uniform(0,1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1
    
    def run(self):
        self.draw()
        
        
class MatrixApp:
    def __init__(self):
        pg.init()
        self.razmer = pg.display.Info()
        self.RES = self.razmer.current_w, self.razmer.current_h
        self.screen = pg.display.set_mode(self.RES,pg.FULLSCREEN)
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)
        self.clock = pg.time.Clock()
        self.matrixLetters = MatrixLetters(self)
    
    def draw(self):
        self.surface.fill((0,0,0,10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0,0))
        
    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.KEYDOWN and i.key == pg.K_END]
            pg.display.flip()
            self.clock.tick(30)

if __name__ == '__main__':
    app = MatrixApp()
    app.run()