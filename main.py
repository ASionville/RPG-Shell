import entites
import objets
from plateau import Plateau
from musicmanager import MusicManager
from intro_outro import splashscreen, get_texte_intro, fin_mort, fin_victoire
from utils import demander_difficulte, demander_fuite, vider_console, _print

from time import sleep
from random import randint
from colorama import init, Fore, Style

##Initialisation
init(autoreset=True)

vider_console()
musicmanager = MusicManager()


##Introduction
splashscreen()
sleep(5)
vider_console()

COEFF_JOUEUR, COEFF_ENNEMI, TAILLE = demander_difficulte()
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

	#Récupérer mvmts possibles
	position_joueur = PLATEAU.get_position_joueur()
	
	#Déplacement et point sur l'état du joueur
	PLATEAU.mouvement_joueur()

	_print(f"\n\nTu entres dans la salle {position_joueur[0]}-{position_joueur[1]}", "jaune")
	_print(f"Ton état pour le moment :", "jaune")
	_print(f"Vie : {JOUEUR.get_vie()}\t\tForce : {JOUEUR.get_force()}\t\t\tFortune : {JOUEUR.get_fortune()}", "jaune")

	##Détection d'un ennemi
	contenu = PLATEAU.get_contenu_case_courante()
	ennemi = contenu[0]
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
				_print("Voyons ce qu'il y a dans cette pièce !", "jaune")
			else:
				_print("Nous n'avons pas réussi à nous échapper à temps, il va falloir combatre !", "rouge")
		
		else:

			##Boucle de combat
			while not (JOUEUR.est_mort() or ennemi.est_mort()):
				#Attaque du joueur sur l'ennemi
				degats = int((	JOUEUR.get_vie()*(randint(5,15)/10) +
								JOUEUR.get_force()*(randint(5,15)/10) +
								JOUEUR.get_chance()*(randint(5,15)/10))/3)

				#Le moins de dégats possible = 1 ou 2
				degats = int(min(degats * COEFF_JOUEUR, randint(1, 2)))

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
				degats = int(min(degats * COEFF_ENNEMI, randint(1, 2)))
				joueur.appliquer_degats(degats)
				_print(f"Tu as reçu {degats} points de dégats !", "rouge")
				_print(f"Il te reste {max(JOUEUR.get_vie(), 0)} points de vie", "rouge")
				sleep(3)

		musicmanager.end_bataille()

	if JOUEUR.est_mort():
		break

	#Si on fuit on ne récupère pas ce que protège l'ennemi
	if not fuite :
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
			#On enlève l'objet pour éviter la duplication si on revient
			contenu[1] = None

	#Pour laisser le temps de lire
	sleep(3)

#Fin du jeu
if joueur.est_mort():
	_print("Tu commences à sentir que tu ne vas pas y arriver, les coups de tes adversaires sont trop puissants", "rouge")
	_print("Tu vois tes amis tomber un par un, et puis tu te rends compte que tu es seul, seul contre l'ennemi", "rouge")
	_print("Malheureusement, celui-ci est trop fort, trop rapide, trop agile", "rouge")
	_print("Tes coups sont faibles, les siens fracas...", "rouge")

	sleep(0.8)
	fin_mort()

else:
	_print("Tu réalises ce que tu viens d'accomplir avec tes camarades", "rouge")
	_print("Vous avez vaincu chaque menace, et survécu jusqu'au trésor", "rouge")
	_print("Mais avant toute chose, il est temps de fêter ça avec les tiens", "rouge")

	sleep(0.8)
	fin_victoire()

print(f"Ton score : {JOUEUR.get_fortune()}")