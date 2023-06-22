import os
import shutil

# Chemin du dossier de téléchargement
download_directory = 'C:/Users/Gerome/Téléchargement'

# Chemin du dossier du bureau
desktop_directory = 'C:/Users/Gerome/OneDrive/Bureau/Trieur'

# Boucle sur tous les fichiers dans le dossier de téléchargement
for filename in os.listdir(download_directory):
    # Chemin complet du fichier dans le dossier de téléchargement
    filepath = os.path.join(download_directory, filename)
    
    # Vérifie si c'est un fichier
    if os.path.isfile(filepath):
        # Trouve l'extension du fichier
        extension = os.path.splitext(filepath)[1][1:]
        
        # Crée le dossier pour cette extension s'il n'existe pas
        if not os.path.exists(os.path.join(download_directory, extension)):
            os.makedirs(os.path.join(download_directory, extension))
        
        # Déplace le fichier dans le bon dossier
        shutil.move(filepath, os.path.join(download_directory, extension, filename))

# Boucle sur tous les fichiers sur le bureau
for filename in os.listdir(desktop_directory):
    # Chemin complet du fichier sur le bureau
    filepath = os.path.join(desktop_directory, filename)
    
    # Vérifie si c'est un fichier
    if os.path.isfile(filepath):
        # Trouve l'extension du fichier
        extension = os.path.splitext(filepath)[1][1:]
        
        # Crée le dossier pour cette extension s'il n'existe pas
        if not os.path.exists(os.path.join(desktop_directory, extension)):
            os.makedirs(os.path.join(desktop_directory, extension))
        
        # Déplace le fichier dans le bon dossier
        shutil.move(filepath, os.path.join(desktop_directory, extension, filename))