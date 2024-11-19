import numpy as np
import matplotlib.colors as cols
import matplotlib.pyplot as plt
from valeur import *

def afficherGraphicEtSauvegarder(tab):
        
    if(pourcentage) :
        tab = tab / np.max(tab) * 100
        tab = np.round(tab, 2)

    
    fig, ax = plt.subplots()
    im = ax.imshow(tab, cmap='viridis', interpolation='nearest')
    
    if(pourcentage) :
        cbar = plt.colorbar(im, ax=ax, format='%.2f%%')
        im.set_clim(0, 100)
    else :
        cbar = plt.colorbar(im, ax=ax, format='%.2f')

    if(pourcentage) :
        cbar.ax.set_ylabel('Concentration par rapport au maximum', rotation=-90, va="bottom")
    else :
        cbar.ax.set_ylabel('Concentration', rotation=-90, va="bottom")

    fig.tight_layout()

    if(sauvegarderImage):
        if(pourcentage):
            filename = f"images/pourcentage/D={D} ux={u_x} uy={u_y} taille={taille} n={n}.png"
        else:
            filename = f"images/valeur/D={D} ux={u_x} uy={u_y} taille={taille} n={n}.png"

        plt.savefig(filename)
    if(afficherVisuel):
        plt.show()





        

def afficher (tableau_milieu_aquatique):
    if(afficherTableau):
        print("\n")
        for x in range(0,taille):
            print(tableau_milieu_aquatique[x])
        print("\n")

def verification_CFL_1D():
    if(verifierLesConditionCFL):
        if((2*D)*((delta_t/delta_x**2))>1):
            print("\033[91mpropagation trop elever en x ou en y\033[0m")
            exit()
        if(abs(u_x) > (2*D)*(delta_t/delta_x)):
            print("\033[91mcourant trop elever en x\033[0m")
            exit()

        if((2*D)*((delta_t/delta_x**2)) == 1):
            print("\033[92mpropagation limite en x ou en y\033[0m")
        if(abs(u_x) == (2*D)*(delta_t/delta_x)):
            print("\033[92mcourant limite en x\033[0m")


def verification_CFL_2D():
    if(verifierLesConditionCFL):
        if((2*D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))>1):
            print("\033[91mpropagation trop elever en x ou en y\033[0m")
            exit()
        if(abs(u_x) > (2*D)*(delta_t/delta_x)):
            print("\033[91mcourant trop elever en x\033[0m")
            exit()
        if(abs(u_y) > (2*D)*(delta_t/delta_y)):
            print("\033[91mcourant trop elever en y\033[0m")
            exit()

        if((2*D)*((delta_t/delta_x**2)+(delta_t/delta_y**2)) == 1):
            print("\033[92mpropagation limite en x ou en y\033[0m")
        if(abs(u_x) == (2*D)*(delta_t/delta_x)):
            print("\033[92mcourant limite en x\033[0m")
        if(abs(u_y) == (2*D)*(delta_t/delta_y)):
            print("\033[92mcourant limite en y\033[0m")




def calcul_total(tab):
    if isinstance(tab, np.ndarray):
        total = np.sum(tab)
    else:
        total = sum(sum(row) for row in tab)
    afficher(tab)
    print("total : " + str(total))


