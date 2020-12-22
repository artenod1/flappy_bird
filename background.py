import pygame
import random

class Background():
	def __init__(self, settings, screen, theme='day'):

		self.settings = settings
		self.screen = screen

		#background
		if theme == 'day':
			self.bg_surface_image = pygame.image.load('images/background-day.png').convert()
		elif theme == 'night':
			self.bg_surface_image = pygame.image.load('images/background-night.png').convert()
		self.bg_surface = pygame.transform.scale(self.bg_surface_image, 
			(self.settings.screen_width, self.settings.screen_height))

		# floor
		self.floor_image = pygame.image.load('images/base.png').convert()
		self.floor = pygame.transform.scale(self.floor_image, 
			(self.settings.floor_width, self.settings.floor_height))
		self.floor_x_pos = 0
		self.floor_y_pos = self.settings.screen_height-self.settings.floor_height*.5

		# Pipes
		self.pipe = Pipes(self.settings, self.screen, theme)

	def blit_bg(self):
		self.update_floor()
		self.pipe.update()
		self.screen.blit(self.bg_surface, (0,0))
		self.pipe.blit_pipes()
		self.screen.blit(self.floor, (self.floor_x_pos, self.floor_y_pos))

	def blit_bg_intro(self):
		# self.update_floor()
		self.screen.blit(self.bg_surface, (0,0))
		self.screen.blit(self.floor, (self.floor_x_pos, self.floor_y_pos))


	def update_floor(self):
		self.floor_x_pos -= self.settings.pipe_rate

		if self.floor_x_pos <= -self.settings.screen_width:
			self.floor_x_pos = 0

	def reset(self):
		self.pipe.reset()


class Pipes():

	def __init__(self, settings, screen, theme='day'):
		self.settings = settings
		self.screen = screen
		if theme == 'day':
			self.bottom_pipe_image = pygame.image.load('images/pipe-green.png').convert()
		elif theme == 'night':
			self.bottom_pipe_image = pygame.image.load('images/pipe-red.png').convert()

		self.bottom_pipe = pygame.transform.scale(self.bottom_pipe_image, 
			(self.settings.pipe_width, self.settings.pipe_height))
		self.top_pipe = pygame.transform.flip(self.bottom_pipe, False, True)

		self.rect_bp = self.bottom_pipe.get_rect()
		self.rect_tp = self.top_pipe.get_rect()

		#start pipes at the right-mid screen for now, will make this random later
		y = self._random_height()
		self.rect_bp.topleft = (self.settings.screen_width, y)
		self.rect_tp.bottomleft = (self.settings.screen_width, y - self.settings.pipe_separation)


	def update(self):
		self.rect_bp.centerx -= self.settings.pipe_rate
		self.rect_tp.centerx -= self.settings.pipe_rate
		if self.rect_bp.topright[0] <= 0:
			self.reset()
		self.blit_pipes()

	def blit_pipes(self):
		self.screen.blit(self.bottom_pipe, self.rect_bp)
		self.screen.blit(self.top_pipe, self.rect_tp)		


	def reset(self):
		y = self._random_height()
		self.rect_bp.topleft = (self.settings.screen_width, y)
		self.rect_tp.bottomleft = (self.settings.screen_width, y - self.settings.pipe_separation)

	def _random_height(self):
		return random.choice(
			[self.settings.screen_height//1.2,
			self.settings.screen_height//1.5, 
			self.settings.screen_height//2, 
			self.settings.screen_height//2.9,
			self.settings.screen_height//3.1,
			])




