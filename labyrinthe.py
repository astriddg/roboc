# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, carte):
		self.grille = carte.labyrinthe
		self.position_actuelle = self.trouverX(carte.labyrinthe)
		self.nom_lab = carte.nom
		self.case_remplacee = None
		self.en_cours = False

	def __repr__(self): # Fonction qui définit ce qui sortira quand on mettra print(lab)
		self.etat = ''
		for row in self.grille:
			self.etat += ''.join(row)
			self.etat += '\n'

		return self.etat

	def analyse(self, choix): 
		""" Fonction d'analyse de la commande du joueur """
		if choix.upper() not in ['Q', 'E', 'W', 'N', 'S']:
			return 'Vous n\'avez pas rentré la bonne lettre.'
		if choix.upper() == 'Q':
			if raw_input('Etes-vous sûr de quitter le jeu ? O/N  ') == 'O': 
				self.en_cours = False 
				lefichier = self.nom_lab # On enregistre la partie.
				with open("labs/" + lefichier, "w") as fichier:
					fichier.write(self.__repr__())

				return 'Vous quittez le jeu.'
			else:
				return 'On continue alors.'

		position_voulue = self.donnerPosition(choix) # On calcule la position associée à la demande du joueur

		if position_voulue[0] < 0 or position_voulue[1] < 1 or position_voulue[0] >= len(self.grille) or position_voulue[1] >= len(self.grille[0]):
			# Là, le robot sort du jeu
			return 'Vous cherchez à sortir du labyrinthe'

		case = self.grille[position_voulue[0]][position_voulue[1]]
		if case == 'O':
			return'Vous foncez dans un mur.'
		if case == '.' or case == ' ':
			# de ici...
			if self.case_remplacee is None:
				self.grille[self.position_actuelle[0]][self.position_actuelle[1]] = ' '
			else:
				self.grille[self.position_actuelle[0]][self.position_actuelle[1]] = self.case_remplacee

			self.case_remplacee = case
			# ... à ici, c'est pour s'assurer que quand le robot quitte une case, elle redeviendra porte 
			# ou case vide en fonction de ce qu'elle était à l'origine.
			# Ci-dessous on bouge le X et on enregistre sa position.
			self.grille[position_voulue[0]][position_voulue[1]] = 'X'
			self.position_actuelle[0] = position_voulue[0]
			self.position_actuelle[1] = position_voulue[1]
			return ' '

		if case == 'U':
			self.en_cours = False
			return True


	def trouverX(self, labyrinthe):
		# Cette fonction est pour savoir au début du jeu où se trouve X
		for kr, row in enumerate(labyrinthe):
			for ke, elt in enumerate(row):
				if elt == 'X':
					position = [kr, ke]
					return position



	def donnerPosition(self, choix):
		""" Où la commande du joueur mène-t-elle le robot ? """
		choix = choix.upper()
		if choix == 'E':
			position_voulue = []
			position_voulue.append(self.position_actuelle[0])
			position_voulue.append(self.position_actuelle[1] + 1)
		if choix == 'W':
			position_voulue = []
			position_voulue.append(self.position_actuelle[0])
			position_voulue.append(self.position_actuelle[1] - 1)
		if choix == 'N':
			position_voulue = []
			position_voulue.append(self.position_actuelle[0] - 1)
			position_voulue.append(self.position_actuelle[1])
		if choix == 'S':
			position_voulue = []
			position_voulue.append(self.position_actuelle[0] + 1)
			position_voulue.append(self.position_actuelle[1])

		return position_voulue

	def finirJeu(self):
		# Là on supprime les parties enregistrées sur ce labyrinthe s'il y en a.
		import os
		if os.path.isfile("labs/" + self.nom_lab):
			os.remove("labs/" + self.nom_lab)
		return True










