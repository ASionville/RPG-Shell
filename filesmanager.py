import pyperclip

from time import sleep
from os import getcwd, path


fichiers_needed = ["files/intro.txt", "files/scores.txt.bak", "files/scores.txt.dat",
					"files/scores.txt.dir", "music/bataille.mp3", "music/music.mp3"]
def check_fichiers_ok():
	for fichier in fichiers_needed:
		if not (path.exists(fichier) or path.exists("../" + fichier)):
			message_erreur_fichier()

	return True

def message_erreur_fichier():
	print("\n\n\n")
	print("IL SEMBLERAIT QUE VOUS AYEZ UN PROBLEME AVEC LES FICHIERS DU JEU")
	print("VEUILLEZ TELECHARGER UNE VERSION COMPLETE VIA L'ADRESSE COPIEE DANS LE PRESSE-PAPIER")
	pyperclip.copy("https://github.com/ASionville/RPG-Shell")
	input()

def get_files_path():
	check_fichiers_ok()
	for fichier in fichiers_needed:
		if fichier.split("/")[0] == "files":
			if path.exists(fichier):
				return "files/"
			else:
				return "../files/"

def get_music_path():
	check_fichiers_ok()
	for fichier in fichiers_needed:
		if fichier.split("/")[0] == "music":
			if path.exists(fichier):
				return "music/"
			else:
				return "../music/"