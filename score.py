import pygame
import shelve
from settings import Settings 

class Score:
	def __init__(self, settings, screen, score=0, high_score=0):
		self.settings = settings
		self.screen = screen
		self.score = score
		self.high_score = high_score
		self.all_time_high_score = self.get_all_time_high_score()
		self.score_pos = (self.settings.screen_width*.5, self.settings.screen_height*.97)
		self.score_surface = self.settings.score_font.render(str(int(self.score)), True, self.settings.font_color)
		self.score_rect = self.score_surface.get_rect(center=self.score_pos)

	def add_score(self):
		self.score += .1

	def blit_score(self):
		self.score_surface = self.settings.score_font.render(str(int(self.score)), True, self.settings.font_color)
		self.score_rect = self.score_surface.get_rect(center=self.score_pos)
		self.screen.blit(self.score_surface, self.score_rect)

	def blit_score_intro(self):
		self.score_surface = self.settings.score_font.render(f'Score: {int(self.score)}', True, self.settings.font_color)
		self.score_rect = self.score_surface.get_rect(topleft=(self.settings.screen_width*.05, self.settings.screen_height*.75))
		self.high_score_surface = self.settings.score_font.render(f'High Score: {int(self.high_score)}', True, self.settings.font_color)
		self.high_score_rect = self.score_surface.get_rect(topleft=(self.settings.screen_width*.05, self.settings.screen_height*.80))
		self.all_time_high_score_surface = self.settings.score_font.render(f'Record High Score: {int(self.all_time_high_score)}', True, self.settings.font_color)
		self.all_time_high_score_rect = self.score_surface.get_rect(topleft=(self.settings.screen_width*.05, self.settings.screen_height*.85))
		self.screen.blit(self.score_surface, self.score_rect)
		self.screen.blit(self.high_score_surface, self.high_score_rect)
		self.screen.blit(self.all_time_high_score_surface, self.all_time_high_score_rect)


	def update_high_score(self):
		if self.score > self.high_score:
			self.high_score = self.score
		self.set_all_time_high_score()

	def get_all_time_high_score(self):
		d = shelve.open('high_scores')

		if 'high_score' not in d:
			d['high_score'] = 0

		
		return d['high_score']

	def set_all_time_high_score(self):
		if self.high_score > self.all_time_high_score:
			self.all_time_high_score = self.high_score
			d = shelve.open('high_scores')

			d['high_score'] = self.all_time_high_score


	def reset(self):
		self.score = 0
		