import os
import datetime
import platform
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,114,0)
GREEN = (0,255,0)


class DisplayText():
	def __init__(self, text, size, color, x, y):
		self.font = pygame.font.Font(None, size)
		self.image = self.font.render(text, 1, color)
		self.textpos = self.image.get_rect()
		self.textpos.centerx = x
		self.textpos.centery = y
	def draw(self, surface):
		surface.blit(self.image, self.textpos)



class Window():
	def __init__(self, width, height):
		self.rect = pygame.Rect(0, 0, width, height)
		pygame.display.init()
		pygame.font.init()
		pygame.mouse.set_visible(False)
		pygame.display.set_caption('pygame: time test')
		self.screen = pygame.display.set_mode(self.rect.size)

	def run(self):
		running = True
		frame_rate = 5

		self.clock = pygame.time.Clock()

		# Event loop
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			self.background = pygame.Surface(self.screen.get_size())
			self.background = self.background.convert()
			self.background.fill(BLACK)

			self.time = DisplayText(datetime.datetime.now().strftime("%H:%M:%S"),
									150,
									GREEN,
									self.background.get_rect().centerx,
									self.background.get_rect().centery)

			self.dist = DisplayText(platform.linux_distribution()[0],
									40,
									RED,
									self.background.get_rect().centerx,
									450)

			self.uname = DisplayText(platform.uname()[2],
									40,
									ORANGE,
									self.background.get_rect().centerx,
									500)

			self.time.draw(self.background)
			self.dist.draw(self.background)
			self.uname.draw(self.background)

			# Blit everything to the screen
			self.screen.blit(self.background, (0, 0))
			pygame.display.flip()

			self.clock.tick(frame_rate)

		pygame.quit()


Window(800,600).run()
