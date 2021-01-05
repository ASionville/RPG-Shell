"""Module musicmanager

Contient une classe MusicManager, qui gère la musique en arrière-plan durant le jeu
"""

import pygame
from filesmanager import get_music_path

VOLUME_AMBIANCE = 0.2
VOLUME_BATAILLE = 0.3

class MusicManager():

	"""	Classe MusicManager, gère la musique
	Attributs:
	    channel1 (pygame.mixer.Channel) : Canal audio de la musique d'ambiance
	    channel2 (pygame.mixer.Channel) : Canal audio de la musique de combat
		musique_ambiance : Son mp3 issu du dossier music/, musique d'ambiance
		musique_bataille : Son mp3 issu du dossier music/, musique de combat

	Méthode:
		start_bataille() : Changement de musique au début d'un combat
		end_bataille() : Changement de musique à la fin d'un combat
	"""
	
	def __init__(self):
		""" Fonction d'initialisation du gestionaiire de musiques
		"""
		pygame.mixer.init()

		self.channel1 = pygame.mixer.Channel(0)
		self.channel2 = pygame.mixer.Channel(1)

		self.channel1.set_volume(VOLUME_AMBIANCE)
		self.channel2.set_volume(VOLUME_BATAILLE)

		path = get_music_path()

		self.musique_ambiance = pygame.mixer.Sound(path +"music.mp3")
		self.musique_bataille = pygame.mixer.Sound(path + "bataille.mp3")
		
		self.channel1.play(self.musique_ambiance)


	def start_bataille(self):
		""" Fonction de changement de musique au début d'un combat
		"""
		self.channel2.play(self.musique_bataille, fade_ms=500)
		self.channel1.pause()

	def end_bataille(self):
		"""Fonction de changement de musique à la fin d'un combat
		"""
		self.channel1.unpause()
		self.channel2.stop()
