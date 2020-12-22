# Store all flappy bird settings
import pygame

class Settings():

	def __init__(self, scale=1, sound=True):

		# Screen settings
		self.scale = scale
		self.screen_width = int(288*self.scale)
		self.screen_height = int(512*self.scale)
		self.mid_screen = (self.screen_width//2, self.screen_height//2)
		self.intro_width = int(148*self.scale)
		self.intro_height = int(267*self.scale)

		# floor settings
		self.floor_width = int(336*2*self.scale)
		self.floor_height = int(112*self.scale)

		# Pipe settings
		self.pipe_width = int(52*self.scale)
		self.pipe_height = int(320*self.scale)
		self.pipe_separation = int(150*self.scale)
		self.pipe_rate = 2*self.scale

		# bird settings
		self.gravity = 0.125*self.scale
		self.jump_rate = -5*self.scale
		self.flap_rate = 8
		self.start_pos = .17*self.screen_width

		# Options Font
		self.font_size = int(10*self.scale)
		self.game_font = pygame.font.Font('font/04b_19.ttf', self.font_size)
		self.font_color = (255, 255, 255)

		# Score Font
		self.score_font_size = int(20*self.scale)
		self.score_font = pygame.font.Font('font/04b_19.ttf', self.score_font_size)

		# Sounds
		self.sound = sound
		self.flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
		self.death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')

		

		
