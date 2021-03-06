import entites
import objets
from plateau import Plateau
from musicmanager import MusicManager
from filesmanager import check_fichiers_ok
from intro_outro import splashscreen, get_texte_intro, fin_mort, fin_victoire
from utils import demander_difficulte, demander_fuite, vider_console, _print,\
					enregister_score, get_scores

from time import sleep
from random import randint
from colorama import init, Fore, Style

##Initialisation
check_fichiers_ok()
init(autoreset=True)

vider_console()
musicmanager = MusicManager()

##Introduction
splashscreen()
sleep(5)
vider_console()

COEFF_JOUEUR, COEFF_ENNEMI, TAILLE, COEFF_SCORE = demander_difficulte()
vider_console()

PLATEAU = Plateau(TAILLE)
JOUEUR = entites.Joueur()
position_joueur = PLATEAU.get_position_joueur()
_print(get_texte_intro(TAILLE), "jaune")


##Faire un point sur l'état du joueur avant de commencer
_print(f"Tu commences dans la première salle", "jaune")
_print(f"Ton état pour le moment :", "jaune")
_print(f"Vie : {JOUEUR.get_vie()}\t\tForce : {JOUEUR.get_force()}\t\t\tFortune : {JOUEUR.get_fortune()}", "jaune")


##Boucle principale du jeu
while not(JOUEUR.est_mort()) or not(PLATEAU.get_fin()):

	vider_console()

	position_joueur = PLATEAU.get_position_joueur()
	
	#Déplacement et point sur l'état du joueur
	PLATEAU.mouvement_joueur()

	if PLATEAU.get_fin():
		break

	vider_console()

	_print(f"Tu entres dans la salle {position_joueur[0]}-{position_joueur[1]}", "jaune")
	_print(f"Ton état pour le moment :", "jaune")
	_print(f"Vie : {JOUEUR.get_vie()}\t\tForce : {JOUEUR.get_force()}\t\t\tFortune : {JOUEUR.get_fortune()}", "jaune")

	##Détection d'un ennemi
	contenu = PLATEAU.get_contenu_case_courante()
	ennemi = contenu[0]

	# Par défaut, pour éviter une erreur de variable non existante
	fuite = True

	if ennemi == None:
		_print("Ouf, pas d'ennemi en vue", "vert")

	else:
		musicmanager.start_bataille()
		_print("Attention Thorin ! Un ennemi !", "rouge")

		#Demander si le joueur veut fuire
		fuite = demander_fuite()
		if fuite:

			if JOUEUR.get_chance() > ennemi.get_chance():
				_print("Nous l'avons échappé belle !", "vert")
			else:
				_print("Nous n'avons pas réussi à nous échapper à temps, il va falloir combatre !", "rouge")
				entites.combat(JOUEUR, ennemi, COEFF_JOUEUR, COEFF_ENNEMI)

		else:
			entites.combat(JOUEUR, ennemi, COEFF_JOUEUR, COEFF_ENNEMI)
		musicmanager.end_bataille()

	if JOUEUR.est_mort():
		break

	#Si on fuit on ne récupère pas ce que protège l'ennemi
	if ennemi != None and not fuite :

		objet = contenu[1]
		if objet == None:
			_print("Dommage, il n'y a rien du tout ici", "jaune")

		else:
			_print("Oh, regardez là-bas, il y a quelque chose !", "jaune")
			_print(str(objet), "vert")

			if type(objet).__name__ == "Nourriture":
				JOUEUR.manger(objet)

			else:
				JOUEUR.ramasser_argent(objet)
	#On vide la case pour éviter la duplication si on revient
	PLATEAU.vider_case_joueur()

	#Pour laisser le temps de lire
	sleep(3)

vider_console()


#Fin du jeu
if JOUEUR.est_mort():
	_print("Tu commences à sentir que tu ne vas pas y arriver, les coups de tes adversaires sont trop puissants", "rouge")
	_print("Tu vois tes amis tomber un par un, et puis tu te rends compte que tu es seul, seul contre l'ennemi", "rouge")
	_print("Malheureusement, celui-ci est trop fort, trop rapide, trop agile", "rouge")
	_print("Tes coups sont faibles, les siens fracassants...", "rouge")

	sleep(0.8)
	vider_console()
	fin_mort()

else:
	_print("Tu réalises ce que tu viens d'accomplir avec tes camarades", "vert")
	_print("Vous avez vaincu chaque menace, et survécu jusqu'au trésor", "vert")
	_print("Mais avant toute chose, il est temps de fêter ça avec les tiens", "vert")

	sleep(0.8)
	vider_console()
	fin_victoire()

##Gestion des scores
print(f"Ton score : {JOUEUR.get_fortune()}")
enregister_score(JOUEUR.get_fortune(), COEFF_SCORE)

#Affichage de tous les meilleurs scores
print("\nTous les scores :")
for score in get_scores():
	print(score)

input()