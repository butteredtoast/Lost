#!/usr/bin/env python
# encoding: utf-8
import pygame
import os
import sys

sys.path.insert(0, "lib")
#from menu import MainMenu
from title_screen import TitleScreen
from game import Game

"""some globals we'll need."""
SIZE = WIDTH, HEIGHT = 800, 600

def run():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    caption = pygame.display.set_caption('Lost In Africa')

    """"Get the title screen."""
    title = TitleScreen(screen)
    title.main()

    """Get the menu going."""
    Game()

if __name__ == "__main__":
    run()
