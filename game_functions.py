import pygame
import sys
import random
from bird import Bird
from settings import Settings 
from background import Background
from score import Score 


def check_events(settings, screen, bird):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:			
			if event.key == pygame.K_SPACE:
				bird.jump = True

def check_collision(bird, bg_surface):
	if bird.rect.collidelist([bg_surface.pipe.rect_bp, bg_surface.pipe.rect_tp]) != -1:
		return True
	if bird.rect.bottom <= 0 or bird.rect.bottom >= bg_surface.floor_y_pos:
		return True
	return False
		
def update_screen(settings, screen, bird, bg_surface, score):
	bg_surface.blit_bg()
	bird.blit_bird()
	score.blit_score()
	pygame.display.flip()

def update_intro_screen(settings, screen, bg_surface, bird, score):
	intro_image = pygame.transform.scale(
		pygame.image.load('images/message.png').convert_alpha(),
		(settings.intro_width, settings.intro_height)
		)
	intro_rect = intro_image.get_rect(center=settings.mid_screen)
	bg_surface.blit_bg_intro()
	screen.blit(bird.bird_image, bird.rect)
	screen.blit(intro_image, intro_rect)
	score.blit_score_intro()
	display_options(settings, screen)
	pygame.display.flip()

def reset_window(settings):
	pygame.display.quit()
	pygame.display.set_mode((settings.screen_width, settings.screen_height))

def display_options(settings, screen):
	options_text = "Options:"
	screen_size_text = "Toggle Screen Size: '1', '2', '3'"
	bird_color_text = "Toggle Bird Color: 'b', 'r', 'y'"
	theme_text = "Toggle Theme: 'd', 'n'"
	options_surface = settings.game_font.render(options_text, True, settings.font_color)
	options_rect = options_surface.get_rect(topleft=(.05*settings.screen_width, .025*settings.screen_height))
	screen_size_surface = settings.game_font.render(screen_size_text, True, settings.font_color)
	screen_size_rect = screen_size_surface.get_rect(topleft=(.05*settings.screen_width, .05*settings.screen_height))
	bird_color_surface = settings.game_font.render(bird_color_text, True, settings.font_color)
	bird_color_rect = bird_color_surface.get_rect(topleft=(.05*settings.screen_width, .075*settings.screen_height))
	theme_surface = settings.game_font.render(theme_text, True, settings.font_color)
	theme_rect = theme_surface.get_rect(topleft=(.05*settings.screen_width, .1*settings.screen_height))
	screen.blit(options_surface, options_rect)
	screen.blit(screen_size_surface, screen_size_rect)
	screen.blit(bird_color_surface, bird_color_rect)
	screen.blit(theme_surface, theme_rect)

