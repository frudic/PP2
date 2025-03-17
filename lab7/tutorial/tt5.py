import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

font = pygame.font.SysFont("timesnewroman", 72)

text = font.render("Solo Leveling", True, (0, 128, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)