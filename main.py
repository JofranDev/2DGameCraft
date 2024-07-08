import pygame

#iniciar pygame
pygame.init()

#configurar la ventana del juego
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mi primer juego con Pygame")
running = True

#variables de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#loop principal del juego
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

#actualizar pantalla
screen.fill(WHITE)
pygame.display.flip()