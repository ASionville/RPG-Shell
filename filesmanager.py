"""Module filesmanager

Contient différentes fonction afin de vérifier la présence des fichiers nécessaires au jeu
Sert également à synchroniser les scores entre la version EXE et la version py

Fonction :
	check_fichiers_ok(): Vérifie que tous les fichiers sont présents
	message_erreur_fichier(): Affiche un message d'erreur et copie le lien git
	get_files_path() : Donne le chemin vers le dossier "files"
	get_music_path() : Donne le chemin vers le dossier "music"
"""
import pyperclip

from time import sleep
from os import getcwd, path


fichiers_needed = ["files/intro.txt", "files/scores.txt.bak", "files/scores.txt.dat",
					"files/scores.txt.dir", "music/bataille.mp3", "music/music.mp3"]
def check_fichiers_ok():
	""" Fonction qui vérifie que tous les fichiers soient présents
	"""
	for fichier in fichiers_needed:
		if not (path.exists(fichier) or path.exists("../" + fichier)):
			message_erreur_fichier()

	return True

def message_erreur_fichier():
	""" Fonction qui affiche un message d'erreur et copie le lien git
	"""
	print("\n\n\n")
	print("IL SEMBLERAIT QUE VOUS AYEZ UN PROBLEME AVEC LES FICHIERS DU JEU")
	print("VEUILLEZ TELECHARGER UNE VERSION COMPLETE VIA L'ADRESSE COPIEE DANS LE PRESSE-PAPIER")
	pyperclip.copy("https://github.com/ASionville/RPG-Shell")
	input()

def get_files_path():
	""" Fonction qui donne le chemin vers le dossier "files"

		Retourne : "files/" ou "../files/"
				(change si vous lancez le .py ou le .exe)
	"""
	check_fichiers_ok()
	for fichier in fichiers_needed:
		if fichier.split("/")[0] == "files":
			if path.exists(fichier):
				return "files/"
			else:
				return "../files/"

def get_music_path():
	""" Fonction qui donne le chemin vers le dossier "music"

		Retourne : "music/" ou "../music/"
				(change si vous lancez le .py ou le .exe)
	"""
	check_fichiers_ok()
	for fichier in fichiers_needed:
		if fichier.split("/")[0] == "music":
			if path.exists(fichier):
				return "music/"
			else:
				return "../music/"