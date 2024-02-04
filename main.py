
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from list_filleul import filleul
from list_parrain import parrain
import random 
import time
import os
#transformer les dictionnaires en tableau
parrainT = [j for j in parrain.values()]
filleulT= [i for i in filleul.values()]
#melange des tableaux aleatoirement
random.shuffle(parrainT)
random.shuffle(filleulT)
j=0
while len(filleulT)>len(parrainT):
    parrainT.append(parrainT[j])
    j+=1
# Affichez la liste de listes
random.shuffle(parrainT)
print(len(filleulT)," de filleuls pour ",len(parrainT)," de parrains")
for k in range(len(filleulT)):
    print(filleulT[k]["nom_filleul"]+"est binomé avec"+parrainT[k]["nom_parrain"])
"""
DEBUT DU PROGRAMME
"""

#transformation  des dictionnaires (filleul et parrain) en tableau (parrainT et filleulT)

# Fonction pour choisir un binôme

# Créer une fenêtre principale
fenetre = tk.Tk()
fenetre.title("BINOMAGE 21 ET 22 EME PROMOTIONS STCGP")
fenetre.geometry("1920x1080")
# Charger l'image de fond
image_de_fond = Image.open("img/maquetfinal.jpg")
image_de_fond = ImageTk.PhotoImage(image_de_fond)

label_image = tk.Label(fenetre, image=image_de_fond)
label_image.place(relwidth=1, relheight=1)  # Remplir tout l'écran avec l'image

label = tk.Label(fenetre, text="BINOMAGE")
label.pack()
#fonctionnement
i,idf,idp,idpp,idpf=0,None,None,None,None
valf,valp=True,False
def choix_binome(numero_bouton):
    # Code pour choisir un binôme ici
    global i, idf, idp, idpp, idpf, valf, valp

    if i < len(filleulT) and valp:
        animation_images = []
        for n in range(15):
            image = Image.open(parrainT[(random.randint(0, 100)) % len(parrainT)]["photo_parrain"])
            image = image.resize((310, 310))
            animation_images.append(ImageTk.PhotoImage(image=image))
        random.shuffle(animation_images)
        for k in range(15):
            an = canvas_photo_droit.create_image(155, 155, image=animation_images[k])  # Centrer l'animation
            fenetre.update()
            time.sleep(0.15)
            canvas_photo_droit.delete(an)

        imagep = Image.open(parrainT[i]["photo_parrain"])
        php = imagep.resize((310, 310))
        photop = ImageTk.PhotoImage(php)
        idpp = canvas_photo_droit.create_image(0, 0, anchor=tk.NW, image=photop)
        canvas_photo_droit.image = photop

        texte = parrainT[i]["nom_parrain"]  # La chaîne de caractères à ajouter
        idp = canvas_nom_droit.create_text(220, 30, text=texte, font=("Algerian", 20), fill="black")
        i += 1
        valp = False
        valf = True

        # Change la couleur du bouton sur lequel on a cliqué
        Bouton[numero_bouton - 1].configure(bg="grey")
    else:
        pass

def debuter_choix():
    # Code pour commencer le choix des binômes ic
    global i,idf, idp, idpf, idpp,valf,valp
    if i < len(filleulT) :
        imagef = (Image.open(filleulT[i]["photo_filleul"]))
        phf=imagef.resize((310, 310))
        photo = ImageTk.PhotoImage(phf)
        idpf=canvas_photo_gauche.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas_photo_gauche.image=photo
        texte = filleulT[i]["nom_filleul"]  # La chaîne de caractères à ajouter
        idf=canvas_nom_gauche.create_text(220, 30, text=texte, font=("Algerian", 20), fill="black")
        if i==30:
            for btn in Bouton:
                btn["bg"]="white"
    
    else:
        pass
def supprimer_binome():
    global idf, idp, idpf, idpp
    canvas_nom_gauche.delete(idf)
    canvas_nom_droit.delete(idp)
    canvas_photo_gauche.delete(idpf)
    canvas_photo_droit.delete(idpp)

def prochain_binome():
    global i,idf, idp, idpf, idpp,valf,valp
    if i==0 and valf:
        debuter_choix()
        valf=False
        valp=True
    else:
        if i < len(filleulT) and valf:
            supprimer_binome()
            debuter_choix()
            valf=False
            valp=True
        else:
            pass

    # Code pour afficher le prochain binôme ici
    
# Canvas pour la photo du binôme gauche
canvas_photo_gauche = tk.Canvas(fenetre, width=300, height=300, bg="orange", bd=10, relief="sunken", highlightthickness=0)
canvas_photo_gauche.place(x=245, y=30)

# Canvas pour le nom du binôme gauche

canvas_nom_gauche = tk.Canvas(fenetre, width=400, height=50, bg="white", bd=10, relief="groove", highlightthickness=0)
canvas_nom_gauche.place(x=195, y=370)

# Canvas pour la photo du binôme droit

    
canvas_photo_droit = tk.Canvas(fenetre, width=300, height=300, bg="orange", bd=10, relief="sunken", highlightthickness=2)
canvas_photo_droit.place(x=955, y=30)

# Canvas pour le nom du binôme droit
canvas_nom_droit = tk.Canvas(fenetre, width=400, height=50, bg="white", bd=10, relief="groove", highlightthickness=0)
canvas_nom_droit.place(x=905, y=370)

# Boutons en haut de la page

bouton_filleul = tk.Button(fenetre, text="SUIVANT", command=prochain_binome, width=13,height=3 ,font=("Algerian", 10), bg="blue", fg="white", bd=5, relief="raised",activebackground='green')
bouton_filleul.place(x=710, y=370)

canvas_boutons = tk.Canvas(fenetre, width=1300, height=220, bg="orange")
canvas_boutons.place(x=115,y=470)

# Nombre de lignes et de colonnes
nb_lignes = 3
nb_colonnes = 10

# Largeur et hauteur des boutons
largeur_bouton = ((1366 - 10 * (nb_colonnes + 1)) // (nb_colonnes))-20
hauteur_bouton = (300 - 10 * (nb_lignes + 1)) // (nb_lignes*2)
# tableau de boutons
Bouton=[0]*30
# Créez les boutons dans une boucle
for ligne in range(nb_lignes):
    for colonne in range(nb_colonnes):
        numero_bouton = ligne * nb_colonnes + colonne + 1
        text_bouton = str(numero_bouton)
        x = 10 + colonne * (largeur_bouton + 10)
        y = 10 + ligne * (hauteur_bouton + 10)
        Bouton[numero_bouton - 1] = tk.Button(canvas_boutons, text=text_bouton, command=lambda num=numero_bouton: choix_binome(num),font=("Algerian", 20), bd=5, highlightthickness=3,padx=0, pady=0, relief="raised", bg="white",activebackground="green", fg="black", width=13, height=3)
        canvas_boutons.create_window(x + 120, y + 50, window=Bouton[numero_bouton - 1],
                                     width=largeur_bouton, height=hauteur_bouton)

# Lancer la boucle principale de l'application
fenetre.mainloop()
