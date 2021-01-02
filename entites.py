""" Module entites

	Contient les classe Entite, Ennemi et Joueur
	Ainsi que la fonction de combat
"""
from utils import random_20, _print

from time import sleep
from random import randint


class Entite(object):
	
	"""	Classe Entite, représentant une Entité du jeu
	Attributs:
		vie (int) [privé] : Points de vie
	    force (int) [privé] : Points de force
	    chance (int) [privé] : Points de chance

	Méthodes :
		est_mort() : Dit si l'entité est morte ou pas
		get_vie() : Donne les points de vie de l'entité
		get_force() : Donne les points de force de l'entité
		get_chance() : Donne les points de chance de l'entité
		appliquer_degats(degats) : Applique des dégats à l'entité
	"""

	def __init__(self):
		""" Fonction d'initialisation de l'entité
		"""
		self.__vie = random_20()
		self.__force = random_20()
		self.__chance = random_20()
	
	def est_mort(self):
		""" Fonction qui dit si l'entité est morte ou pas
		
		Retourne:
		    bool: Est ce que l'entité est morte ou non
		"""
		return self.__vie <= 0

	def get_vie(self):
		""" Fonction qui donne les points de vie de l'entité
		
		Retourne:
		    int: Nombre de points de vie
		"""
		return self.__vie

	def get_force(self):
		""" Fonction qui donne les points de force de l'entité
		
		Retourne:
		    int: Nombre de points de force
		"""
		return self.__force

	def get_chance(self):
		""" Fonction qui donne les points de chance de l'entité
		
		Retourne:
		    int: Nombre de points de chance
		"""
		return self.__chance

	def appliquer_degats(self, degats: int):
		""" Fonction qui applique des dégats à l'entité
		
		Args:
		    degats (int): Nombre de points de vie à retirer
		"""
		self.__vie -= degats

class Ennemi(Entite):
	"""	Classe Ennemi, représentant un Ennemi du jeu
	Hérite de tous les attributs et de toutes les méthodes de Entite
	"""
	def __init__(self):
		""" Fonction d'initialisation de l'ennemi
		"""
		super().__init__()

class Joueur(Entite):
	"""	Classe Joueur, représentant le joueur dans le jeu
	Hérite de tous les attributs et de toutes les méthodes de Entite
	Attributs:
	    fortune (int) [privé] : Quantité d'argent possédé par le joueur (points de fortune)

	Méthodes :
		get_fortune() : Donne les points de fortune du joueur
		ramasser_argent(argent) : Ajoute au joueur la quantité d'argent (cf objets.py)
		manger(nourriture) : Ajoute des points de vie au joueur par la nourriture (cf objets.py)
	"""
	def __init__(self):
		""" Fonction d'initialisation du joueur
		"""
		super().__init__()
		self.__fortune = 0

	def get_fortune(self):
		""" Donne les points de fortune du joueur
		
		Retourne:
		    int: Points de fortune du joueur
		"""
		return self.__fortune

	def ramasser_argent(self, argent):
		"""Ajoute au joueur la quantité d'argent (cf objets.py)
		
		Args:
		    argent (Argent): Quantité d'argent (cf objets.py)
		"""
		self.__fortune += argent.get_points()

	def manger(self, nourriture):
		"""Ajoute au joueur la quantité de nourriture (cf objets.py)
		
		Args:
		    nourriture (Nourriture): Quantité de nourriture (cf objets.py)
		"""
		self._Entite__vie += nourriture.get_points()




def combat(JOUEUR, ennemi, COEFF_JOUEUR, COEFF_ENNEMI):
	""" Fonction de combat entre le joueur et un ennemi
	
	Args:
	    JOUEUR (Joueur): Le joueur qui combat
	    ennemi (Ennemi): L'ennemi qui combat

		#Voir demander_difficulte dans utils.py
	    COEFF_JOUEUR (float/int): Le coefficient d'attaque du joueur
	    COEFF_ENNEMI (float/int): Le coefficient d'attaque de l'ennemi
	
	Returns:
	    tuple: Le joueur et l'ennemi
	"""
	##Boucle de combat
	while not JOUEUR.est_mort():
		#Attaque du joueur sur l'ennemi
		degats = int((	JOUEUR.get_vie()*(randint(5,15)/10) +
						JOUEUR.get_force()*(randint(5,15)/10) +
						JOUEUR.get_chance()*(randint(5,15)/10))/3)

		#Le moins de dégats possible = 1 ou 2
		degats = int(max(degats * COEFF_JOUEUR, randint(1, 2)))

		ennemi.appliquer_degats(degats)
		_print(f"Tu as infligé {degats} points de dégats à l'ennemi !", "vert")
		_print(f"Il lui reste {max(ennemi.get_vie(), 0)} points de vie\n", "vert")
		sleep(3)

		if ennemi.est_mort():
			break

		#Attaque de l'ennemi sur le joueur
		degats = int((	ennemi.get_vie()*(randint(5,15)/10) +
						ennemi.get_force()*(randint(5,15)/10) +
						ennemi.get_chance()*(randint(5,15)/10))/3)

		#Le moins de dégats possible = 1 ou 2
		degats = int(max(degats * COEFF_ENNEMI, randint(1, 2)))
		JOUEUR.appliquer_degats(degats)
		_print(f"Tu as reçu {degats} points de dégats !", "rouge")
		_print(f"Il te reste {max(JOUEUR.get_vie(), 0)} points de vie", "rouge")
		sleep(3)

	return JOUEUR, ennemi