# Coefficient de diffusion
D = 0.25

# pas de coordonnée
delta_x=1
delta_y=1 #utile seuleuement en 2D

# pas de temps
delta_t=1

# taille de la grille
taille=31

# Si u est grand le schema n'est pas adapté
u_x=0 # possitif vers la droite
u_y=0 # possitif vers le bas #utile seuleuement en 2D

# true : mur Newman
# false : filtre Dirichlet
murGauche = False
murDroite = False
murHaut = False #utile seuleuement en 2D
murBas =False #utile seuleuement en 2D

# Permet d'afficher en % fonction du maximum du tableau
pourcentage = False

# Déffinit la polution dans sur un mur entier / utile seuleuement en 2D
Ghaut = 0
Ggauche = 0
Gbas = 0
Gdroite = 0

# afficher ou non les elements durant l'execution
afficherTableauCalcul = False
afficherConstant = False
afficherTableau = False
afficherVisuel = True
sauvegarderImage = True

verifierLesConditionCFL = False

# nombre de tour de boucle
n=10


# fonctions :
def initialisation_tableau():
    tableau = [[] for y in range(taille)]
    for x in range(0,taille):
        for y in range(0,taille):
            tableau[x].append(0)
    return tableau



tableau_milieu_aquatique = initialisation_tableau()
# polution initiale
tableau_milieu_aquatique[15][15] = 1


def initialisation_tableau_constant_1D():
    tableau_constant = initialisation_tableau()
    # tableau_constant[0][0] = (D)*((delta_t/delta_x**2)


    return tableau_constant

def initialisation_tableau_constant_2D():
    tableau_constant = initialisation_tableau()

    for x in range(0,taille):
        for y in range(0,taille):
            # Double au coin si les 2 mur sont polué
            if(x == 0 ) :
                # TODO pas finit ... pour y ??? pk cette formule
                tableau_constant[x][y] +=(D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Ghaut
            if(y==0):
                tableau_constant[x][y] += (D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Ggauche
            if(x == taille -1):
                tableau_constant[x][y] += (D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Gbas
            if(y==taille-1):
                tableau_constant[x][y] += (D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Gdroite
    return tableau_constant



