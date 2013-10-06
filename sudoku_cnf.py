# -.- coding: utf-8 -.-
from sudoku_utils import c


class CNF():

    """
    Classe CNF contenant les clauses ainsi que les méthodes pour générer
    les clauses.
    """
#

    def __init__(self, sudoku):
        """
        On instancie la classe avec une grille de sudoku et on calcul les clauses
        """
        self.clauses = []
        self.sudoku = sudoku
        self.clauses_sudoku()
        self.clauses_codage_case()
        self.clauses_horizontal_vertical()
        self.clauses_sousmatrices()


    def clauses_sudoku(self):
        """
        Génère les clauses de la grille à résoudre (cases déjà remplies)
        """
        for i in xrange(0, self.sudoku.size):
            for j in xrange(0, self.sudoku.size):
                valeur = int(self.sudoku.grille[i][j])
                if valeur:
                    self.clauses.append([c(i, j, valeur, self.sudoku)])

    def valid(self, cells):
        """
        Génère les clauses pour un tableau 9x9 (si d'ordre 3, ou 4x4 pour ordre 2).
        Le tableau peut ainsi contenir les lignes, colonnes ou blocs.
        Cette méthode est donc utilisée par les méthodes clauses_horizontal_vertical et clauses_sousmatrices
        qui génèrent les matrices 9x9 désirées.
        """
        for i, xi in enumerate(cells):
            for j, xj in enumerate(cells):
                if i < j:
                    for d in range(1, self.sudoku.size + 1):
                        self.clauses.append(
                            [-c(xi[0], xi[1], d, self.sudoku), -c(xj[0], xj[1], d, self.sudoku)])

    def clauses_horizontal_vertical(self):
        """
        Génère les clauses pour les contraintes :
        - Les lignes ont des valeurs distinctes
        - Les colonnes ont des valeurs distinctes
        """
        for i in xrange(0, self.sudoku.size):
            self.valid([(i, j) for j in xrange(0, self.sudoku.size)])  # Lignes
            self.valid([(j, i)
                       for j in xrange(0, self.sudoku.size)])  # Colonnes

    def clauses_sousmatrices(self):
        """
        Génère les clauses pour les contraintes :
        - Les sous matrices ont des valeurs distinctes
        """
        blocs = [self.sudoku.ordre * x for x in xrange(self.sudoku.ordre)]
        for i in blocs:
            for j in blocs:
                self.valid([(i + k % self.sudoku.ordre, j + k // self.sudoku.ordre)
                           for k in xrange(self.sudoku.size)])  # Sous matrices

    def clauses_codage_case(self):
        """
        Génère les clauses pour les contraintes :
        - Au moins une valeur est vraie pour chaque case
        - Au plus une valeur est vraie pour chaque case
        """
        for i in xrange(0, self.sudoku.size):
            for j in xrange(0, self.sudoku.size):
                # Au moins une valeur vraie
                self.clauses.append([c(i, j, d, self.sudoku)
                                    for d in xrange(1, self.sudoku.size + 1)])
                # Au plus une valeur vraie
                for val in xrange(1, self.sudoku.size + 1):
                    for val2 in xrange(val + 1, self.sudoku.size + 1):
                        self.clauses.append(
                            [-c(i, j, val, self.sudoku), -c(i, j, val2, self.sudoku)])

    def toFile(self, file):
        """
        Sauve les clauses dans un fichier au format DIMACS CNF
        """
        f = open(file, 'w')
        str = ""
        for clause in self.clauses:
            for c in clause:
                str += "%d " % c
            str += "0\n"
        f.write(str)
