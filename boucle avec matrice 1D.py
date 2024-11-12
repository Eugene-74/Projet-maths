

import numpy as np
import matplotlib.pyplot as plt

D= 0.2

delta_x=1
delta_y=1

delta_t=1


taille_x=10

# Si u est grand le schema n'est pas adapté
# Les murs ne marche pas non plus
u=0.1

# Mur impossible pour l
# true : mur Newman
# false : filtre Dirichlet
murHaut = True
murBas =True


n=1

if(2*D)*((delta_t/delta_x**2)<=1):

    tableau_milieu_aquatique_initial = [[] for y in range(taille_x)]
    for x in range(0,taille_x):
        for y in range(0,taille_x):
            tableau_milieu_aquatique_initial[x].append(0)



    tableau_milieu_aquatique = tableau_milieu_aquatique_initial


    def afficherGraphic(tab):

        fig,ax=plt.subplots()
        im = ax.imshow(tab)

        plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")

        ax.set_title("Propagation d'un poluant")
        fig.tight_layout()
        plt.show()

    def afficher (tableau_milieu_aquatique):
        print("\n")
        for x in range(0,taille_x):
            print(tableau_milieu_aquatique[x])
        print("\n")




    def actualiser(tableau_milieu_aquatique,tableau_calcul_x,tableau_constant):
        nouveau_tableau = np.dot(tableau_calcul_x,tableau_milieu_aquatique)

        nouveau_tableau = np.add(nouveau_tableau,tableau_constant)

        return nouveau_tableau



    def tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_constant):
        for i in range(n):
            tableau_milieu_aquatique = actualiser(tableau_milieu_aquatique,tableau_calcul_x,tableau_constant)
        return tableau_milieu_aquatique



    tableau_calcul_x = [[] for y in range(taille_x)]

    for x in range(0,taille_x):
        for y in range(0,taille_x):
            if(y-x == -1):
                tableau_calcul_x[x].append((D*delta_t/delta_x**2) + delta_t*u/(2*delta_x))
            elif(y-x == 0):
                if(murBas and (x== taille_x -1 and y == taille_x-1)) :
                    tableau_calcul_x[x].append((1-1*D*delta_t/delta_x**2))
                elif(murHaut and (x== 0 and y == 0)) :
                    tableau_calcul_x[x].append((1-1*D*delta_t/delta_x**2))
                else :
                    tableau_calcul_x[x].append((1-2*D*delta_t/delta_x**2))
            elif(y-x == 1):
                tableau_calcul_x[x].append((D*delta_t/delta_x**2) - delta_t*u/(2*delta_x))

            else :
                tableau_calcul_x[x].append(0)


            

    tableau_milieu_aquatique[2][2] = 1

    tableau_milieu_aquatique=np.matrix(tableau_milieu_aquatique)

    tableau_milieu_aquatique = tableau_milieu_aquatique.transpose()

    tableau_calcul_x=np.matrix(tableau_calcul_x)


    tableau_constant = [[] for y in range(taille_x)]

    for x in range(0,taille_x):
        for y in range(0,taille_x):
            tableau_constant[x].append(0)
    
    # for x in range(0,taille_x):
    #     for y in range(0,taille_y):
    #         if(x==0 or x==taille_x-1):
    #             tableau_constant[x][y]=1
    #         if(y==0 or y==taille_y-1):
    #             tableau_constant[x][y]=1

    afficher(tableau_constant)


    tableau_constant=np.matrix(tableau_constant)

    tableau_constant = tableau_constant.transpose()


    # MODIFIER TABLEAU CONSTANT POUR AVOIR DES MURS ET PAS DES FILTRES




    afficher(tableau_calcul_x)


    afficher(tableau_milieu_aquatique)



    tableau_milieu_aquatique = tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_constant)


    afficher(tableau_milieu_aquatique)

    afficherGraphic(tableau_milieu_aquatique)

    def calcul(tab):
        total = 0
        afficher(tab)
        for x in range(0,taille_x):
            for y in range(0,taille_x):
                total += tab[x,y]
        print("total : "+str(total))
        
    calcul(tableau_milieu_aquatique)
else :
    print("\033[91mpropagation trop elever en x ou en y\033[0m")