SudokuToSAT
===========

Sudoku solver using minisat.


Français
--------


### Dépendance 
minisat < http://minisat.se/ >

Le programme a été développé avec le langage Python dans sa branche 2.
### Utilisation 

        python sudoku.py <fichier grille à résoudre>
ou python2 selon la distribution.

Le fichier contenant la grille doit être sous la forme suivante :

        3
        . 8 .  . . 1  . 6 5
        1 . 6  . . .  4 9 3
        . . .  . . .  . 1 2

        . 1 5  . 4 9  . . .
        . 6 .  1 . 2  . 3 .
        . . .  7 3 .  6 5 .

        8 3 .  . . .  . . .
        9 7 1  . . .  3 . 6
        6 5 .  8 . .  . 2 .

Avec l'ordre n de la grille en première ligne.
Les . remplacent les valeurs inconnues. Les valeurs connues sont numérotées de 1 à n^2 
et séparées d'un espace.

Le programme est livré avec 4 grilles :

* sudoku2 : une grille d'ordre 2
* sudoku3 : une grille d'ordre 3
* sudoku3_hard : une grille d'ordre 3 jugée difficile
* sudoku3_hardest : une grille d'ordre 3 jugée très difficile.
* sudoku4 : une grille d'ordre 4
* sudoku5 : une grille d'ordre 5
