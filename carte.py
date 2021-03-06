# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        lab = []
        import re
        for line in re.split('\r\n|\n', chaine):
            lab.append(list(line))
        return lab

