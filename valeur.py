# Coefficient de diffusion
D = 0.2

# pas de coordonnée
delta_x=1
delta_y=1 #utile seuleuement en 2D

# pas de temps
delta_t=1

# taille de la grille
taille=101

# Si u est grand le schema n'est pas adapté sauf avec l'utilisation de ubis
u_x=0 # possitif vers la droite
u_y=0 # possitif vers le bas #utile seuleuement en 2D

# true : mur Newman
# false : filtre Dirichlet
murHaut = False
murBas =False
murGauche = False #utile seuleuement en 2D
murDroite = False #utile seuleuement en 2D

# nombre de tour de boucle
n=1000

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

# demander la verification des conditions CFL ou non
verifierLesConditionCFL = True


# Parametre pour cree une video
ubis = False # choix entre une approximation de u d'ordre 1 (True) ou 2 (False)

ecart = n/100 # ecart entre la sauvegarde d'une image
# Pour une jolie video avec peu de temps de création il est conseiller de mettre un ecart de n/100

# fonctions :
def initialisation_tableau():
    tableau = [[] for y in range(taille)]
    for x in range(0,taille):
        for y in range(0,taille):
            tableau[x].append(0)
    return tableau

tableau_milieu_aquatique = initialisation_tableau()

# polution initiale

tableau_milieu_aquatique[50][50] = 1

def initialisation_tableau_constant_1D():
    tableau_constant = initialisation_tableau()
    # polution constante
    # tableau_constant[0][0] = (D)*((delta_t/delta_x**2)


    return tableau_constant

def initialisation_tableau_constant_2D():
    tableau_constant = initialisation_tableau()

    for x in range(0,taille):
        for y in range(0,taille):
            # Double au coin si les 2 mur sont polué
            if(x == 0 ) :
                tableau_constant[x][y] +=(D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Ghaut
            if(y==0):
                tableau_constant[x][y] += (D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Ggauche
            if(x == taille -1):
                tableau_constant[x][y] += (D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Gbas
            if(y==taille-1):
                tableau_constant[x][y] += (D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))*Gdroite
    return tableau_constant



