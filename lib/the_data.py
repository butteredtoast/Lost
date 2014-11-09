import pygame, os
main_dir = os.path.split(os.path.abspath(__file__))[0]
sound_dir = os.path.split(main_dir)[0]

def load_sound(file):
    if not pygame.mixer: return lambda *a: 'Oops!Mixer not initialized!'
    files = os.path.join(sound_dir, r'data/audio', file)
    print(files)
    try:
        sound = pygame.mixer.Sound(files)
        return sound
    except pygame.error:
        raise SystemExit('Unable to load {}'.format(files))

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(sound_dir, r'data/images', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface

def load_font(file, size):
    file = os.path.join(sound_dir, r'data/fonts', file)
    try:
        font = pygame.font.Font(file, size)
        return font
    except pygame.error:
        print("Can't open the file {}".format(file))
        
def load_music(file):
    if not pygame.mixer: return lambda *a: 'Oops!Mixer not initialized!'
    files = os.path.join(sound_dir, r'data/audio', file)
    try:
        sound = pygame.mixer.music.load(files)
        return sound
    except pygame.error:
        raise SystemExit('Unable to load {}'.format(files))

class MusicPlayer:
    def __init__(self, filename=None):
        pygame.mixer.init()
        if filename is not None:
            pygame.mixer.music.load(os.path.join(sound_dir, r'data/audio', filename))
        
    def load(self, filename):
        try:
            pygame.mixer.music.load(data.filepath(os.path.join("music", filename)))
        except pygame.error: print('Oops!')
        
    def play(self):
        pygame.mixer.music.play(-1)
    
    def stop(self):
        pygame.mixer.music.stop()

