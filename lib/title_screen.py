#!usr/bin/env/python
import pygame
from random import randint
import os, pygame.mixer, pygame.time
from menu import MainMenu
from the_data import load_image, load_sound, load_font

SIZE = WIDTH, HEIGHT = 800, 600
BAGE = 255, 240, 200
WHITE = 255,255,255
BLACK = 0,0,0
BLUE = 20, 20, 40
NUMSTARS = 400

class Star:
    def __init__(self, numstars):
        self.size = self.width, self.height = SIZE
        self.numstars = numstars
        self.stars = []
        self.initialize()

    def initialize(self):
        for num in xrange(self.numstars):
            self.pos = [randint(0,WIDTH), randint(0,HEIGHT)]
            self.stars.append(self.pos)

    def draw_stars(self, surface, color):
        for star in self.stars:
            surface.set_at(star, color)

    

class TitleScreen:
    """ Start screen. Also doubles as a stage intermission screen. """
    def __init__(self, screen = None, logo = None):
        if screen is None:
            self.screen = pygame.display.set_mode(SIZE)
        else:
            self.screen = screen
        self.running = True

        if not logo:
            self.logo   = load_image('nightfall.png').convert()
        else:
            self.logo = logo
            
        self.font = load_font('GameOption.ttf', 24)
        self.stars = Star(NUMSTARS)
        self.bird1 = load_sound('single_cricket.ogg')
        self.bird1.set_volume(0.25)
        self.clock = pygame.time.Clock()
        self.skip = False
        

        self.stars = Star(NUMSTARS)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.skip = True
        elif event.type == (pygame.QUIT or pygame.K_ESCAPE):
            self.running = False
            return

    def fade_into_screen(self, logo_alpha = 0):
        while logo_alpha < 255 and not self.skip:
            for evt in pygame.event.get(): self.handle_event(evt)
            self.screen.fill(BLACK)
            self.stars.draw_stars(self.screen, WHITE)
            self.logo.set_alpha(logo_alpha)
            self.screen.blit(self.logo, (150, 150))
            logo_alpha += 3
            pygame.display.flip()
            self.clock.tick(30)
    
    def fade_out(self, logo_alpha = 0):
        while logo_alpha > 0 and not self.skip:
            for event in pygame.event.get(): self.handle_event(event)
            self.logo.set_alpha(logo_alpha)
            self.screen.blit(self.logo, (150,150))
            logo_alpha -= 3
            pygame.display.flip()

    def fadein_text(self, intro=''):
        self.skip = False
        counter = 50
        while counter > 0 and not self.skip:
            for event in pygame.event.get(): self.handle_event(event)
            self.screen.fill(BLACK)
            text = self.font.render(intro, 1, WHITE)
            self.screen.blit(text, (150, 500))
            pygame.display.flip()
            self.clock.tick(30)
            counter -= 1
            
    def main(self):
        """ Display the screen and a little bit of text at the bottom
            of the screen. """
        self.bird1.play(2)
             
        logo_alpha = 0

        text = "A journey through Africa..."
     
        self.fade_into_screen(logo_alpha)
        
        self.fade_out(logo_alpha)

        self.fadein_text(intro = text)
            
        self.bird1.stop()


if __name__ == '__main__':
    pygame.init()
    title = TitleScreen()
    title.main()

