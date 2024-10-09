from affichage import *

D= 0.2

delta_x=1
delta_y=1

delta_t=1


taille_x=5
taille_y=5


u=0

# true : mur Newman
# false : filtre Dirichlet
murGauche = True
murDroite = True
murHaut = True
murBas =True


n=2

if not ((2*D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))<=1):
    print("\033[91mpropagation trop elever en x ou en y\033[0m")
    exit()

tableau_milieu_aquatique_initial = [[] for y in range(taille_x)]
for x in range(0,taille_x):
    for y in range(0,taille_y):
        tableau_milieu_aquatique_initial[x].append(0)



tableau_milieu_aquatique = tableau_milieu_aquatique_initial

def actualiser(tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant_x,tableau_constant_y):
    nouveau_tableau1 = np.dot(tableau_calcul_x,tableau_milieu_aquatique)
    nouveau_tableau2 = np.dot(tableau_milieu_aquatique ,tableau_calcul_y)

    nouveau_tableau = np.add(nouveau_tableau1,nouveau_tableau2)
    
    # nouveau_tableau = np.add(nouveau_tableau,nouveau_tableau2)
    
    tableau_constant1 = np.dot(tableau_milieu_aquatique ,tableau_constant_x)
    tableau_constant2 = np.dot(tableau_constant_y ,tableau_milieu_aquatique)

    tableau_constant = np.add(tableau_constant1,tableau_constant2)


    nouveau_tableau = np.add(nouveau_tableau,tableau_constant)


    return nouveau_tableau

def tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant_x,tableau_constant_y):
    for i in range(n):
        tableau_milieu_aquatique = actualiser(tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant_x,tableau_constant_y)
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

for x in range(0,taille_y):
    for y in range(0,taille_y):
        if(y-x == -1):
            tableau_calcul_y[x].append((D*delta_t/delta_y**2))
        elif(y-x == 0):
            tableau_calcul_y[x].append((1/2-2*D*delta_t/delta_y**2))
        elif(y-x == 1):
            tableau_calcul_y[x].append((D*delta_t/delta_y**2))
        else :
            tableau_calcul_y[x].append(0)

afficherConsole(tableau_milieu_aquatique,taille_x)

tableau_constant_x = [[] for y in range(taille_x)]
for x in range(0,taille_x):
    for y in range(0,taille_y):
        if(x== taille_x-1 and y == taille_y-1):
            if(y-x == -1):
                tableau_constant_x[x].append((D*delta_t/delta_x**2)*2)
            elif(y-x == 0):
                tableau_constant_x[x].append((1/2-2*D*delta_t/delta_x**2)*2)
            elif(y-x == 1):
                tableau_constant_x[x].append((D*delta_t/delta_x**2)*2)
            else :
                tableau_constant_x[x].append(0)
        else :
            tableau_constant_x[x].append(0)

print("constant x : ")
afficherConsole(tableau_constant_x,taille_x)

tableau_constant_y = [[] for y in range(taille_x)]
for x in range(0,taille_x):
    for y in range(0,taille_y):
        if(x== taille_x-1 and y == taille_y-1):
            if(y-x == -1):
                tableau_constant_y[x].append((D*delta_t/delta_y**2)*2)
            elif(y-x == 0):
                tableau_constant_y[x].append((1/2-2*D*delta_t/delta_y**2)*2)
            elif(y-x == 1):
                tableau_constant_y[x].append((D*delta_t/delta_y**2)*2)
            else :
                tableau_constant_y[x].append(0)
        else :
            tableau_constant_y[x].append(0)


tableau_milieu_aquatique[4][4] = 1

tableau_milieu_aquatique=np.matrix(tableau_milieu_aquatique)

tableau_milieu_aquatique = tableau_milieu_aquatique.transpose()

tableau_calcul_x=np.matrix(tableau_calcul_x)
tableau_calcul_y=np.matrix(tableau_calcul_y)

tableau_constant_x=np.matrix(tableau_constant_x)
tableau_constant_y=np.matrix(tableau_constant_y)




# tableau_constant = [[] for y in range(taille_x)]

# for x in range(0,taille_x):
#     for y in range(0,taille_y):
#         tableau_constant[x].append(0)

# for x in range(0,taille_x):
#     for y in range(0,taille_y):
#         if(x==0 or x==taille_x-1):
#             tableau_constant[x][y]=1
#         if(y==0 or y==taille_y-1):
#             tableau_constant[x][y]=1

# afficher(tableau_constant)


# tableau_constant=np.matrix(tableau_constant)

# tableau_constant = tableau_constant.transpose()


# MODIFIER TABLEAU CONSTANT POUR AVOIR DES MURS ET PAS DES FILTRES

afficherConsole(tableau_calcul_x,taille_x)
afficherMatplotlib(tableau_milieu_aquatique,taille_x,taille_y)



tableau_milieu_aquatique = tourner(n,tableau_milieu_aquatique,tableau_calcul_x,tableau_calcul_y,tableau_constant_x,tableau_constant_y)


afficherConsole(tableau_milieu_aquatique,taille_x)

afficherMatplotlib(tableau_milieu_aquatique,taille_x,taille_y)

def calcul(tab):
    total = 0
    afficherConsole(tab,taille_x)
    for x in range(0,taille_x):
        for y in range(0,taille_y):
            total += tab[x,y]
    print("total : "+str(total))
    
calcul(tableau_milieu_aquatique)