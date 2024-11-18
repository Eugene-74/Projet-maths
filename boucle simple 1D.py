import numpy as np
import matplotlib.pyplot as plt
from fonction import *
from valeur import *

verification_CFL_1D()


def get(i,j,tableau_milieu_aquatique_n):
    if(i>=taille_x or i< 0 or j >=taille_x or j <0):
        return 0
    return tableau_milieu_aquatique_n[i][j]

def C(i,j,tableau_milieu_aquatique_n):
    newC = 0
    newC= get(i,j,tableau_milieu_aquatique_n)

    droite,gauche = 1,1
    if(murDroite):
        if(j==taille_x-1):
            droite = 0
    if(murGauche):
        if(j==0):
            gauche = 0
    newC+= ((D*delta_t)/(delta_x**2))*(get(i+1,j,tableau_milieu_aquatique_n)-droite*get(i,j,tableau_milieu_aquatique_n)-gauche*get(i,j,tableau_milieu_aquatique_n)+get(i-1,j,tableau_milieu_aquatique_n))
    newC-= delta_t*u_x*((get(i+1,j,tableau_milieu_aquatique_n)-get(i-1,j,tableau_milieu_aquatique_n))/(2*delta_x))
    return newC

def effectuer_calcul(tableau_milieu_aquatique):
    nouveau_tableau = initialisation_tableau_constant()

    for x in range(0,taille_x):
        for y in range(0,taille_x):
            nouveau_tableau[x][y] = C(x,y,tableau_milieu_aquatique)
    return nouveau_tableau

afficher(tableau_milieu_aquatique)

def lancer_les_calculs(n,tableau_milieu_aquatique):
    for i in range(n):
        tableau_milieu_aquatique = effectuer_calcul(tableau_milieu_aquatique)
    return tableau_milieu_aquatique

tableau_milieu_aquatique = lancer_les_calculs(n,tableau_milieu_aquatique)

afficher(tableau_milieu_aquatique)
afficherGraphic(tableau_milieu_aquatique)

calcul_total(tableau_milieu_aquatique)
