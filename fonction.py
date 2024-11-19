import numpy as np
import matplotlib.colors as cols
import matplotlib.pyplot as plt
from valeur import *


def afficherMatplotlib(tab:list or np.matrix,len_x:int,len_y:int):
    """Permet d'afficher un tableau de valeur de taille len_x
    Préconditions :
     - Un tableau sous forme de list ou de numpy.matrix
    """
    fig,ax = plt.subplots()
    im = ax.imshow(tab)

    ax.set_xticks(np.arange(0,len_x))
    ax.set_yticks(np.arange(0,len_y))

    colors = ["#000c57","#0051ff","#00f7ff","#00ffa2","#00ff08","#9dff00","#ffff00","#ffdd00","#ffa600","#ff5100","#ff0000"]
    custom_cmap = cols.LinearSegmentedColormap.from_list("custom_cmap",colors)

    plt.imshow(tab,cmap=custom_cmap)
    cbar = plt.colorbar()

    plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")

    ax.set_title("Propagation d'un polluant")
    fig.tight_layout()
    plt.show()




def afficherGraphic(tab):
    if(afficherVisuel):
        
        # Normalize the data by the maximum value
        tab = tab / np.max(tab) * 100
        if(arondire) :
            tab = np.round(tab, arondie)

        
        fig, ax = plt.subplots()
        im = ax.imshow(tab, cmap='viridis', interpolation='nearest')

        # Create a colorbar with a specific format
        cbar = plt.colorbar(im, ax=ax, format='%.2f')
        cbar.ax.set_ylabel('Concentration (%)', rotation=-90, va="bottom")

        fig.tight_layout()
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


