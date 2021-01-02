"""Module objet

	Contient les classes Objet, Nourriture et Argent
"""
from utils import random_5

class Objet():
	"""	Classe Objet
		Sert de classe mère pour les objets précis

	Attributs :
		points (int) [privé] : Nombre de points (valeur) de l'objet
	"""
	def __init__(self):
		""" Fonction d'initialisation d'un objet
		"""
		self.__points = random_5()

	def get_points(self):
		""" Fonction qui récupère le nombre de points (la valeur) d'un objet
		
		Retourne:
		    int: Nombre de points
		"""
		return self.__points

class Nourriture(Objet):
	""" Classe Nourriture, représentant de la nourriture présente dans une salle
		Classe Fille de la classe Objet

	Attributs: 
		cf classe Objet

	Méthodes :
		cf classe Objet
	"""
	def __init__(self):
		"""Summary
		"""
		super().__init__()

	def __str__(self):
		""" Transformation Nourriture -> str
		
		Retourne:
		    str: Texte descriptif de la nourriture
		"""
		txt = f"Eh, regarde Thorin ! De la viande !\n(+{self.get_points()} points de vie)"
		return txt	

class Argent(Objet):
	"""	Classe Argent, représentant des pièces d'or présentes dans une salle
		Classe Fille de la classe Objet
		
	Attributs: 
		cf classe Objet

	Méthodes :
		cf classe Objet
	"""
	def __init__(self):
		"""Summary
		"""
		super().__init__()

	def __str__(self):
		"""	Transformation Argent -> str
		
		Retourne:
		    str: Texte descriptif de l'argent
		"""
		txt = f"Oh ça brille! Des écus, ce sont des écus !\n(+{self.get_points()} points de fortune)"
		return txt	