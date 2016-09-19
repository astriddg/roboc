# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import os, shutil

from carte import Carte
from labyrinthe import Labyrinthe


def chargeLabs():
	""" Cette fonction a pour but de charger les jeux en cours s'ils existent, ou 
	d'appeler la fonction qui chargera les cartes d'origine
	"""
	if os.listdir('labs') and os.listdir('labs') != []:

		print('\r \n Il y a des parties enregistrées, voulez-vous continuer à jouer ?')
		labs = []
		for nom_fichier in os.listdir("labs"):
		    if nom_fichier.endswith(".txt"):
		        chemin = os.path.join("labs", nom_fichier)
		        nom_lab = nom_fichier[:-3].lower()
		        with open(chemin, "r") as fichier:
		            contenu = fichier.read()
		            carte = Carte(nom_fichier, contenu)
		            labs.append(carte)

		print("\rParties en cours :")
		for i, lab in enumerate(labs):
			print(" {}".format( lab.nom))

		choix = raw_input('O/N :  ')


		if choix == 'O':
			for i, lab in enumerate(labs):
				print("  {} - {}".format(i + 1, lab.nom))
			numero_lab = input('tapez le chiffre du labyrinthe choisi :') - 1
			lab = Labyrinthe(labs[numero_lab])

		elif choix == 'N':
			for nom_fichier in os.listdir("labs"):
				chemin = os.path.join("labs", nom_fichier)
				os.unlink(chemin)

			lab = chargeCartes()

	else:
		lab = chargeCartes()
	return lab


def chargeCartes():
	# Cette fonction charge les cartes d'origine.
	cartes = []
	for nom_fichier in os.listdir("cartes"):
	    if nom_fichier.endswith(".txt"):
	        chemin = os.path.join("cartes", nom_fichier)
	        nom_carte = nom_fichier[:-3].lower()
	        with open(chemin, "r") as fichier:
	            contenu = fichier.read()
	            carte = Carte(nom_fichier, contenu)
	            cartes.append(carte)

	# On affiche les cartes existantes
	print("\rLabyrinthes existants :")
	for i, carte in enumerate(cartes):
	    print("  {} - {}".format(i + 1, carte.nom))

	numero_lab = input('tapez le chiffre du labyrinthe choisi :') - 1
	lab = Labyrinthe(cartes[numero_lab])
	return lab



lab = chargeLabs()

print('Choisissez les options suivantes : \n - N pour monter \n - S pour descendre \n - O pour aller à gauche \n - E pour aller à droite \n - Q pour quitter')

choix = ''


while (choix.upper() != 'Q'): # Tant que le joueur n'a pas décidé de quitter la partie...
	print(lab) # ... On montre l'état du labyrinthe ...
	choix = raw_input('>') # ... On lui demande d'entrer une commande ...
	analyse = lab.analyse(choix) # ... L'objet lab l'analyse ...
	if analyse is True: # On sort le résultat.
		choix = 'Q'
		lab.finirJeu()
		print('Vous avez gagné !')
	elif analyse == 'On continue alors.':
		choix = 'C'
		print(analyse)
	else:
		print(analyse)


