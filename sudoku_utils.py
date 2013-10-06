# -.- coding: utf-8 -.-


def c(x, y, k, sudoku):
        """
        Fonction de codage des cases en fonction de la taille de grille
        Renvoie la valeur de la case (x,y) avec le chiffre k.
        """
        return k + sudoku.size * x + sudoku.size**2 * y
