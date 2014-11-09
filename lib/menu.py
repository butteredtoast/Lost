#!/usr/bin/env python
# encoding: utf-8
import pygame, os
from sys import exit
from pygame.locals import * 
from text import Text
from util import load_image
from the_data import load_sound

WIDTH, HEIGHT = 800, 600
""" Global Config """
from globals import *

""" Generic Menu Class """
class Menu(object):
  
  def __init__(self, screen):
    self.running = True
    self.display = screen
    self.selection = ""
    self.key_pressed   = ""
    self.click = load_sound('on_click.ogg')
    self.vanish = load_sound("vanish.ogg")

  """ Check Menu Events """
  def checkEvents(self):
    
    for event in pygame.event.get():

     if event.type == KEYDOWN:
      keyname = pygame.key.name(event.key)
      

      if event.key in(K_DOWN, K_UP, K_LEFT, K_RIGHT, K_RETURN):
        self.selection = ""
        if keyname == "down" or keyname == "right":
          self.click.play()
          self.current_option += 1
        elif keyname == "up" or keyname == "left":
          self.click.play()
          self.current_option -= 1
        elif keyname == "return":
          self.vanish.play()
          self.selection = self.current_option

    """ Adjust the Menu """
    if self.current_option == len(self.MenuOptions):
      self.current_option = 0
    if self.current_option < 0:
      self.current_option = len(self.MenuOptions) - 1

  """ Meant to be Overloaded """
  def __handleSelection(self):
    pass

""" A Blank Menu """
class BlankMenu(Menu):

  def __init__(self, screen):
    Menu.__init__(self, screen)
    self.x = 180
    self.y = 125
    self.increment = 40
    self.active = True
    self.current_option = 0
    self.background = load_image("bg.png")
    self.MenuOptions = ["Go Back"]

  """ Run the Display For The Menu """
  def run(self):
    while self.active == True:
      self.display.blit(self.background, (self.x, self.y)) 
      self.checkEvents()
      self.__handleSelection()
      self.__draw()
      pygame.display.flip()
  
  """ Handle Selection """
  def __handleSelection(self):
    if isinstance(self.selection, int):

      """ Load Game Menu """
      if self.selection == 0:
        self.active = False


  """ Draw the Menu """
  def __draw(self):
    y = self.y

    text = Text("[Not Yet Implemented]", 18, "GameOption", (255, 255, 255))
    self.display.blit(text.render, (self.x, self.y + 220))

    for i, option in enumerate(self.MenuOptions):
      if self.selection == i:
        color = (255, 0, 0)
      elif self.current_option == i:
        color = (255, 255, 0)
      else:
        color = (255, 255, 255)

      text = Text(option, 22, "GameOption", color)
      self.display.blit(text.render, (self.x+100, y+100))
      y += self.increment

""" Main Menu """
class MainMenu(Menu):

  def __init__(self, screen):
    Menu.__init__(self, screen)
    self.x = 180
    self.y = 125
    self.increment = 40
    self.active = True
    self.current_option = 0
    self.background = load_image("bg.png")
    self.MenuOptions = ["Begin Adventure", "Load Adventure", "Settings", "Quit"]

  """ Run the Display For The Menu """
  def run(self):
    self.display.blit(self.background, (self.x-50, self.y)) 
    self.checkEvents()
    self.__handleSelection()
    self.__draw()
    pygame.display.flip()


  """ Handle Selection """
  def __handleSelection(self):
    if isinstance(self.selection, int):

      """ Start Game """
      if self.selection == 0:
        self.active = False
      
      """ Load Game """
      if self.selection == 1:
        self.selection = ""
        NoMenu = BlankMenu(self.display)
        NoMenu.run()
  
      """ Settings """
      if self.selection == 2:
        self.selection = ""
        NoMenu = BlankMenu(self.display)
        NoMenu.run()

      """ Quit """
      if self.selection == len(self.MenuOptions) - 1:
        exit()

  """ Draw the Menu """
  def __draw(self):
    y = self.y
    for i, option in enumerate(self.MenuOptions):
      if self.selection == i:
        color = (255, 0, 0)
      elif self.current_option == i:
        color = (255, 255, 0)
      else:
        color = (255, 255, 255)

      text = Text(option, 22, "GameOption", color)
      self.display.blit(text.render, (self.x+150, y+100))
      y += self.increment

