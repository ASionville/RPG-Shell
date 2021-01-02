"""Module plateau

	Contient les classes Salle et Plateau
"""
from entites import Ennemi
from objets import Nourriture, Argent

from random import randint
from utils import choix_ennemi, choix_objet, demander_mouvement

class Salle():

	"""	Classe Salle, représentant une Salle du Plateau
	Attributs:
		position (tuple) [privé] : Postion (x, y) de la salle
	    contenu (liste): Contenu de la pièce :
	    	Contenu[0] : Ennemi
	    	Contenu[1] : Objet (Argent/Nourriture)

	Méthodes :
		remplir_salle(x, y, taille): Ajoute du contenu à une salle
		get_position(): Récupère la position d'une salle sur le plateau
	"""
	
	def __init__(self, x:int, y:int, *contenu):
		"""	Fonction d'initialisation de la salle
		Args:
		    x (int): Position x de la pièce
		    y (int): Position y de la pièce
		    *contenu: Contenu de la pièce (cf Classe)
		"""
		self.__position = (x, y)

		#Contenu[ennemi, objet]
		self.contenu = [None, None]

	def remplir_salle(self, taille: int):
		"""	Fonction qui ajoute du contenu à une salle
		Args:
		    taille (int): Taille totale du plateau
		
		Retourne:
		    La salle, une fois remplie
		"""
		x, y = self.__position
		if x == 1 and y == 1:
			return
		if x == taille and y == taille:
			return
		else :
			if (choix_ennemi()):
				ennemi = Ennemi()
				self.contenu[0] = ennemi

			if choix_objet() == "Nourriture":
				objet = Nourriture()
			else:
				objet = Argent()
			self.contenu[1] = objet
		return self

	def get_position(self) -> tuple:
		"""	Fonction pour récupérer la position d'une salle sur le plateau
		Retourne:
		    position (tuple): tuple de position (x, y) 
		"""
		return self.__position

	def __str__(self):
		"""	Transformation Salle -> str
		Retourne:
		    str: "Salle X-Y" (X et Y positions respectives de la salle)
		"""
		return(f"Salle {self.get_position()[0]}-{self.get_position()[1]}")

class Plateau():

	"""	Classe Plateau, représentant le plateau de jeu
	Attributs:
	    matrice (list): Matrice contenant les salles du plateau
	    taille (int) [privé] : Taille du plateau (minimum : 7x7)
	    position_joueur (liste) [privé] : Position actuelle du joueur [x, y]

	Méthode:
		creer_matrice(taille): Créé la matrice des salles du plateau
		get_mouvements_possibles(position_joueur): Récupère les mouvements possible selon la position du joueur
		mouvement_joueur(): Fait déplacer le joueur
		vider_case_joueur() : Vide la case du joueur
		get_contenu_case_courante(): Récupère le contenu de la case où se situe le joueur
		get_position_joueur(): Récupère la position actuelle du joueur
		get_fin(): Dit si le joueur est arrivé à la fin du plateau (il a gagné)
	"""
	
	def __init__(self, taille:int):
		"""	Fonction d'initialisation du plateau
		Args:
		    taille (int): Taille totale du plateau
		"""
		self.matrice = []
		self.__taille = taille
		self.matrice = self.creer_matrice(self.__taille)
		self.__position_joueur = [6, 7]

	def creer_matrice(self, taille:int):
		"""	Fonction qui créé la matrice des salles du plateau
		Args:
		    taille (int): Taille totale du plateau
		
		Retourne:
		    matrice (list): Matrice contenant les salles du plateau
		"""
		# Création d'une matrice carrée de {taille} par {taille}
		matrice = [[Salle(i + 1, j + 1).remplir_salle(taille) for j in range(taille)] for i in range(taille)] 

		return matrice

	def get_mouvements_possibles(self, position_joueur: list):
		"""	Fonction qui récupère les mouvements possible selon la position du joueur
		afin qu'il le sorte pas du plateau
		Args:
		    position_joueur (list): Position actuelle du joueur [x, y]
		
		Retourne:
		    str: Texte représentant les mouvements possible
		    	Combinaison de 
		    		H : Aller vers le Haut
		    		B : Aller vers le Bas
		    		G : Aller à Gauche
		    		D : Aller à Droite
		"""
		ligne, col = position_joueur[0], position_joueur[1]
		mouvements_possibles = "HBGD"

		if ligne == 1 : # Sur la première ligne (en haut)
			mouvements_possibles = mouvements_possibles.replace("H", "")
		elif ligne == self.__taille: # Sur la dernière ligne (en bas)
			mouvements_possibles = mouvements_possibles.replace("B", "")

		if col == 1: # Sur la première colonne (à gauche)
			mouvements_possibles = mouvements_possibles.replace("G", "")
		elif col == self.__taille:# Sur la dernière colonne (à droite)
			mouvements_possibles = mouvements_possibles.replace("D", "")

		return mouvements_possibles

	def mouvement_joueur(self):
		"""	Fonction qui fait déplacer le joueur"""
		mouvement = demander_mouvement(self.get_mouvements_possibles(self.__position_joueur))
		if mouvement == "H":
			self.__position_joueur[0] -= 1
		elif mouvement == "B":
			self.__position_joueur[0] += 1
		elif mouvement == "G":
			self.__position_joueur[1] -= 1
		elif mouvement == "D":
			self.__position_joueur[1] += 1

	def vider_case_joueur(self):
		""" Fonction qui vide la case du joueur afin d'éviter des bugs de duplication
		"""

		self.matrice[self.__position_joueur[0]-1][self.__position_joueur[1]-1].contenu = [None, None]

	def get_contenu_case_courante(self):
		"""	Fonction qui récupère le contenu de la case où se situe le joueur
		Retourne:
		    list: Contenu de la salle courante
		"""
		return self.matrice[self.__position_joueur[0]-1][self.__position_joueur[1]-1].contenu

	def get_position_joueur(self):
		"""	Fonction qui récupère la position actuelle du joueur
		Retourne:
		    list: Position actuelle du joueur [x, y]
		"""
		return self.__position_joueur

	def get_fin(self):
		"""	Fonction qui dit si le joueur est arrivé à la fin du plateau (il a gagné)
		Retourne:
		    bool: Est ce que le joueur est à la dernière case
		"""
		return self.__position_joueur == [self.__taille, self.__taille]

	def __str__(self):
		"""	Transformation Plateau -> str
		Retourne:
		    Tableau graphique (en texte) avec le numéro de chaque salle
		"""
		txt = ''
		for i in range(self.__taille):
			for j in range(self.__taille):
				txt += "| " + str(self.matrice[i][j]) + " "
			txt += "\n"
		return txt