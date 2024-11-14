
import numpy as np
import matplotlib.pyplot as plt

# Coefficient de diffusion
D= 0.2

# pas de coordonnée
delta_x=1
delta_y=1

# pas de temps
delta_t=1

# taille de la grille
taille_x=100
taille_y=100

# Si u est grand le schema n'est pas adapté
u_x=0.4 # possitif vers la droite
u_y=0 # possitif vers le bas

# true : mur Newman
# false : filtre Dirichlet
murGauche = True
murDroite = True
murHaut = True
murBas =True

# Déffinit la polution dans sur un mur entier
Ghaut = 0
Ggauche = 0
Gbas = 0
Gdroite = 0

afficherTableauCalcul = False

afficherConstant = False

afficherTableau = False

# nombre de tour de boucle
n=100

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


tableau_milieu_aquatique_initial = [[] for y in range(taille_x)]
for x in range(0,taille_x):
    for y in range(0,taille_y):
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
    
    
    nouveau_tableau = np.add(nouveau_tableau,tableau_constant)


    return nouveau_tableau



def tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant):
    for i in range(n):
        tableau_milieu_aquatique = actualiser(tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant)
    return tableau_milieu_aquatique



tableau_calcul_x = [[] for y in range(taille_x)]

for x in range(0,taille_x):
    for y in range(0,taille_y):
        if(y-x == -1):
            tableau_calcul_x[x].append((D*delta_t/delta_x**2) + delta_t*u_x/(2*delta_x))
        elif(y-x == 0):
            if(murBas and (x== taille_x -1 and y == taille_y-1)) :
                tableau_calcul_x[x].append((1/2-1*D*delta_t/delta_x**2))
            elif(murHaut and (x== 0 and y == 0)) :
                tableau_calcul_x[x].append((1/2-1*D*delta_t/delta_x**2))
            else :
                tableau_calcul_x[x].append((1/2-2*D*delta_t/delta_x**2))
        elif(y-x == 1):
            tableau_calcul_x[x].append((D*delta_t/delta_x**2)-delta_t*u_x/(2*delta_x))
            
        else :
            tableau_calcul_x[x].append(0)
# enleve les echanges avec l'exterieur du au courant
tableau_calcul_x[0][0] += -delta_t*u_x/(2*delta_x)
tableau_calcul_x[taille_x-1][taille_y-1] += delta_t*u_x/(2*delta_x)




tableau_calcul_y = [[] for y in range(taille_x)]

for x in range(0,taille_x):
    for y in range(0,taille_y):
        if(y-x == -1):
            tableau_calcul_y[x].append((D*delta_t/delta_y**2) - delta_t*u_y/(2*delta_y))
        elif(y-x == 0):
            if(murDroite and (x== taille_x -1 and y == taille_y-1)) :
                tableau_calcul_y[x].append((1/2-1*D*delta_t/delta_y**2))
            elif(murGauche and (x== 0 and y == 0)) :
                tableau_calcul_y[x].append((1/2-1*D*delta_t/delta_y**2))
            else :
                tableau_calcul_y[x].append((1/2-2*D*delta_t/delta_y**2))
        elif(y-x == 1):
            tableau_calcul_y[x].append((D*delta_t/delta_y**2) + delta_t*u_y/(2*delta_y))
        else :
            tableau_calcul_y[x].append(0)
# enleve les echanges avec l'exterieur du au courant
tableau_calcul_y[0][0] += -delta_t*u_y/(2*delta_y)
tableau_calcul_y[taille_x-1][taille_y-1] += delta_t*u_y/(2*delta_y)

# Initialiation de la polution
tableau_milieu_aquatique[4][4] = 1


tableau_milieu_aquatique=np.matrix(tableau_milieu_aquatique)

tableau_milieu_aquatique = tableau_milieu_aquatique.transpose()

tableau_calcul_x=np.matrix(tableau_calcul_x)
tableau_calcul_y=np.matrix(tableau_calcul_y)


tableau_constant = [[] for y in range(taille_x)]

for x in range(0,taille_x):
    for y in range(0,taille_y):
        # Double au coin si les 2 mur sont polué
        tableau_constant[x].append(0)
        if(x == 0 ) :
            tableau_constant[x][y] += (D*delta_t/delta_x**2*Ggauche)
        if(y==0):
            tableau_constant[x][y] += (D*delta_t/delta_x**2*Ghaut)
        if(x == taille_x -1):
            tableau_constant[x][y] += (D*delta_t/delta_x**2*Gdroite)
        if(y==taille_y-1):
            tableau_constant[x][y] += (D*delta_t/delta_x**2*Gbas)
if(afficherConstant):
    afficher(tableau_constant)


tableau_constant=np.matrix(tableau_constant)

tableau_constant = tableau_constant.transpose()

if(afficherTableauCalcul):
    afficher(tableau_calcul_x)
    afficher(tableau_calcul_y)


if afficherTableau:
    afficher(tableau_milieu_aquatique)



tableau_milieu_aquatique = tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant)

if afficherTableau:
    afficher(tableau_milieu_aquatique)

afficherGraphic(tableau_milieu_aquatique)

def calcul(tab):
    total = 0
    # afficher(tab)
    for x in range(0,taille_x):
        for y in range(0,taille_y):
            total += tab[x,y]
    print("total : "+str(total))
    
calcul(tableau_milieu_aquatique)

    