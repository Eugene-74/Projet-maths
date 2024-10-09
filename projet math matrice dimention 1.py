
import numpy as np
import matplotlib.pyplot as plt

D= 0.10

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


n=4


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




def actualiser(tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant):
    nouveau_tableau1 = np.dot(tableau_calcul_x,tableau_milieu_aquatique)
    nouveau_tableau2 = np.dot(tableau_milieu_aquatique ,tableau_calcul_y)

    nouveau_tableau = np.add(nouveau_tableau1,nouveau_tableau2)
    
    # nouveau_tableau = np.add(nouveau_tableau,nouveau_tableau2)
    
    
    nouveau_tableau = np.add(nouveau_tableau,tableau_constant)


    return nouveau_tableau



def tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant):
    for i in range(n):
        tableau_milieu_aquatique = actualiser(tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant)
    return tableau_milieu_aquatique



tableau_calcul_x = [[] for y in range(taille_x)]

for x in range(0,taille_x):
    for y in range(0,taille_x):
        if(y-x == -1):
            tableau_calcul_x[x].append((D*delta_t/delta_x**2))
        elif(y-x == 0):
            tableau_calcul_x[x].append((1/2-2*D*delta_t/delta_x**2))
        elif(y-x == 1):
            tableau_calcul_x[x].append((D*delta_t/delta_x**2))
        else :
            tableau_calcul_x[x].append(0)

tableau_calcul_y = [[] for y in range(taille_x)]

for x in range(0,taille_x):
    for y in range(0,taille_x):
        if(y-x == -1):
            tableau_calcul_y[x].append((D*delta_t/delta_y**2))
        elif(y-x == 0):
            tableau_calcul_y[x].append((1/2-2*D*delta_t/delta_y**2))
        elif(y-x == 1):
            tableau_calcul_y[x].append((D*delta_t/delta_y**2))
        else :
            tableau_calcul_y[x].append(0)



        

tableau_milieu_aquatique[4][4] = 1

tableau_milieu_aquatique=np.matrix(tableau_milieu_aquatique)

tableau_milieu_aquatique = tableau_milieu_aquatique.transpose()

tableau_calcul_x=np.matrix(tableau_calcul_x)
tableau_calcul_y=np.matrix(tableau_calcul_y)


tableau_constant = [[] for y in range(taille_x)]

for x in range(0,taille_x):
    for y in range(0,taille_x):
        tableau_constant[x].append(0)

tableau_constant=np.matrix(tableau_constant)

tableau_constant = tableau_constant.transpose()


# MODIFIER TABLEAU CONSTANT POUR AVOIR DES MURS ET PAS DES FILTRES




afficher(tableau_calcul_x)


afficher(tableau_milieu_aquatique)



tableau_milieu_aquatique = tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant)


afficher(tableau_milieu_aquatique)

afficherGraphic(tableau_milieu_aquatique)

def calcul(tab):
    total = 0
    afficher(tab)
    for x in range(0,taille_x):
        for y in range(0,taille_y):
            total += tab[x,y]
    print("total : "+str(total))
    
calcul(tableau_milieu_aquatique)