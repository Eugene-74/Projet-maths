
import numpy as np
import matplotlib.pyplot as plt

D= 0.25

delta_x=1

delta_t=1


taille_x=10

u=0

# true : mur Newman
# false : filtre Dirichlet
murGauche = True
murDroite = True
murHaut = True
murBas =True


n=1000


tableau_milieu_aquatique_initial = []


for x in range(0,taille_x):
    # for y in range(0,taille_y):
    tableau_milieu_aquatique_initial.append(0)



tableau_milieu_aquatique = tableau_milieu_aquatique_initial


def afficherGraphic(tab):

    fig,ax=plt.subplots()
    im = ax.imshow(tab)

    # ax.set_xticks(np.arange(0,taille_x))
    # ax.set_yticks(np.arange(0,taille_y))

    plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")

    ax.set_title("Propagation d'un poluant")
    fig.tight_layout()
    plt.show()

def afficher (tableau_milieu_aquatique):
    print("\n")
    # for x in range(0,taille_x):
    print(tableau_milieu_aquatique)
    print("\n")




def actualiser(tableau_milieu_aquatique,tableau_calcul,tableau_constant):
    # nouveau_tableau = []
    nouveau_tableau = np.dot(tableau_calcul,tableau_milieu_aquatique)

    nouveau_tableau = np.add(nouveau_tableau,tableau_constant)

    # nouveau_tableau = tableau_milieu_aquatique

# TODO faire les matrices



    return nouveau_tableau



def tourner(n,tableau_milieu_aquatique,tableau_calcul,tableau_constant):
    for i in range(n):
        tableau_milieu_aquatique = actualiser(tableau_milieu_aquatique,tableau_calcul,tableau_constant)
    return tableau_milieu_aquatique



tableau_calcul = [[] for y in range(taille_x)]

for x in range(0,taille_x):
    for y in range(0,taille_x):
        if(y-x == -1):
            tableau_calcul[x].append(D*delta_t/delta_x**2)
        elif(y-x == 0):
            tableau_calcul[x].append(1-2*D*delta_t/delta_x**2)
        elif(y-x == 1):
            tableau_calcul[x].append(D*delta_t/delta_x**2)
        else :
            tableau_calcul[x].append(0)

tableau_milieu_aquatique[4] = 1

tableau_milieu_aquatique=np.matrix(tableau_milieu_aquatique)

tableau_milieu_aquatique = tableau_milieu_aquatique.transpose()

tableau_calcul=np.matrix(tableau_calcul)

tableau_constant = []

for x in range(0,taille_x):
    # for y in range(0,taille_y):
    tableau_constant.append(0)

tableau_constant=np.matrix(tableau_constant)

tableau_constant = tableau_constant.transpose()


# MODIFIER TABLEAU CONSTANT POUR AVOIR DES MURS ET PAS DES FILTRES




afficher(tableau_calcul)


afficher(tableau_milieu_aquatique)



tableau_milieu_aquatique = tourner(n,tableau_milieu_aquatique,tableau_calcul,tableau_constant)


afficher(tableau_milieu_aquatique)

# afficherGraphic(tableau_milieu_aquatique)