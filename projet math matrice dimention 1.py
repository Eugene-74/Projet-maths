
import numpy as np
import matplotlib.pyplot as plt

D= 0.25

delta_x=1
delta_y=1

delta_t=1


taille_x=10
taille_y=10

u=0

# true : mur Newman
# false : filtre Dirichlet
murGauche = True
murDroite = True
murHaut = True
murBas =True


n=100


tableau_milieu_aquatique_initial = [[] for y in range(taille_y)]


for x in range(0,taille_x):
    # for y in range(0,taille_y):
    tableau_milieu_aquatique_initial.append(0)



tableau_milieu_aquatique = tableau_milieu_aquatique_initial


def afficherGraphic(harvest):

    fig,ax=plt.subplots()
    im = ax.imshow(harvest)

    # ax.set_xticks(np.arange(0,taille_x))
    # ax.set_yticks(np.arange(0,taille_y))

    plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")

    ax.set_title("Propagation d'un poluant")
    fig.tight_layout()
    plt.show()

def afficher (tableau_milieu_aquatique):
    print("\n")
    for x in range(0,taille_x):
        print(tableau_milieu_aquatique[x])
    print("\n")


def get(i,j,tableau_milieu_aquatique_n):
    # filtre
    if(i+1>taille_x-1 or i-1< 0 or j+1 >taille_y-1 or j-1 <0):
        return 0
    
    return tableau_milieu_aquatique_n[i][j]


def actualiser(tableau_milieu_aquatique):
    nouveau_tableau = [[] for y in range(taille_y)]

    # Polution permanente
    # nouveau_tableau[4][4] = 1

    # for x in range(0,taille_x):
        # for y in range(0,taille_y):
            # nouveau_tableau[x].append(0)

    for x in range(1,taille_x-1):
        for y in range(1,taille_y-1):
            nouveau_tableau[x][y] = C(x,y,tableau_milieu_aquatique)
    return nouveau_tableau

tableau_milieu_aquatique[4] = 1



afficherGraphic(tableau_milieu_aquatique)