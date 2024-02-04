
import tkinter as tk
from PIL import Image, ImageTk

# Votre dictionnaire de filleuls (15 filleuls)
filleul = {
    1: {"nom_filleul": "ADECHINA AMIRATH", "photo_filleul": "filleul/image1.jpg", "matricule_filleul": 1},
    2: {"nom_filleul": "AGBATOU ANOUAMAN", "photo_filleul": "filleul/image2.jpg", "matricule_filleul": 2},
    3: {"nom_filleul": "ANANI KOUAKOU FOKOUO", "photo_filleul": "filleul/image3.jpeg", "matricule_filleul": 3},
    4: {"nom_filleul": "APPIENY ELISABETH", "photo_filleul": "filleul/singe1.jpg", "matricule_filleul": 4},
    5: {"nom_filleul": "BANOKA BIH-KOM STONNE", "photo_filleul": "filleul/singe1.jpg", "matricule_filleul": 5},
    6: {"nom_filleul": "BASSA KOUAME YANNIC", "photo_filleul": "filleul/image6.jpg", "matricule_filleul": 6},
    7: {"nom_filleul": "BINDE GHISLAIN", "photo_filleul": "filleul/image7.jpg", "matricule_filleul": 7},
    8: {"nom_filleul": "BOLDAR JOSEPH", "photo_filleul": "filleul/singe2.jpg", "matricule_filleul": 8},
    9: {"nom_filleul": "DANHO GBADJI BASILE", "photo_filleul": "filleul/singe2.jpg", "matricule_filleul": 9},
    10: {"nom_filleul": "DEMBELE EL HADJ", "photo_filleul": "filleul/image10.jpeg", "matricule_filleul": 10},
    11: {"nom_filleul": "DIALLO ALIMATOU", "photo_filleul": "filleul/singe3.jpg", "matricule_filleul": 11},
    12: {"nom_filleul": "DOUMBIA OUMAR", "photo_filleul": "filleul/image12.jpeg", "matricule_filleul": 12},
    13: {"nom_filleul": "FALANAN AURELLE", "photo_filleul": "filleul/image13.jpeg", "matricule_filleul": 13},
    14: {"nom_filleul": "FANNY TIEMOKO", "photo_filleul": "filleul/singe3.jpg", "matricule_filleul": 14},
    15: {"nom_filleul": "FONGORO CHRIST", "photo_filleul": "filleul/singe1.jpg", "matricule_filleul": 15},
    16: {"nom_filleul": "GBALLOU JEAN-CHRIST", "photo_filleul": "filleul/singe2.jpg", "matricule_filleul": 16},
    17: {"nom_filleul": "GOLE BI TRA DECLAIR", "photo_filleul": "filleul/image17.jpg", "matricule_filleul": 17},
    18: {"nom_filleul": "KAM YELI JOANNE", "photo_filleul": "filleul/image18.jpg", "matricule_filleul": 18},
    19: {"nom_filleul": "KING RAOUL JAMES", "photo_filleul": "filleul/image19.jpg", "matricule_filleul": 19},
    20: {"nom_filleul": "KOFFI MARIE MARTHE", "photo_filleul": "filleul/image20.jpg", "matricule_filleul": 20},
    21: {"nom_filleul": "KOFFI EZECHIEL", "photo_filleul": "filleul/image21.jpg", "matricule_filleul": 21},
    22: {"nom_filleul": "KONAN AFFOUE RUTH", "photo_filleul": "filleul/image22.jpg", "matricule_filleul": 22},
    23: {"nom_filleul": "KONATE DRAMANE", "photo_filleul": "filleul/image23.jpeg", "matricule_filleul": 23},
    24: {"nom_filleul": "KONATE MAMADOU", "photo_filleul": "filleul/image24.jpeg", "matricule_filleul": 24},
    25: {"nom_filleul": "KONE ADAMA", "photo_filleul": "filleul/singe3.jpg", "matricule_filleul": 25},
    26: {"nom_filleul": "KONE AMARA", "photo_filleul": "filleul/singe1.jpg", "matricule_filleul": 26},
    27: {"nom_filleul": "KONE TIEMOKO KADER", "photo_filleul": "filleul/image27.jpg", "matricule_filleul": 27},
    28: {"nom_filleul": "KONE WASSA", "photo_filleul": "filleul/image28.jpeg", "matricule_filleul": 28},
    29: {"nom_filleul": "KOUAKOU KONAN ARMAND ", "photo_filleul": "filleul/image29.jpg", "matricule_filleul": 29},
    30: {"nom_filleul": "KOUAME CHARLEMAGNE", "photo_filleul": "filleul/singe3.jpg", "matricule_filleul": 30},
    31: {"nom_filleul": "KOUASSI AHOU CHANTAL", "photo_filleul": "filleul/image31.jpg", "matricule_filleul": 31},
    32: {"nom_filleul": "KOUASSI NICARETTE", "photo_filleul": "filleul/image32.jpg", "matricule_filleul": 32},
    33: {"nom_filleul": "KOUASSI YAO OTHNIEL", "photo_filleul": "filleul/image33.jpg", "matricule_filleul": 33},
    34: {"nom_filleul": "KOUMAN ABRAN MOYE", "photo_filleul": "filleul/image34.jpg", "matricule_filleul": 34},
    35: {"nom_filleul": "KOUMAN FLAVIO-JUNIOR", "photo_filleul": "filleul/image35.jpg", "matricule_filleul": 35},
    36: {"nom_filleul": "LATTE WILFRIED", "photo_filleul": "filleul/image36.jpg", "matricule_filleul": 36},
    37: {"nom_filleul": "LOH NANOU ALAIN", "photo_filleul": "filleul/image37.jpg", "matricule_filleul": 37},
    38: {"nom_filleul": "MOHA OUMAROU", "photo_filleul": "filleul/image38.jpg", "matricule_filleul": 38},
    39: {"nom_filleul": "N'CHO LAUNES HELZE", "photo_filleul": "filleul/image39.jpg", "matricule_filleul": 39},
    40: {"nom_filleul": "N'DRI FRANCK-IVAN", "photo_filleul": "filleul/image40.jpg", "matricule_filleul": 40},
    41: {"nom_filleul": "NABOUE BI DANIEL", "photo_filleul": "filleul/image41.jpeg", "matricule_filleul": 41},
    42: {"nom_filleul": "OUATTARA BOMBO YVES", "photo_filleul": "filleul/image42.jpg", "matricule_filleul": 42},
    43: {"nom_filleul": "OUATTARA EDMOND", "photo_filleul": "filleul/image43.jpg", "matricule_filleul": 43},
    44: {"nom_filleul": "OUATTARA LAMINE", "photo_filleul": "filleul/image44.jpeg", "matricule_filleul": 44},
    45: {"nom_filleul": "OUSSOU YAO JEAN", "photo_filleul": "filleul/image45.jpeg", "matricule_filleul": 45},
    46: {"nom_filleul": "TANH DION ROCHE", "photo_filleul": "filleul/singe2.jpg", "matricule_filleul": 46},
    47: {"nom_filleul": "TANO ASSANDE LANDRY", "photo_filleul": "filleul/image47.jpg", "matricule_filleul": 47},
    48: {"nom_filleul": "TAPSOBA GISELE", "photo_filleul": "filleul/image48.jpg", "matricule_filleul": 48},
    49: {"nom_filleul": "TIA PATERNE", "photo_filleul": "filleul/image49.jpg", "matricule_filleul": 49},
    50: {"nom_filleul": "TRA BI DIEUDONNE", "photo_filleul": "filleul/image50.jpg", "matricule_filleul": 50},
    51: {"nom_filleul": "TRAORE MORISSENEFOU", "photo_filleul": "filleul/image51.jpg", "matricule_filleul": 51},
    52: {"nom_filleul": "WHEI ASHALL DAVID", "photo_filleul": "filleul/image52.jpeg", "matricule_filleul": 52},
    53: {"nom_filleul": "YA KOFFI JEAN EUDES", "photo_filleul": "filleul/image53.jpg", "matricule_filleul": 53}
}
# Créer une fenêtre principale
fenetre = tk.Tk()
fenetre.title("Liste des filleuls")

# Créer un canvas pour afficher les informations des filleuls
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

# Afficher les informations de chaque filleul dans la grille
for i, (filleul_id, info) in enumerate(filleul.items()):
    ligne = i // nombre_colonnes
    colonne = i % nombre_colonnes

    # Coordonnées de la cellule dans la grille
    x1 = colonne * largeur_cellule
    y1 = ligne * hauteur_cellule
    x2 = x1 + largeur_cellule
    y2 = y1 + hauteur_cellule

    image =Image.open(info["photo_filleul"])
    image.thumbnail((largeur_cellule - 20, hauteur_cellule - 20))  # Redimensionner l'image pour s'adapter à la cellule
    photo = ImageTk.PhotoImage(image)
    images.append(photo)  # Ajouter l'image à la liste

    # Afficher l'image
    canvas.create_image(x1 + 10, y1 + 10, anchor=tk.NW, image=photo)
    
    # Afficher le nom
    canvas.create_text(x1 + 10, y1 + hauteur_cellule - 10, text="Nom: " + info["nom_filleul"], anchor=tk.W)

    # Afficher le matricule
    canvas.create_text(x1 + 10, y1 + hauteur_cellule - 30, text="Matricule: " + str(info["matricule_filleul"]), anchor=tk.W)

# Lancer la boucle principale de l'application
fenetre.mainloop()














