import pygame

VOLUME_AMBIANCE = 0.2
VOLUME_BATAILLE = 0.3

class MusicManager():
	def __init__(self):

		pygame.mixer.init()

		self.channel1 = pygame.mixer.Channel(0)
		self.channel2 = pygame.mixer.Channel(1)

		self.channel1.set_volume(VOLUME_AMBIANCE)
		self.channel2.set_volume(VOLUME_BATAILLE)

		self.musique_ambiance = pygame.mixer.Sound("music/music.mp3")
		self.musique_bataille = pygame.mixer.Sound("music/bataille.mp3")
		
		self.channel1.play(self.musique_ambiance)


	def start_bataille(self):
		self.channel2.play(self.musique_bataille, fade_ms=500)
		self.channel1.pause()

	def end_bataille(self):
		self.channel1.unpause()
		self.channel2.stop()
