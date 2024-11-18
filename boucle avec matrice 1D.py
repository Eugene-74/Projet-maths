import numpy as np
import matplotlib.pyplot as plt
from fonction import *
from valeur import *


verification_CFL_1D()


def effectuer_calcul(tableau_milieu_aquatique,tableau_calcul_x,tableau_constant):
    nouveau_tableau = np.dot(tableau_calcul_x,tableau_milieu_aquatique)
    nouveau_tableau = np.add(nouveau_tableau,tableau_constant)

    return nouveau_tableau



def lancer_les_calculs(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_constant):
    for i in range(n):
        tableau_milieu_aquatique = effectuer_calcul(tableau_milieu_aquatique,tableau_calcul_x,tableau_constant)
    return tableau_milieu_aquatique

# Initialisation du tableau de calcul en x
tableau_calcul_x = initialisation_tableau()
for x in range(0,taille):
    for y in range(0,taille):
        if(y-x == -1):
            tableau_calcul_x[x][y] = (D*delta_t/delta_x**2) + delta_t*u_x/(2*delta_x)
        elif(y-x == 0):
            if(murBas and (x== taille -1 and y == taille-1)) :
                tableau_calcul_x[x][y] = (1-1*D*delta_t/delta_x**2)
            elif(murHaut and (x== 0 and y == 0)) :
                tableau_calcul_x[x][y] = (1-1*D*delta_t/delta_x**2)
            else :
                tableau_calcul_x[x][y] = (1-2*D*delta_t/delta_x**2)
        elif(y-x == 1):
            tableau_calcul_x[x][y] = (D*delta_t/delta_x**2) - delta_t*u_x/(2*delta_x)

# convertir les tableaux en matrices
tableau_milieu_aquatique=np.matrix(tableau_milieu_aquatique)
tableau_calcul_x=np.matrix(tableau_calcul_x)

tableau_constant = initialisation_tableau_constant_1D()

afficher(tableau_constant)


tableau_constant=np.matrix(tableau_constant)

afficher(tableau_calcul_x)

afficher(tableau_milieu_aquatique)

tableau_milieu_aquatique = lancer_les_calculs(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_constant)

afficher(tableau_milieu_aquatique)

afficherGraphic(tableau_milieu_aquatique)

calcul_total(tableau_milieu_aquatique)
