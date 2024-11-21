# Explication des programmes

Nous avons réalisé 5 programmes qui permettent chacun de faire une simulation différente.  
Pour simplifier leur utilisation, nous avons ajouté un fichier *valeur.py* qui permet de définir toutes les valeurs initiales utilisées dans les 5 autres programmes.

Chacun des programmes inclut un visuel et un calcul de la concentration totale à la fin.  
Ils prennent en compte les conditions de Newman ou de Dirichlet et permettent également de placer une pollution constante à un emplacement précis.  
De plus, il est possible de sauvegarder les visuels si nécessaire.


## Les différents programmes

### Boucle simple 1D  
Le programme *boucle simple 1D.py* permet de simuler une diffusion et un courant en 1D.  


### Boucle simple 2D  
Le programme *boucle simple 2D.py* permet de simuler cette fois-ci en 2D.  


### Boucle avec matrice 1D  
Le programme *boucle avec matrice 1D.py* permet de simuler une diffusion et un courant en 1D à l'aide de matrices.  


### Boucle avec matrice 2D  
Le programme *boucle avec matrice 2D.py* permet de simuler cette fois-ci en 2D à l'aide de matrices.  


### Boucle avec matrice 2D avec u d'ordre 1  
Le programme *boucle avec matrice 2D ubis.py* permet de simuler un courant en 2D avec une approximation d'ordre 1 appelée *ubis*.  


### Création d'une vidéo  
Le programme *sauvegarde multiple.py* permet de simuler à l'aide de matrices et de sauvegarder les visuels tous les x tours. Ensuite, le programme crée une vidéo de 10 secondes compilant tous les visuels.


## Sauvegarde  
À chaque sauvegarde de visuel, le fichier est enregistré dans un dossier avec un nom permettant d’identifier les conditions initiales.  


# Dépendances  

- *Numpy* est nécessaire pour gérer les matrices.  
  ```bash
  pip install numpy
  ```
  
- *Matplotlib* est nécessaire pour afficher les visuels.  
  ```bash
  pip install matplotlib
  ```

- *OpenCV* est nécessaire pour créer des vidéos.  
  ```bash
  pip install opencv-python
  ```


# Compilation  
Pour utiliser les programmes, il vous suffit de choisir les conditions initiales et les paramètres dans *valeur.py*, puis d’exécuter le fichier correspondant à la simulation souhaitée (exemple : *boucle avec matrice 2D.py*).  