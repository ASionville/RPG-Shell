"""Module utils

	Contient des fonctions qui seront utilisées par d'autres modules
	Ne contient pas de classe
"""
import time
import click

from os import system, name
from random import choice, randint
from colorama import init, Fore, Style

def random_20():
	""" Fonction aléatoire modifiée pour un résultat entier entre 1 et 20
	
	Retourne:
	    int: nombre aléatoire : 1 <= x <= 20
	"""
	hasard =  	[1] * 9 + [2] * 9 + [3] * 9\
				 + [4] * 8 + [5] * 8 + [6] * 8\
				 + [7] * 7 + [8] * 7 + [9] * 6\
				 + [10] * 5 + [11] * 5 + [12] * 4\
				 + [13] * 3 + [14] * 3 + [15] * 2\
				 + [16] * 2 + [17] * 2 + [18] * 1\
				 + [19] * 1 + [20] * 1
	return choice(hasard)

def random_5():
	""" Fonction aléatoire modifiée pour un résultat entier entre 1 et 5
	
	Retourne:
	    int: nombre aléatoire : 1 <= x <= 5
	"""
	hasard = [1] * 6 + [2] * 5 + [3] * 4 + [4] * 3 + [5] * 2
	return choice(hasard)

def choix_ennemi():
	""" Fonction qui dit au hasard si un ennemi est présent dans une salle
		3 chances sur 5 pour oui
		2 chances sur 5 pour non
	
	Retourne:
	    bool: Ennemi présent ou pas
	"""
	hasard = [True] * 3 + [False] * 2
	return choice(hasard)

def choix_objet():
	""" Fonction qui dit au hasard quel objet est présent dans une salle
		2 chances sur 8 pour Rien
		3 chances sur 8 pour Nourriture
		3 chances sur 8 pour Argent
	
	Retourne:
	    bool: Ennemi présent ou pas
	"""
	hasard = ["Rien"] * 2 + ["Nourriture"] * 3 + ["Argent"] * 3
	return choice(hasard)

def demander_difficulte():
	""" Fonction qui demande au joueur de choisir la difficulté du jeu
		et calcule certains paramètre du jeu selon cette difficulté

	Retourne:
	    tuple: 	Coefficient d'attaque du joueur (int)
				Coefficient d'attaque de l'ennemi (int)
				Taille du plateau (int)
	"""
	difficulte = ""
	while difficulte not in [1, 2, 3]:
		click.echo('Avec quelle difficulte veux-tu jouer ? [1/2/3] ', nl=False)
		c = click.getchar()
		click.echo()
		if (c.upper() == "1"):
			_print('Niveau Facile', "vert")
			difficulte = 1
			coeff_joueur = 2
			coeff_ennemi = 5
			taille = 7
		elif (c.upper() == "2"):
			_print('Niveau Moyen', "jaune")
			difficulte = 2
			coeff_joueur = 3
			coeff_ennemi = 3
			taille = 8
		elif (c.upper() == "3"):
			_print('Niveau Difficile', "rouge")
			difficulte = 3
			coeff_joueur = 4
			coeff_ennemi = 2
			taille = 10
		else:
			print('Entrée invalide :(')

	return coeff_joueur, coeff_ennemi, taille

def demander_mouvement(mvmts_possibles: str):
	""" Fonction qui demande au joueur le mouvement qu'il souhaite effectuer
	
	Args:
	    mvmts_possibles (str): Mouvements que le joueur peut faire
	
	Retourne:
	    str: Mouvement choisi par le joueur
	    	H : Aller vers le Haut
		    B : Aller vers le Bas
		    G : Aller à Gauche
		    D : Aller à Droite
	"""
	mouvement = ""
	mouvements_to_fr = {"H":'Monter', "B":"Descendre", "G":"Aller à gauche", "D":"Aller à droite"}
		
	while mouvement == "" or mouvement not in "HBGD":
		print('Tu peux :')
		for mvmt in mvmts_possibles:
			print(f"- {mouvements_to_fr[mvmt]}")
		click.echo('Où aller ? [ZQSD / Flèches] ', nl=False)
		c = click.getchar()
		click.echo()
		if (c == '\xe0H' or c.upper() == "Z") and "H" in mvmts_possibles:
			mouvement = "H"
		elif (c == '\xe0K' or c.upper() == "Q") and "G" in mvmts_possibles:
			mouvement = "G"
		elif (c == '\xe0P' or c.upper() == "S") and "B" in mvmts_possibles:
			mouvement = "B"
		elif (c == '\xe0M' or c.upper() == "D") and "D" in mvmts_possibles:
			mouvement = "D"
		else:
			click.echo('Entrée invalide ou mouvement impossible :(')
	return mouvement

def demander_fuite():
	""" Fonction qui demande au joueur s'il veut fuire un ennemi ou pas
	
	Retourne:
	    bool: Le joueur veut fuire ou pas
	"""
	fuite = ""
	while fuite not in [True, False]:
		click.echo('Tenter de fuir ? [O/N] ', nl=False)
		c = click.getchar()
		click.echo()
		if (c.upper() == "O"):
			_print('Fuyez, pauvres fous !', "jaune")
			fuite = True
		elif (c.upper() == "N"):
			_print('Il faut tenir !!', "rouge")
			fuite = False
		else:
			print('Entrée invalide :(')
	return fuite

def vider_console():
	""" Fonction qui vide la console
	"""
	#Windows 
	if name == 'nt': 
		system('cls') 
  
	#Mac/Linux
	else: 
		system('clear') 

def _print(text: str, couleur="blanc", nouvelle_ligne_apres=True):
	""" Fonction print modifiée pour écrire du texte en couleur
	
	Args:
	    text (str): Texte à écrire
	    couleur (str, option): Couleur du texte à écrire
	    nouvelle_ligne_apres (bool, option): Est ce qu'il faut écrire sur une nouvelle ligne après ou pas
	"""
	#Dico des codes couleurs
	style={	"jaune":Fore.YELLOW, "rouge":Fore.RED,
			"vert":Fore.GREEN, "blanc":Fore.WHITE}

	#Effet "tapé"
	for lettre in text:
		print(f"{style[couleur] if couleur in style.keys() else ''}{lettre}", end="")
		time.sleep(randint(3, 13)/100)

	#Délai et nouvelle ligne
	time.sleep(0.4)
	if nouvelle_ligne_apres:
		print("")