#! /usr/bin/env python2
# -.- coding: utf-8 -.-
import sys
import os

from sudoku_model import Sudoku
from sudoku_cnf import CNF


if __name__ == '__main__':

    if (len(sys.argv) < 2):
        print "Usage: python sudoku.py <fichier contenant la grille>"
        exit()

    iFile = sys.argv[1]
    cnfFile = 'clauses.cnf'
    resultFile = 'result'

    sudoku = Sudoku()
    try:
        sudoku.openGrid(iFile)
    except:
        print "Erreur lors de la lecture du fichier grille"
        exit()

    cnf = CNF(sudoku)
    cnf.toFile(cnfFile)

    exe = "minisat " + cnfFile + " " + resultFile

    try:
        os.system(exe)
    except:
        print "Erreur lors du lancement de minisat. Est-il correctement installé ?"
        exit()

    sudokuResponse = Sudoku(sudoku.ordre)
    sudokuResponse.openResult(resultFile)
