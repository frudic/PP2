import pygame

playlist = [r"Ariana Grande - 7 rings.mp3", r"Ajjkyn_Tolepbergen_-_Pakh_pakh_78109168.mp3"]
current_track = 0

def play():
  pygame.mixer.music.load(playlist[current_track])
  pygame.mixer.music.play(0)
  
def stop():
  pygame.mixer.music.stop()

def next():
  global current_track
  current_track = (current_track + 1) % len(playlist)
  play()

def previous():
  global current_track
  current_track = (current_track - 1) % len(playlist)
  play()

pygame.init()
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200, 200))

while not done:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill((255, 255, 255))
  pressed = pygame.key.get_pressed() 
  if pressed[pygame.K_SPACE]: stop() #stop
  if pressed[pygame.K_o]: play() #play
  if pressed[pygame.K_RIGHT]: next() #next
  if pressed[pygame.K_LEFT]: previous() #previous

  pygame.display.flip()