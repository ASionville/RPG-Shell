""" Module entites

	Contient les classe Entite, Ennemi et Joueur
	Ainsi que la fonction de combat
"""
from utils import random_20, _print

from time import sleep
from random import randint
class Entite(object):
	"""docstring for Entite
	"""
	def __init__(self):
		"""Summary
		"""
		self.__vie = random_20()
		self.__force = random_20()
		self.__chance = random_20()
	
	def est_mort(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__vie <= 0

	def get_vie(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__vie

	def get_force(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__force

	def get_chance(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__chance

	def appliquer_degats(self, degats: int):
		"""Summary
		
		Args:
		    degats (int): Description
		"""
		self.__vie -= degats

class Ennemi(Entite):
	"""docstring for Ennemi
	"""
	def __init__(self):
		"""Summary
		"""
		super().__init__()

class Joueur(Entite):
	"""docstring for Joueur
	"""
	def __init__(self):
		"""Summary
		"""
		super().__init__()
		self.__fortune = 0

	def get_fortune(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__fortune

	def ramasser_argent(self, argent):
		"""Summary
		
		Args:
		    argent (TYPE): Description
		"""
		self.__fortune += argent.get_points()

	def manger(self, nourriture):
		"""Summary
		
		Args:
		    nourriture (TYPE): Description
		"""
		self._Entite__vie += nourriture.get_points()


def combat(JOUEUR, ennemi, COEFF_JOUEUR, COEFF_ENNEMI):
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