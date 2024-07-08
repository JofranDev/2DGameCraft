import pygame

#iniciar pygame
pygame.init()

#configurar la ventana del juego
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mi primer juego con Pygame")
running = True

#variables de colores
BLUE = (0, 0, 255)

#coordenadas y tamaño del rectangulo
rect_x = 100
rect_y = 100
rect_width = 200
rect_height = 100

#loop principal del juego
while running:

	screen.fill("purple")
	pygame.draw.rect(screen, BLUE, [rect_x, rect_y, rect_width, rect_height])
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.update()

#actualizar pantalla
pygame.display.flip()