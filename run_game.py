import pygame
import sys
import random
from bird import Bird
from settings import Settings 
from background import Background
from score import Score
import game_functions as gf



def game_intro(settings, screen, bg_surface, bird, scale, bird_color, theme, score):
	intro = True

	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:			
				if event.key == pygame.K_SPACE:
					intro=False
					score.reset()
				if event.key == pygame.K_1:
					run_game(scale=1, bird_color=bird_color, theme=theme, curr_score=score.score, curr_high_score=score.high_score)
				if event.key == pygame.K_2:
					run_game(scale=1.5, bird_color=bird_color, theme=theme, curr_score=score.score, curr_high_score=score.high_score)
				if event.key == pygame.K_3:
					run_game(scale=2, bird_color=bird_color, theme=theme, curr_score=score.score, curr_high_score=score.high_score)
				if event.key == pygame.K_b:
					run_game(scale=scale, bird_color='blue', theme=theme, curr_score=score.score, curr_high_score=score.high_score)
				if event.key == pygame.K_r:
					run_game(scale=scale, bird_color='red', theme=theme, curr_score=score.score, curr_high_score=score.high_score)
				if event.key == pygame.K_y:
					run_game(scale=scale, bird_color='yellow', theme=theme, curr_score=score.score, curr_high_score=score.high_score)
				if event.key == pygame.K_d:
					run_game(scale=scale, bird_color=bird_color, theme='day', curr_score=score.score, curr_high_score=score.high_score)
				if event.key == pygame.K_n:
					run_game(scale=scale, bird_color=bird_color, theme='night', curr_score=score.score, curr_high_score=score.high_score)

		gf.update_intro_screen(settings, screen, bg_surface, bird, score)


def run_game(scale=1.5, bird_color='blue', theme='day', curr_score=0, curr_high_score=0):
	# Initialize pygame, settings, screen bird and background.
	pygame.init()
	clock = pygame.time.Clock()
	settings = Settings(scale)
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	bg_surface = Background(settings, screen, theme=theme)
	bird = Bird(settings, screen, color=bird_color)
	score = Score(settings, screen, score=curr_score, high_score=curr_high_score)

	# load intro screen
	game_intro(settings, screen, bg_surface, bird, scale, bird_color, theme, score)
	while True:
		
		score.add_score()
		gf.check_events(settings, screen, bird)
		gf.update_screen(settings, screen, bird, bg_surface, score)
		if gf.check_collision(bird, bg_surface):
			settings.death_sound.play()
			bird.reset()
			bg_surface.reset()
			score.update_high_score()
			game_intro(settings, screen, bg_surface, bird, scale, bird_color, theme, score)


		clock.tick(120) #set the refresh rate to 120 Hz

run_game()
