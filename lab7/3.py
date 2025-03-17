import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")


BALL_RADIUS = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
BALL_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)
MOVE_STEP = 20

running = True
while running:
  clock.tick(60)  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP] and ball_y - BALL_RADIUS - MOVE_STEP >= 0:
    ball_y -= MOVE_STEP
  if pressed[pygame.K_DOWN] and ball_y + BALL_RADIUS + MOVE_STEP <= HEIGHT:
    ball_y += MOVE_STEP
  if pressed[pygame.K_LEFT] and ball_x - BALL_RADIUS - MOVE_STEP >= 0:
    ball_x -= MOVE_STEP
  if pressed[pygame.K_RIGHT] and ball_x + BALL_RADIUS + MOVE_STEP <= WIDTH:
    ball_x += MOVE_STEP
  
  screen.fill(BG_COLOR)
  pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
  pygame.display.flip()

pygame.quit()