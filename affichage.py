import numpy as np
import matplotlib.colors as cols
import matplotlib.pyplot as plt

def afficherMatplotlib(tab:list or np.matrix,len_x:int,len_y:int):
    """Permet d'afficher un tableau de valeur de taille len_x
    Préconditions :
     - Un tableau sous forme de list ou de numpy.matrix
    """
    fig,ax = plt.subplots()
    im = ax.imshow(tab)

    ax.set_xticks(np.arange(0,len_x))
    ax.set_yticks(np.arange(0,len_y))

    colors = ["#000c57","#0051ff","#00f7ff","#00ffa2","#00ff08","#9dff00","#ffff00","#ffdd00","#ffa600","#ff5100","#ff0000"]
    custom_cmap = cols.LinearSegmentedColormap.from_list("custom_cmap",colors)

    plt.imshow(tab,cmap=custom_cmap)
    cbar = plt.colorbar()

    plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")

    ax.set_title("Propagation d'un polluant")
    fig.tight_layout()
    plt.show()

def afficherConsole(tab:list or np.matrix, len_x:int):
    """Permet d'afficher dans la console le tableau de valeur en entrée
    Préconditions :
     - Un tableau sous forme de list ou de numpy.matrix
    """
    print()
    for x in range(0,len_x):
        print(tab[x])
    print()