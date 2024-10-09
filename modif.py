
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# D = 10**-1
D= 0.25
# si D*Delta t/delta x ** 2 > 1/4 c'est pas possible les cases polue plus que leur propre concentration
# si D*Delta t/delta y ** 2 > 1/4 c'est pas possible les cases polue plus que leur propre concentration

delta_x=1
delta_y=1

delta_t=1


taille_x=20
taille_y=20

u=0

# true : mur Newman
# false : filtre Dirichlet
murGauche = True
murDroite = True
murHaut = True
murBas =True


n=200

if((D*delta_t)/(delta_x**2)>1/4):
    print("propagation trop elever en x")
if((D*delta_t)/(delta_y**2)>1/4):
    print("propagation trop elever en y")


tableau_milieu_aquatique_initial = [[] for y in range(taille_y)]


for x in range(0,taille_x):
    for y in range(0,taille_y):
        tableau_milieu_aquatique_initial[x].append(0)



tableau_milieu_aquatique = tableau_milieu_aquatique_initial


def afficherGraphic(tab):

    fig,ax=plt.subplots()
    ax.imshow(tab)

    ax.set_xticks(np.arange(0,taille_x))
    ax.set_yticks(np.arange(0,taille_y))
	
    colors = ["#000c57","#0051ff","#00f7ff","#00ffa2","#00ff08","#9dff00","#ffff00","#ffdd00","#ffa600","#ff5100","#ff0000"]
    custom_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom_cmap",colors)

    plt.imshow(tab,cmap=custom_cmap)
    cbar = plt.colorbar()

    plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")

    ax.set_title("Propagation d'un poluant")
    fig.tight_layout()
    plt.show()

def afficher (tableau_milieu_aquatique):
    print("\n")
    for x in range(0,taille_x):
        print(tableau_milieu_aquatique[x])
    print("\n")

# afficher (tableau_milieu_aquatique)

def get(i,j,tableau_milieu_aquatique_n):
    # filtre
    if(i+1>taille_x-1 or i-1< 0 or j+1 >taille_y-1 or j-1 <0):
        return 0
    
    return tableau_milieu_aquatique_n[i][j]

def C(i,j,tableau_milieu_aquatique_n):
    newC = 0
    newC= get(i,j,tableau_milieu_aquatique_n)

    droite,gauche,haut,bas = 1,1,1,1
    if(murBas):
        if(get(i+1,j,tableau_milieu_aquatique_n)==0):
            bas = 0
    if(murHaut):
        if(get(i-1,j,tableau_milieu_aquatique_n) == 0):
            haut = 0
    if(murDroite):
        if(get(i,j+1,tableau_milieu_aquatique_n)==0):
            droite = 0
    if(murGauche):
        if(get(i,j-1,tableau_milieu_aquatique_n)==0):
            gauche = 0
    newC+= ((D*delta_t)/(delta_x**2))*(get(i+1,j,tableau_milieu_aquatique_n)-droite*get(i,j,tableau_milieu_aquatique_n)-gauche*get(i,j,tableau_milieu_aquatique_n)+get(i-1,j,tableau_milieu_aquatique_n))
    newC+= ((D*delta_t)/(delta_y**2))*(get(i,j+1,tableau_milieu_aquatique_n)-haut*get(i,j,tableau_milieu_aquatique_n)-bas*get(i,j,tableau_milieu_aquatique_n)+get(i,j-1,tableau_milieu_aquatique_n))
    newC-= delta_t*u*((get(i+1,j,tableau_milieu_aquatique_n)-get(i-1,j,tableau_milieu_aquatique_n))/(2*delta_x) + (get(i,j+1,tableau_milieu_aquatique_n)-get(i,j-1,tableau_milieu_aquatique_n))/(2*delta_y))
    return newC

def actualiser(tableau_milieu_aquatique):
    nouveau_tableau = [[] for y in range(taille_y)]

    # Polution permanente
    # nouveau_tableau[4][4] = 1

    for x in range(0,taille_x):
        for y in range(0,taille_y):
            nouveau_tableau[x].append(0)

    for x in range(1,taille_x-1):
        for y in range(1,taille_y-1):
            nouveau_tableau[x][y] = C(x,y,tableau_milieu_aquatique)
    return nouveau_tableau

tableau_milieu_aquatique[4][4] = 1
tableau_milieu_aquatique[4][5] = 1
tableau_milieu_aquatique[5][4] = 1
tableau_milieu_aquatique[5][5] = 1


def tourner(n,tableau_milieu_aquatique):
    for i in range(n):
        tableau_milieu_aquatique = actualiser(tableau_milieu_aquatique)
    return tableau_milieu_aquatique
# tableau_milieu_aquatique[5][5] = C(5,5,tableau_milieu_aquatique)

# afficher (tableau_milieu_aquatique)

tableau_milieu_aquatique = tourner(n,tableau_milieu_aquatique)
afficherGraphic(tableau_milieu_aquatique)

# tourner(100,tableau_milieu_aquatique)
# afficherGraphic(tableau_milieu_aquatique)