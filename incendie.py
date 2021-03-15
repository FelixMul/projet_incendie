#########################################
# groupe DLMP
# Felix Muller  
# James Burat
# Lucas FEDERSPIEL
# Bixente Bengochea
# https://github.com/FelixMul/projet_incendie
#########################################

# import des librairies #
import tkinter as tk
import random as rd
import copy as cp


# Définition des constantes #
DUREE_FEU = 10
DUREE_CENDRE = 10
LARGEUR = 600
HAUTEUR = 400
COULEURS = ["blue", "green", "yellow"]
COTE = 20 # Taille du côté, doit être un diviseur commun de la largeur et de la hauteur

# Définition des variables globales #
Cells = []
nb_feux = None          # Nombre de case en feux
delai = 1000            # Délai d'attente entre 2 étapes du programme (en ms)
nb_etapes = 0           # Nombre d'étapes


### Cells est la liste qui contient les coordonées et la couleur de chaque cellules sous la forme [x, y, "color"]
### Cells_step est la liste qu'on utilise pour passer a la prochaine etape

# Définition des fonctions
def nouvelle_etape(event = None):
    """Fonction permettant de passer a une nouvelle etape"""
    global Cells
    Cells_step = cp.deepcopy(Cells)
    for n in range(len(Cells)):  # Les carrés de bords ne peuvent pas prendre feu
        if n > (HAUTEUR / COTE) and n < ((HAUTEUR // COTE) * (LARGEUR // COTE) - HAUTEUR // COTE) and n % (HAUTEUR / COTE) != 0 and (n + 1) % (HAUTEUR / COTE) != 0: 
            if Cells[n][2] == "green":
                b = 0
                for m in range(n - 1 - int(HAUTEUR / COTE), n + 2 - int(HAUTEUR / COTE)):
                    if Cells[m][2] == "red":
                        b += 0.1
                for m in range(n - 1 + int(HAUTEUR / COTE), n + 2 + int(HAUTEUR / COTE)):
                    if m < len(Cells):
                        if Cells[m][2] == "red":
                            b += 0.1
                if Cells[n - 1][2] == "red":
                    b += 0.1
                if Cells[n + 1][2] == "red":  # On regarde la couleur de chaque parcelle au tour de Cells[n]
                    b += 0.1
                a = rd.random()
                if a < b:
                    # Une parcelle de forêt prend feu avec la probabilité 0.1 × nf 
                    Cells_step[n][2] = "red"
                    Cells_step[n][3] = DUREE_FEU
                terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill = Cells_step[n][2])
            elif Cells[n][2] == "yellow":
                for m in range(n - 1 - int(HAUTEUR / COTE), n + 2 - int(HAUTEUR / COTE)):
                    if Cells[m][2] == "red":
                        Cells_step[n][2] = "red"
                        Cells_step[n][3] = DUREE_FEU
                for m in range(n - 1 + int(HAUTEUR / COTE), n + 2 + int(HAUTEUR / COTE)):
                    if m < len(Cells):
                        if Cells[m][2] == "red":
                            Cells_step[n][2] = "red"
                            Cells_step[n][3] = DUREE_FEU
                if Cells[n - 1][2] == "red":
                    Cells_step[n][2] = "red"
                    Cells_step[n][3] = DUREE_FEU
                if Cells[n + 1][2] == "red":
                    Cells_step[n][2] = "red"
                    Cells_step[n][3] = DUREE_FEU
                terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill=Cells_step[n][2])
    # Permet de regarder la valeur DUREE_FEU
    for n in Cells_step:
        if n[2] == "red":
            n[3] -= 1
            if n[3] == 0:
                n[2] = "gray"
                n[3] = DUREE_CENDRE
                terrain.create_rectangle(n[0], n[1], n[0]+COTE, n[1]+COTE, fill=n[2])
    # Permet de regarder la valeur DUREE_CENDRE
    for n in Cells_step:
        if n[2] == "gray":
            n[3] -= 1
            if n[3] == 0:
                n[2] = "black"
                terrain.create_rectangle(n[0], n[1], n[0]+COTE, n[1]+COTE, fill=n[2])
    Cells = cp.deepcopy(Cells_step)

def clic_feu(event):
    """Fonction permettant de créer une cellule de feu à l'endroit ou la souris se situe avec un clic gauche"""

    x = event.x
    y = event.y

    for n in range(len(Cells)):
        if (Cells[n][0] + COTE - 1 >= x >= Cells[n][0] and
        Cells[n][1] + COTE - 1 >= y >= Cells[n][1] and
        Cells[n][2] != "blue"):
            terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill="red")
            Cells[n][2] = "red"
            Cells[n][3] = DUREE_FEU


def gen_terrain():
    """Fonction permettant de générer le terrain. La liste Cells contient les coordonnées de chaques cellules ainsi que leurs couleurs respective, leur DUREE_FEU et DUREE_CENDRE"""

    global Cells
    Cells = []
    terrain.delete("all")

    for i in range(1, LARGEUR, COTE):
        for j in range(1, HAUTEUR, COTE):
            Cells.append([i, j, rd.choice(COULEURS), 0])
    for n in range(len(Cells)):

        if Cells[n][2] == "blue":
             terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill="blue")
        elif Cells[n][2] == "green":
             terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill="green")
        elif Cells[n][2] == "yellow":
             terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill="yellow")


def etape_enchaine():
    """Fonction qui permet d'enchainer toutes les étapes, jusqu'à ce qu'il ne reste plus une seule parcelle en feu. Le nombre d'étapes et le nombre de parcelle en feux s'affiche également."""
    global nb_etapes
    compte_case_feux()     
    if nb_feux == 0:
        nb_etapes = 0 
    else:
        nb_etapes += 1
        nouvelle_etape(event=None)
        print("Le programme exécute l'étape", nb_etapes, "du programme.")
        terrain.after(delai, etape_enchaine) 
        
          
def compte_case_feux(): 
    """Cette fonction permet de compter le nombre de case en feux par étape."""
    global nb_feux
    nb_feux = 0
    for n in range(len(Cells)):
        if Cells[n][2] == "red": 
            nb_feux += 1
    print("Il y a", nb_feux, "cases en feu.")

        
### Programme principal contenant la définition des widgets et des événements ###
### qui leur sont liés et l’appel à la boule de gestion des événements.       ###

racine = tk.Tk()
racine.title("Propagation d'un incendie")
terrain = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="black")
Bouton_terrain = tk.Button(racine, text="Generate Terrain", command=gen_terrain)
Bouton_save = tk.Button(racine, text="Save")
Bouton_load = tk.Button(racine, text="Load")
Bouton_step = tk.Button(racine, text="Step", command=nouvelle_etape)
Bouton_start = tk.Button(racine, text="Start", command=etape_enchaine)
Bouton_stop = tk.Button(racine, text="Stop")
Bouton_speedup = tk.Button(racine, text="Speedup")
Bouton_speeddown = tk.Button(racine, text="Slowdown")

terrain.bind('<Button-1>', clic_feu)
racine.bind('<space>', nouvelle_etape)


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
