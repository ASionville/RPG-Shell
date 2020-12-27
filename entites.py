""" Module entites

	Contient les classe Entite, Ennemi et Joueur
"""
from utils import random_20

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