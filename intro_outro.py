"""	Module intro_outro

	Contient les fonctions pour le splashscreen, le texte d'introduction
	et les deux fins possibles (le joueur a gagné ou pas)
"""
from utils import _print

from pyfiglet import Figlet
from colorama import init, Fore, Style

#Nécessaire pour colorama
init(autoreset=True)

def splashscreen():
	""" Fonction qui écrit le splashscreen (écran d'accueil)
	"""
	f = Figlet(font='slant')
	txt = f.renderText("Le Tresor sous\n  la Montagne").split("\n")

	for ligne in txt:
		print(f"{Fore.YELLOW}{ligne}")

def get_texte_intro(taille: int):
	""" Fonction qui lit dans le fichier texte le texte d'intro
	
	Args:
	    taille (int): Taille du plateau
	
	Retourne:
	    str: Texte d'introduction
	"""
	return(open("files/intro.txt", encoding='utf-8').read().replace("X", str(taille)))

def fin_mort():
	""" Fonction qui écrit l'écran de fin si le joueur est mort
	"""
	f = Figlet(font='slant')
	txt = f.renderText("        FIN   \nTu es mort").split("\n")

	for ligne in txt:
		print(f"{Fore.RED}{ligne}")

def fin_victoire():
	""" Fonction qui écrit l'écran de fin si le joueur gagne
	"""
	f = Figlet(font='slant')
	txt = f.renderText("        FIN   \nTu a reussi").split("\n")

	for ligne in txt:
		print(f"{Fore.GREEN}{ligne}")
