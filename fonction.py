import numpy as np
import matplotlib.pyplot as plt
from valeur import *
import os
import cv2

def afficherGraphicEtSauvegarder(tab):
        
    if(pourcentage) :
        tab = tab / np.max(tab) * 100
        tab = np.round(tab, 2)

    
    fig, ax = plt.subplots()
    im = ax.imshow(tab, cmap='viridis', interpolation='nearest')
    ax.set_xlabel('axe y')
    ax.set_ylabel('axe x')

    if(pourcentage) :
        cbar = plt.colorbar(im, ax=ax, format='%.2f%%')
        im.set_clim(0, 100)
    else :
        cbar = plt.colorbar(im, ax=ax, format='%.2e')

    if(pourcentage) :
        cbar.ax.set_ylabel('Concentration par rapport au maximum', rotation=-90, va="bottom")
    else :
        cbar.ax.set_ylabel('Concentration', rotation=-90, va="bottom")

    fig.tight_layout()

    if(sauvegarderImage):
        if(pourcentage):
            filename = f"images/pourcentage/D={D} ux={u_x} uy={u_y} taille={taille} deltaT={delta_t} deltaX={delta_x} deltaY={delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}.png"
        else:
            filename = f"images/valeur/D={D} ux={u_x} uy={u_y} taille={taille} deltaT={delta_t} deltaX={delta_x} deltaY={delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}.png"

        plt.savefig(filename)
    if(afficherVisuel):
        plt.show()
    plt.close()
    

def sauvegarder(tab,i,n):
        
    if(pourcentage) :
        tab = tab / np.max(tab) * 100
        tab = np.round(tab, 2)

    
    fig, ax = plt.subplots()
    im = ax.imshow(tab, cmap='viridis', interpolation='nearest')
    ax.set_xlabel('axe y')
    ax.set_ylabel('axe x')
    if(pourcentage) :
        cbar = plt.colorbar(im, ax=ax, format='%.2f%%')
        im.set_clim(0, 100)
    else :
        cbar = plt.colorbar(im, ax=ax, format='%.2e')

    if(pourcentage) :
        cbar.ax.set_ylabel('Concentration par rapport au maximum', rotation=-90, va="bottom")
    else :
        cbar.ax.set_ylabel('Concentration', rotation=-90, va="bottom")

    fig.tight_layout()

    if(sauvegarderImage):
        if(pourcentage):
            filename = f"video/pourcentage/D={D} ux={u_x} uy={u_y} taille={taille} deltaT={delta_t} deltaX={delta_x} deltaY={delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}/{i}.png"
        else:
            filename = f"video/valeur/D={D} ux={u_x} uy={u_y} taille={taille} deltaT={delta_t} deltaX={delta_x} deltaY={delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}/{i}.png"

        plt.savefig(filename)
    plt.close()



def creer_video(n,tableau):
    if sauvegarderImage:
        if pourcentage:
            chemin = f"video/pourcentage/D={D} ux={u_x} uy={u_y} taille={taille} deltaT={delta_t} deltaX={delta_x} deltaY={delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}/"
        else:
            chemin = f"video/valeur/D={D} ux={u_x} uy={u_y} taille={taille} deltaT={delta_t} deltaX={delta_x} deltaY={delta_y} mur.g={murGauche}.d={murDroite}.h={murHaut}.b={murBas} n={n}/"
        
        images = [f"{chemin}{int(i*ecart)}.png" for i in range(int(n/ecart))]
        frame = cv2.imread(images[0])
        height, width = frame.shape[:2]

        final = calcul_total(tableau)
        initial = calcul_total(tableau_milieu_aquatique)
        video_name = f"{chemin}initial = {initial} final = {final}.mp4"
        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), n/ecart/10, (width, height))

        for image in images:
            video.write(cv2.imread(image))

        cv2.destroyAllWindows()
        video.release()
        

def afficher (tableau_milieu_aquatique):
    if(afficherTableau):
        print("\n")
        for x in range(0,taille):
            print(tableau_milieu_aquatique[x])
        print("\n")

def verification_CFL_1D():
    if(verifierLesConditionCFL):
        if((2*D)*((delta_t/delta_x**2))>1):
            print("\033[91mpropagation trop elever en x ou en y\033[0m")
            exit()
        if(abs(u_x) > (2*D)*(delta_t/delta_x)):
            print("\033[91mcourant trop elever en x\033[0m")
            exit()


def verification_CFL_2D():
    if(verifierLesConditionCFL):
        if((2*D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))>1):
            print("\033[91mpropagation trop elever en x ou en y\033[0m")
            exit()
        if(abs(u_x) > (2*D)*(delta_t/delta_x)):
            print("\033[91mcourant trop elever en x\033[0m")
            exit()
        if(abs(u_y) > (2*D)*(delta_t/delta_y)):
            print("\033[91mcourant trop elever en y\033[0m")
            exit()

def verification_CFL_2D_ubis():
    if(verifierLesConditionCFL):
        if((2*D)*((delta_t/delta_x**2)+(delta_t/delta_y**2))+(delta_t*u_x/(2*delta_x)+delta_t*u_y/(2*delta_y))>1):
            print("\033[91mCondition CFL non respecter\033[0m")
            exit()

def calcul_total(tab):
    if isinstance(tab, np.ndarray):
        total = np.sum(tab)
    else:
        total = sum(sum(row) for row in tab)
    afficher(tab)
    print("total : " + str(total))
    return total

