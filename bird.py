import pygame


class Bird():

	def __init__(self, settings, screen, color='blue'):
		self.screen = screen
		self.settings = settings

		# load all bird images and put in a list.
		self.bird_width = int(34*self.settings.scale)
		self.bird_height = int(24*self.settings.scale)

		if color == 'blue':
			self.bird_animations = [
			pygame.image.load('images/bluebird-upflap.png').convert(),
			pygame.image.load('images/bluebird-midflap.png').convert(),
			pygame.image.load('images/bluebird-downflap.png').convert()
			]

		elif color == 'red':
			self.bird_animations = [
			pygame.image.load('images/redbird-upflap.png').convert(),
			pygame.image.load('images/redbird-midflap.png').convert(),
			pygame.image.load('images/redbird-downflap.png').convert()
			]

		elif color == 'yellow':
			self.bird_animations = [
			pygame.image.load('images/yellowbird-upflap.png').convert(),
			pygame.image.load('images/yellowbird-midflap.png').convert(),
			pygame.image.load('images/yellowbird-downflap.png').convert()
			]

		# Scale each image in list
		for i in range(len(self.bird_animations)):
			self.bird_animations[i] = pygame.transform.scale(self.bird_animations[i], 
				(self.bird_width, self.bird_height))

		# define index to cycle through bird images
		# define index to cycle through bird images at specific rate defined in settings. (settings.flap_rate)
		self.bird_image_index = 0
		self.flap_index = 0


		# load bird and rect
		self.bird_image = self.bird_animations[self.bird_image_index]
		self.rotated_bird = self.bird_image.copy()
		self.rect = self.bird_image.get_rect()

		# Initial bird location is at the center left of screen.
		self.rect.centerx = self.settings.start_pos
		self.rect.centery = self.settings.screen_height//2
		self.jump = False
		self.motion = 0


	def update(self): 
		self.motion += self.settings.gravity
		self.bird_image, self.rect = self.animation()
		self.rotate_bird()
		if self.jump:
			self.settings.flap_sound.play()
			self.motion = self.settings.jump_rate
			self.jump = False
		
		self.rect.centery += self.motion


	def blit_bird(self):
		self.update()
		self.screen.blit(self.rotated_bird, self.rect)

	def rotate_bird(self):
		self.rotated_bird = pygame.transform.rotate(self.bird_image, -self.motion*2)

	def animation(self):
		self.flap_index += 1
		# if flap_index equals flap_rate, change bird image
		if self.flap_index >= self.settings.flap_rate:
			self.flap_index = 0
			if self.bird_image_index < len(self.bird_animations)-1:
				self.bird_image_index += 1
			else:
				self.bird_image_index = 0

		new_bird = self.bird_animations[self.bird_image_index]
		new_bird_rect = new_bird.get_rect(center=(self.rect.centerx, self.rect.centery))
		return new_bird, new_bird_rect


	def reset(self):
		self.rect.centerx = self.settings.start_pos
		self.rect.centery = self.settings.screen_height//2

		self.jump = False
		self.motion = 0

