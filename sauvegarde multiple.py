import numpy as np
from fonction import *
from valeur import *

def effectuer_calcul(tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant):
    nouveau_tableau1 = np.dot(tableau_calcul_x,tableau_milieu_aquatique)
    nouveau_tableau2 = np.dot(tableau_milieu_aquatique ,tableau_calcul_y)

    nouveau_tableau = np.add(nouveau_tableau1,nouveau_tableau2)
    nouveau_tableau = np.add(nouveau_tableau,tableau_constant)

    return nouveau_tableau
def lancer_les_calculs(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant):
    j=0
    num = 0
    for i in range(n):
        if(j==0):
            sauvegarder(tableau_milieu_aquatique,num,n)
            j = ecart
            num += 1
        j-=1
    
        tableau_milieu_aquatique = effectuer_calcul(tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant)
    creer_video(n,num-1)
    return tableau_milieu_aquatique


if(pourcentage):
    os.makedirs(f"video/pourcentage/D={D} ux={u_x} uy={u_y} taille={taille} deltaT{delta_t} deltaX{delta_x} deltaX{delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}/", exist_ok=True)
else:
    os.makedirs(f"video/valeur/D={D} ux={u_x} uy={u_y} taille={taille} deltaT{delta_t} deltaX{delta_x} deltaX{delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}/", exist_ok=True)


def initialisation_tableau_calcul_x():
    tableau_calcul_x = initialisation_tableau()
    for x in range(0,taille):
        for y in range(0,taille):
            if(y-x == -1):
                tableau_calcul_x[x][y] = (D*delta_t/delta_x**2) + delta_t*u_x/(2*delta_x)
            elif(y-x == 0):
                if(murBas and (x== taille -1 and y == taille-1)) :
                    tableau_calcul_x[x][y] = (1/2-1*D*delta_t/delta_x**2)
                elif(murHaut and (x== 0 and y == 0)) :
                    tableau_calcul_x[x][y] = (1/2-1*D*delta_t/delta_x**2)
                else :
                    tableau_calcul_x[x][y] = (1/2-2*D*delta_t/delta_x**2)
            elif(y-x == 1):
                tableau_calcul_x[x][y] = (D*delta_t/delta_x**2)-delta_t*u_x/(2*delta_x)
    # enleve les echanges avec l'exterieur du au courant
    tableau_calcul_x[0][0] += -delta_t*u_x/(2*delta_x)
    tableau_calcul_x[taille-1][taille-1] += delta_t*u_x/(2*delta_x)

    return tableau_calcul_x

def initialisation_tableau_calcul_y():
    # Initialisation du tableau de calcul en y
    tableau_calcul_y = initialisation_tableau()
    for x in range(0,taille):
        for y in range(0,taille):
            if(y-x == -1):
                tableau_calcul_y[x][y] = (D*delta_t/delta_y**2) - delta_t*u_y/(2*delta_y)
            elif(y-x == 0):
                if(murDroite and (x== taille -1 and y == taille-1)) :
                    tableau_calcul_y[x][y] = (1/2-1*D*delta_t/delta_y**2)
                elif(murGauche and (x== 0 and y == 0)) :
                    tableau_calcul_y[x][y] = (1/2-1*D*delta_t/delta_y**2)
                else :
                    tableau_calcul_y[x][y] = (1/2-2*D*delta_t/delta_y**2)
            elif(y-x == 1):
                tableau_calcul_y[x][y] = (D*delta_t/delta_y**2) + delta_t*u_y/(2*delta_y)
    # enleve les echanges avec l'exterieur du au courant
    tableau_calcul_y[0][0] += -delta_t*u_y/(2*delta_y)
    tableau_calcul_y[taille-1][taille-1] += delta_t*u_y/(2*delta_y)

    return tableau_calcul_y

def initialisation_tableau_calcul_x_ubis():

    # Initialisation du tableau de calcul en x
    tableau_calcul_x = initialisation_tableau()
    for x in range(0,taille):
        for y in range(0,taille):
            if(y-x == -1):
                if(u_x <=0):
                    tableau_calcul_x[x][y] = (D*delta_t/delta_x**2)
                elif (u_x >0) :
                    tableau_calcul_x[x][y] = (D*delta_t/delta_x**2) + delta_t*u_x/(2*delta_x)

            elif(y-x == 0):
                if(murBas and (x== taille -1 and y == taille-1)) :
                    tableau_calcul_x[x][y] = (1/2-1*D*delta_t/delta_x**2)
                elif(murHaut and (x== 0 and y == 0)) :
                    tableau_calcul_x[x][y] = (1/2-1*D*delta_t/delta_x**2)
                else :
                    tableau_calcul_x[x][y] = (1/2-2*D*delta_t/delta_x**2)

                if(u_x <0):
                    tableau_calcul_x[x][y] += delta_t*u_x/(2*delta_x)
                elif(u_x>0):
                    tableau_calcul_x[x][y] -= delta_t*u_x/(2*delta_x)


            elif(y-x == 1):
                if(u_x <0):
                    tableau_calcul_x[x][y] = (D*delta_t/delta_x**2) - delta_t*u_x/(2*delta_x)
                elif (u_x >=0) :
                    tableau_calcul_x[x][y] = (D*delta_t/delta_x**2)
    # enleve les echanges avec l'exterieur du au courant
    tableau_calcul_x[0][0] += -delta_t*u_x/(2*delta_x)
    tableau_calcul_x[taille-1][taille-1] += delta_t*u_x/(2*delta_x)

    return tableau_calcul_x


def initialisation_tableau_calcul_y_ubis():
    # Initialisation du tableau de calcul en y
    tableau_calcul_y = initialisation_tableau()
    for x in range(0,taille):
        for y in range(0,taille):
            if(y-x == -1):
                if(u_y <0):
                    tableau_calcul_y[x][y] = (D*delta_t/delta_y**2) - delta_t*u_y/(2*delta_y)
                elif (u_y >=0) :
                    tableau_calcul_y[x][y] = (D*delta_t/delta_y**2)

            elif(y-x == 0):
                if(murDroite and (x== taille -1 and y == taille-1)) :
                    tableau_calcul_y[x][y] = (1/2-1*D*delta_t/delta_y**2)
                elif(murGauche and (x== 0 and y == 0)) :
                    tableau_calcul_y[x][y] = (1/2-1*D*delta_t/delta_y**2)
                else :
                    tableau_calcul_y[x][y] = (1/2-2*D*delta_t/delta_y**2)

                if(u_y <0):
                    tableau_calcul_y[x][y] += delta_t*u_y/(2*delta_y)
                elif(u_y>0):
                    tableau_calcul_y[x][y] -= delta_t*u_y/(2*delta_y)
            
            elif(y-x == 1):
                if(u_y <=0):
                    tableau_calcul_y[x][y] = (D*delta_t/delta_y**2)
                elif (u_y >0) :
                    tableau_calcul_y[x][y] = (D*delta_t/delta_y**2) + delta_t*u_y/(2*delta_y)
    # enleve les echanges avec l'exterieur du au courant
    tableau_calcul_y[0][0] += -delta_t*u_y/(2*delta_y)
    tableau_calcul_y[taille-1][taille-1] += delta_t*u_y/(2*delta_y)

    return tableau_calcul_y

if(ubis):
    tableau_calcul_x = initialisation_tableau_calcul_x_ubis()
    tableau_calcul_y = initialisation_tableau_calcul_y_ubis()
else :
    tableau_calcul_x = initialisation_tableau_calcul_x()
    tableau_calcul_y = initialisation_tableau_calcul_y()

# convertir les tableaux en matrices
tableau_milieu_aquatique=np.matrix(tableau_milieu_aquatique)
tableau_milieu_aquatique = tableau_milieu_aquatique.transpose()

tableau_calcul_x=np.matrix(tableau_calcul_x)
tableau_calcul_y=np.matrix(tableau_calcul_y)

tableau_constant = initialisation_tableau_constant_2D()

tableau_constant=np.matrix(tableau_constant)

tableau_constant = tableau_constant.transpose()

tableau_milieu_aquatique = lancer_les_calculs(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant)


calcul_total(tableau_milieu_aquatique)
