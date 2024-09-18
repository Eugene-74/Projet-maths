
import numpy as np
import matplotlib.pyplot as plt

D = 10**-2

delta_x=1
delta_y=1

delta_t=1


taille_x=10
taille_y=10

u=0


tableau_milieu_aquatique_initial = [[] for y in range(taille_y)]


for x in range(0,taille_x):
    for y in range(0,taille_y):
        tableau_milieu_aquatique_initial[x].append(0)



tableau_milieu_aquatique = tableau_milieu_aquatique_initial


def afficherGraphic(harvest):

    fig,ax=plt.subplots()
    im = ax.imshow(harvest)

    ax.set_xticks(np.arange(0,taille_x))
    ax.set_yticks(np.arange(0,taille_y))

    plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")

    ax.set_title("Test")
    fig.tight_layout()
    plt.show()

def afficher (tableau_milieu_aquatique):
    print("\n")
    for x in range(0,taille_x):
        print(tableau_milieu_aquatique[x])
    print("\n")

afficher (tableau_milieu_aquatique)

def get(i,j,tableau_milieu_aquatique_n):
    # if x<0 or x>len(tableau_milieu_aquatique_n)-1:
    #     return 0
    # if y<0 or y>len(tableau_milieu_aquatique_n)-1:
    #     return 0
    # return tableau_milieu_aquatique_n[x][y]
    if(i+1>taille_x-1 or i-1< 0 or j+1 >taille_y-1 or j-1 <0):
        return 0
    
    return tableau_milieu_aquatique_n[i][j]

def C(i,j,tableau_milieu_aquatique_n):
    newC = 0
    # if(i+1<taille_x and i-1> 0 and j+1 <taille_y and j-1 >0):
    newC= get(i,j,tableau_milieu_aquatique_n)
    newC+= ((D*delta_t)/(delta_x**2))*(get(i+1,j,tableau_milieu_aquatique_n)-2*get(i,j,tableau_milieu_aquatique_n)+get(i-1,j,tableau_milieu_aquatique_n))
    newC+= ((D*delta_t)/(delta_y**2))*(get(i,j+1,tableau_milieu_aquatique_n)-2*get(i,j,tableau_milieu_aquatique_n)+get(i,j-1,tableau_milieu_aquatique_n))
    newC-= delta_t*u*((get(i+1,j,tableau_milieu_aquatique_n)-get(i-1,j,tableau_milieu_aquatique_n))/(2*delta_x) + (get(i,j+1,tableau_milieu_aquatique_n)-get(i,j-1,tableau_milieu_aquatique_n))/(2*delta_y))
    return newC

def actualiser(tableau_milieu_aquatique):
    nouveau_tableau = [[] for y in range(taille_y)]
    for x in range(0,taille_x):
        for y in range(0,taille_y):
            nouveau_tableau[x].append(0)

    for x in range(0,taille_x):
        for y in range(0,taille_y):
            nouveau_tableau[x][y] = C(x,y,tableau_milieu_aquatique)
    return nouveau_tableau

tableau_milieu_aquatique[4][4] = 100
tableau_milieu_aquatique[4][5] = 100
tableau_milieu_aquatique[5][4] = 100
tableau_milieu_aquatique[5][5] = 100


def tourner(n,tableau_milieu_aquatique):
    for i in range(n):
        tableau_milieu_aquatique = actualiser(tableau_milieu_aquatique)
    return tableau_milieu_aquatique
# tableau_milieu_aquatique[5][5] = C(5,5,tableau_milieu_aquatique)

afficher (tableau_milieu_aquatique)

tableau_milieu_aquatique = tourner(100,tableau_milieu_aquatique)
afficherGraphic(tableau_milieu_aquatique)



# tourner(100,tableau_milieu_aquatique)
# afficherGraphic(tableau_milieu_aquatique)