import ConfigParser, os

DATA_DIR    = os.path.abspath(os.path.dirname(__file__))
CONFIG_DIR  = os.path.normpath(os.path.join(DATA_DIR, '..', 'data/config/'))
IMAGE_DIR   = os.path.normpath(os.path.join(DATA_DIR, '..', 'data/audio/'))
SOUND_DIR   = os.path.normpath(os.path.join(DATA_DIR, '..', 'data/sound/'))
SPRITES_DIR = os.path.normpath(os.path.join(DATA_DIR, '..', 'data/sprites'))
FONTS_DIR   = os.path.normpath(os.path.join(DATA_DIR, '..', 'data/fonts'))
MAPS_DIR    = os.path.normpath(os.path.join(DATA_DIR, '..', 'data/maps'))
CHAR_DIR    = os.path.normpath(os.path.join(DATA_DIR, '..', 'data/characters'))


#Game settings
WIDTH, HEIGHT = 800, 600
SIZE = WIDTH, HEIGHT #This should change and be loaded instead from the globals.ini file

#Colors
#		 R    G    B
BLACK  = 0  , 0  , 0
RED    = 0
GREEN  = 0
PURPLE = 0
YELLOW = 0
BAGE   = 0
WHITE  = 255, 255, 255

"""Parse Constants File"""
config = ConfigParser.ConfigParser()
config.read(os.path.join(CONFIG_DIR, "Constants.ini")) 

G,D = {},{}

for k, v in config.items('game'):
  if v.isdigit():
    G[k] = int(v)
  elif v == "true":
    G[k] = True
  elif v == "false":
    G[k] = False
  else:
    G[k] = v
  

for k,v in config.items("debug"):
  if v == "true":
    D[k] = True
  else:
    D[k] = False

SONGLIST = [song for num, song in config.items("music")]

if __name__ == "__main__":
	print(SONGLIST)