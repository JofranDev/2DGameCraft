import pygame

# Initialize pygame
pygame.init()

# Configure game window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("2DGameCraft")
running = True

# Color variables
BLUE = (0, 0, 255)

# Rectangle coordinates and size
rect_x = 100
rect_y = 100
rect_width = 200
rect_height = 100

# Main game loop
while running:
    screen.fill("purple")
    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, rect_width, rect_height])
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

# Update screen
pygame.display.flip()