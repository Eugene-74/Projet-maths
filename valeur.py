# Coefficient de diffusion
D= 1

# pas de coordonnée
delta_x=1
delta_y=1 #utile seuleuement en 2D

# pas de temps
delta_t=1

# taille de la grille
taille_x=11
taille_y=11 #utile seuleuement en 2D

# Si u est grand le schema n'est pas adapté
u_x=0 # possitif vers la droite
u_y=0 # possitif vers le bas #utile seuleuement en 2D

# true : mur Newman
# false : filtre Dirichlet
murGauche = False
murDroite = False
murHaut = False #utile seuleuement en 2D
murBas =False #utile seuleuement en 2D

# Déffinit la polution dans sur un mur entier
Ghaut = 0
Ggauche = 0
Gbas = 0
Gdroite = 0

# afficher ou non les elements durant l'execution
afficherTableauCalcul = False
afficherConstant = False
afficherTableau = False
afficherVisuel = True

verifierLesConditionCFL = False

# nombre de tour de boucle
n=5

# fonctions :
def initialisation_tableau():
    tableau = [[] for y in range(taille_x)]
    for x in range(0,taille_x):
        for y in range(0,taille_x):
            tableau[x].append(0)
    return tableau



tableau_milieu_aquatique = initialisation_tableau()
# polution initiale
tableau_milieu_aquatique[5][5] = 1



def initialisation_tableau_constant():
    tableau_constant = initialisation_tableau()
    # polution permanente
    # tableau_constant[5][5] = 0

    for x in range(0,taille_x):
        for y in range(0,taille_y):
            # Double au coin si les 2 mur sont polué
            if(x == 0 ) :
                tableau_constant[x][y] += (D*delta_t/delta_x**2*Ggauche)
            if(y==0):
                tableau_constant[x][y] += (D*delta_t/delta_x**2*Ghaut)
            if(x == taille_x -1):
                tableau_constant[x][y] += (D*delta_t/delta_x**2*Gdroite)
            if(y==taille_y-1):
                tableau_constant[x][y] += (D*delta_t/delta_x**2*Gbas)
    return tableau_constant



