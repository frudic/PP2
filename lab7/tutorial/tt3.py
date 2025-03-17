import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
clock = pygame.time.Clock()
x = 170
y = 120

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
            sound = pygame.mixer.Sound("Flo Rida - Whistle.mp3")
            sound.play(0)
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -=3
    if pressed[pygame.K_s]: y +=3
    if pressed[pygame.K_a]: x -=3
    if pressed[pygame.K_d]: x +=3
    
    screen.fill((0, 0, 0))
    color = (0, 128, 255) if is_blue else (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(120)
    
pygame.quit()