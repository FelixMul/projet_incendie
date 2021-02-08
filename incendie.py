#########################################
# groupe DLMP
# Felix Muller  
# James Burat
# Lucas FEDERSPIEL
# Bixente Bengochea
# https://github.com/FelixMul/projet_incendie
#########################################

#import des librairies
import tkinter as tk
import random as rd


# Définition des constantes 
DUREE_FEU = 0
DUREE_CENDRE = 0
LARGEUER = 600
HAUTEUR = 400
COULEURS = ["blue", "red", "green", "yellow", "black", "gray50"]

# Définition des variables globales


# Définition des fonctions
def nouvelle_etape():
    pass


# Programme principal contenant la définition des widgets et des 
# événements qui leur sont liés et l’appel à la boule de gestion des événements
racine = tk.Tk()
racine.title("Propagation d'un incendie")
terrain = tk.Canvas(racine, width=600, height=400, bg="black")
Bouton_terrain = tk.Button(racine, text="Terrain")
Bouton_save = tk.Button(racine, text="Save")
Bouton_load = tk.Button(racine, text="Load")
Bouton_step = tk.Button(racine, text="Step")
Bouton_start = tk.Button(racine, text="Start")
Bouton_stop = tk.Button(racine, text="Stop")
Bouton_speedup = tk.Button(racine, text="Speedup")
Bouton_speeddown = tk.Button(racine, text="Slowdown")

Bouton_terrain.grid(row=0, column=0)
Bouton_save.grid(row=0, column=1)
Bouton_load.grid(row=0, column=2)
Bouton_step.grid(row=0, column=3)
Bouton_start.grid(row=0, column=4)
Bouton_stop.grid(row=1, column=4)
Bouton_speedup.grid(row=2, column=4)
Bouton_speeddown.grid(row=3, column=4)
terrain.grid(row=1, column=0, columnspan=4, rowspan=3)

racine.mainloop()