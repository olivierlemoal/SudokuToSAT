#! /usr/bin/env python2
# -.- coding: utf-8 -.-
import string
import re
from sudoku_utils import c


class Sudoku():
    """
    Classe Sudoku contenant l'ordre, la grille et la taille de la grille
    """

    
    def __init__(self, ordre=0):        
        self.ordre = ordre
        self.size = self.ordre * self.ordre   
        self.grille = [[0 for j in xrange(0,self.size)] for i in xrange(0,self.size)]
        
    def openGrid(self, file):
        """
        Ouvre et parse un fichier texte contenant la grille 
        """
        with open(file, 'r') as f:
            self.ordre = int(f.readline())
            lines = [line.strip() for line in f.readlines()]

        self.size = self.ordre * self.ordre

        trans = string.maketrans('.','0')
        grille = []
        for i, line in enumerate(lines):
            if len(line)!=0:
                row = [int(x) for x in line.translate(trans).split()]
                if len(row) != self.size:
                    print "Grille malformée sur la ligne %d." % (i + 2)
                    exit()
                grille.append(row)

        if len(grille) != self.size:
            print "Grille incorrecte"
            exit()

        self.grille = grille

    def openResult(self, file):
        """
        Ouvre un fichier résultat de minisat, interprète la grille résultat, vérifie et l'affiche
        """

        def checkSol(i, j):
            for k in xrange(1, self.size + 1):
                if c(i, j, k, self) in res:
                    return k
        with open(file, 'r') as f:
            sat = f.readline()
            res = f.readline()
        res = re.sub("[^[0-7]]", " ",  res).split()[:-1] #récupère les valeurs sous forme de dictionnaire
        res = map(int, res) #converti en entiers


        for i in xrange(0, self.size):
            for j in xrange(0, self.size):
                self.grille[i][j] = checkSol(i, j) # Regarde pour chaque case la solution trouvée

        if self.checkGrille():
            print "Grille correcte !"
            self.printGrille()
        else:
            print "Erreur ! Grille incorrecte"
            try:
                self.printGrille()
            except:
                print "Impossible d'afficher la grille"

    def printGrille(self):
        """
        Affiche la grille sur l'entrée standard
        """
        str = ""
        for i, line in enumerate(self.grille):
            if i % self.ordre == 0:
                str += "\n"
            for j, case in enumerate(line):                
                if j % self.ordre == 0:
                    str += " "
                if j % self.size == 0:
                    str += "\n"
                str += "%d " % case
        print str

    def checkGrille(self):
        """
        Vérifie si la grille est correcte
        """

        # transpose la matrice contenant les lignes de la grille pour optenir les colonnes
        colonnes = zip(*self.grille)

        # liste des blocs
        blocs = []
        for i, line in enumerate(self.grille):
            for bloc in xrange(self.ordre):
                if not i % self.ordre: 
                    blocs.append([])
                blocs[bloc + i/self.ordre*self.ordre].extend(line[bloc * self.ordre : bloc * self.ordre + self.ordre])
        
        for i in xrange(0, self.size):
            if [x for x in [set(colonnes[i]), set(blocs[i]), set(self.grille[i])] if x != set(range(1, self.size+1))]: # Rappel : Les sets ne contiennent pas de doublons
                return False

        return True