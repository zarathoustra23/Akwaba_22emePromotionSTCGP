import tkinter as tk
from PIL import Image, ImageTk

# Votre dictionnaire de parrains (5 parrains)
parrain = {
    1: {"nom_parrain": "ACHY JOSUE MARSHALL", "photo_parrain": "parrain/image1.jpg", "matricule_parrain": 101},
    2: {"nom_parrain": "BANTANGO ABOUBAKARS", "photo_parrain": "parrain/image2.jpeg", "matricule_parrain": 102},
    3: {"nom_parrain": "BITTY OKOMA HAROLD", "photo_parrain": "parrain/albert.jpg", "matricule_parrain": 103},
    4: {"nom_parrain": "DIARRASSOUBA NEILA", "photo_parrain": "parrain/image4.jpeg", "matricule_parrain": 104},
    5: {"nom_parrain": "DOH KOUAME CHRIS", "photo_parrain": "parrain/image5.jpg", "matricule_parrain": 105},
    6: {"nom_parrain": "DOUMBIA MARIAM", "photo_parrain": "parrain/image6.jpg", "matricule_parrain": 106},
    7: {"nom_parrain": "ETIEN KOUASSI LOIC", "photo_parrain": "parrain/image7.jpg", "matricule_parrain": 107},
    8: {"nom_parrain": "KAMATE ADJA MAGBE", "photo_parrain": "parrain/image8.jpg", "matricule_parrain": 108},
    9: {"nom_parrain": "KANTE SOUMAHORO", "photo_parrain": "parrain/image9.jpeg", "matricule_parrain": 109},
    10: {"nom_parrain": "KISSI DJOUKA JEAN", "photo_parrain": "parrain/albert.jpg", "matricule_parrain": 110},
    11: {"nom_parrain": "KOBA BINDJE DONALD", "photo_parrain": "parrain/image11.jpg", "matricule_parrain": 111},
    12: {"nom_parrain": "KOFFI YAO DEBORAH", "photo_parrain": "parrain/image12.jpg", "matricule_parrain": 112},
    13: {"nom_parrain": "KOFFI BLANCHE-OCEANE", "photo_parrain": "parrain/image13.jpg", "matricule_parrain": 113},
    14: {"nom_parrain": "KOFFI BROU EDDY", "photo_parrain": "parrain/image14.jpeg", "matricule_parrain": 114},
    15: {"nom_parrain": "KOFFI KOUASSI STEVE", "photo_parrain": "parrain/image15.jpg", "matricule_parrain": 115},
    16: {"nom_parrain": "KONE LYA-YANN", "photo_parrain": "parrain/image16.jpg", "matricule_parrain": 116},
    17: {"nom_parrain": "KOUA ASSOUMOU BORIS", "photo_parrain": "parrain/image17.jpg", "matricule_parrain": 117},
    18: {"nom_parrain": "KOUADIO PAUL NOEL", "photo_parrain": "parrain/image18.jpg", "matricule_parrain": 118},
    19: {"nom_parrain": "KOUAKOU KOUAME ROMARIC", "photo_parrain": "parrain/image19.jpeg", "matricule_parrain": 119},
    20: {"nom_parrain": "KOUASSI AURELIEN", "photo_parrain": "parrain/image20.jpg", "matricule_parrain": 120},
    21: {"nom_parrain": "LOGROAN YOHOU EUNICE", "photo_parrain": "parrain/image21.jpeg", "matricule_parrain": 121},
    22: {"nom_parrain": "N'GUESSAN KOUASSI ALAIN", "photo_parrain": "parrain/image22.jpg", "matricule_parrain": 122},
    23: {"nom_parrain": "N'ZI DE YOBOUE PAUL", "photo_parrain": "parrain/image23.jpg", "matricule_parrain": 123},
    24: {"nom_parrain": "OUATTARA PEPEYOGO", "photo_parrain": "parrain/image24.jpeg", "matricule_parrain": 124},
    25: {"nom_parrain": "PALE SEBY FRANCK", "photo_parrain": "parrain/image25.jpg", "matricule_parrain": 125},
    26: {"nom_parrain": "PLEHIA CHARBELLE", "photo_parrain": "parrain/image26.jpeg", "matricule_parrain": 126},
    27: {"nom_parrain": "SOKOURI ANICET VALERE", "photo_parrain": "parrain/image27.jpg", "matricule_parrain": 127},
    28: {"nom_parrain": "SORO SERGE ELIE", "photo_parrain": "parrain/image28.jpg", "matricule_parrain": 128},
    29: {"nom_parrain": "SOUMAHORO OUSMANE", "photo_parrain": "parrain/image29.jpeg", "matricule_parrain": 129},
    30: {"nom_parrain": "SYLLA SIAKA ", "photo_parrain": "parrain/image30.jpg", "matricule_parrain": 130},
    31: {"nom_parrain": "TIESSE TRA JAIRUS", "photo_parrain": "parrain/image31.jpeg", "matricule_parrain": 131},
    32: {"nom_parrain": "YAMOSSOUN AHOUSSI", "photo_parrain": "parrain/image32.jpg", "matricule_parrain": 132},
    33: {"nom_parrain": "YAO KOUAME ELYSEE", "photo_parrain": "parrain/image33.jpeg", "matricule_parrain": 133},
    34: {"nom_parrain": "YUMBA MARIE CASSANDRE", "photo_parrain": "parrain/image34.jpg", "matricule_parrain": 134}
}

# Créer une fenêtre principale
fenetre = tk.Tk()
fenetre.title("Liste des parrains")

# Créer un canvas pour afficher les informations des parrains
canvas = tk.Canvas(fenetre, width=1366, height=768)
canvas.pack()

# Liste pour stocker les images
images = []

# Nombre de lignes et de colonnes dans la grille
nombre_lignes = 6
nombre_colonnes = 10

# Largeur et hauteur de chaque cellule
largeur_cellule = 1366 // nombre_colonnes
hauteur_cellule = 768 // nombre_lignes

# Afficher les informations de chaque parrain dans la grille
for i, (parrain_id, info) in enumerate(parrain.items()):
    ligne = i // nombre_colonnes
    colonne = i % nombre_colonnes

    # Coordonnées de la cellule dans la grille
    x1 = colonne * largeur_cellule
    y1 = ligne * hauteur_cellule
    x2 = x1 + largeur_cellule
    y2 = y1 + hauteur_cellule

    image = Image.open(info["photo_parrain"])
    image.thumbnail((largeur_cellule - 20, hauteur_cellule - 20))  # Redimensionner l'image pour s'adapter à la cellule
    photo = ImageTk.PhotoImage(image)
    images.append(photo)  # Ajouter l'image à la liste

    # Afficher l'image
    canvas.create_image(x1 + 10, y1 + 10, anchor=tk.NW, image=photo)
    
    # Afficher le nom
    canvas.create_text(x1 + 10, y1 + hauteur_cellule - 10, text="Nom: " + info["nom_parrain"], anchor=tk.W)

    # Afficher le matricule
    canvas.create_text(x1 + 10, y1 + hauteur_cellule - 30, text="Matricule: " + str(info["matricule_parrain"]), anchor=tk.W)

# Lancer la boucle principale de l'application
fenetre.mainloop()
