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
LARGEUR = 600
HAUTEUR = 400
COULEURS = ["blue", "green", "yellow"]
TAILLE_CARRE = 20

# Définition des variables globales
Cells = []

### Cells est la liste qui contient les coordonées et la couleur de chaque cellules sous la forme [x, y, "color"]


# Définition des fonctions
def nouvelle_etape():
    # Fonction permettant de passer a une nouvelle etape
    global Cells
    Cells_step = Cells
    for n in range(len(Cells)):#les carres de bords ne peuvent pas prendre feu
        if n > (HAUTEUR / TAILLE_CARRE) and n < (HAUTEUR * LARGEUR - HAUTEUR / TAILLE_CARRE) and n % (HAUTEUR / TAILLE_CARRE) != 0 and (n + 1) % (HAUTEUR / TAILLE_CARRE) != 0: 
            if Cells[n][2] == "green":
                b = 0
                for m in range(n - 1 - int(HAUTEUR / TAILLE_CARRE), n + 2 - int(HAUTEUR / TAILLE_CARRE)):
                    if Cells[m][2] == "red":
                        b += 0.1
                for m in range(n - 1 + int(HAUTEUR / TAILLE_CARRE), n + 2 + int(HAUTEUR / TAILLE_CARRE)):
                    if m < len(Cells):
                        if Cells[m][2] == "red":
                            b += 0.1
                if Cells[n - 1][2] == "red":
                    b += 0.1
                if Cells[n + 1][2] == "red":#on regarde la couleur de chaque parcelle au tour de Cells[n]
                    b += 0.1
                a = rd.random()
                if a < b:
                    #une parcelle de forêt prend feu avec la probabilité 0.1 × nf 
                    Cells_step[n][2] = "red"
                terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+TAILLE_CARRE, Cells[n][1]+TAILLE_CARRE, fill = Cells_step[n][2])
            elif Cells[n][2] == "yellow":
                for m in range(n - 1 - int(HAUTEUR / TAILLE_CARRE), n + 2 - int(HAUTEUR / TAILLE_CARRE)):
                    if Cells[m][2] == "red":
                        Cells_step[n][2] = "red"
                for m in range(n - 1 + int(HAUTEUR / TAILLE_CARRE), n + 2 + int(HAUTEUR / TAILLE_CARRE)):
                    if m < len(Cells):
                        if Cells[m][2] == "red":
                            Cells_step[n][2] = "red"
                if Cells[n - 1][2] == "red":
                    Cells_step[n][2] = "red"
                if Cells[n + 1][2] == "red":
                    Cells_step[n][2] = "red"
                terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+TAILLE_CARRE, Cells[n][1]+TAILLE_CARRE, fill=Cells_step[n][2])
    Cells = Cells_step


def clic_feu(event):
    """Fonction permettant de créer une cellule de feu à l'endroit ou la souris se situe avec un clic gauche"""

    x = event.x
    y = event.y

    for n in range(len(Cells)):
        if (Cells[n][0] + TAILLE_CARRE - 1 >= x >= Cells[n][0] and
        Cells[n][1] + TAILLE_CARRE - 1 >= y >= Cells[n][1] and
        Cells[n][2] != "blue"):
            terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+TAILLE_CARRE, Cells[n][1]+TAILLE_CARRE, fill="red")
            Cells[n][2] = "red"


def gen_terrain():
    """Fonction permettant de générer le terrain. La liste Cells contient les coordonnées de chaques cellules ainsi que leurs couleurs respective"""

    global Cells
    Cells = []
    terrain.delete("all")

    for i in range(1, LARGEUR, TAILLE_CARRE):
        for j in range(1, HAUTEUR, TAILLE_CARRE):
            Cells.append([i, j, rd.choice(COULEURS)])
    
    for n in range(len(Cells)):

        if Cells[n][2] == "blue":
             terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+TAILLE_CARRE, Cells[n][1]+TAILLE_CARRE, fill="blue")
        elif Cells[n][2] == "green":
             terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+TAILLE_CARRE, Cells[n][1]+TAILLE_CARRE, fill="green")
        elif Cells[n][2] == "yellow":
             terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+TAILLE_CARRE, Cells[n][1]+TAILLE_CARRE, fill="yellow")


# Programme principal contenant la définition des widgets et des 
# événements qui leur sont liés et l’appel à la boule de gestion des événements

racine = tk.Tk()
racine.title("Propagation d'un incendie")
terrain = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="black")
Bouton_terrain = tk.Button(racine, text="Generate Terrain", command=gen_terrain)
Bouton_save = tk.Button(racine, text="Save")
Bouton_load = tk.Button(racine, text="Load")
Bouton_step = tk.Button(racine, text="Step", command=nouvelle_etape)
Bouton_start = tk.Button(racine, text="Start")
Bouton_stop = tk.Button(racine, text="Stop")
Bouton_speedup = tk.Button(racine, text="Speedup")
Bouton_speeddown = tk.Button(racine, text="Slowdown")

terrain.bind('<Button-1>', clic_feu)


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