import os
import shutil

# Chemin du dossier de téléchargement
download_directory = '.'

# Boucle sur tous les dossiers dans le dossier de téléchargement
for foldername in os.listdir(download_directory):
    # Verifie si le dossier porte le nom du fichier officiel (commence par "Fichier ")
    if foldername.startswith("Fichier "):
        folderpath = os.path.join(download_directory, foldername)
        # Boucle sur tous les fichiers dans le dossier actuel
        for filename in os.listdir(folderpath):
            # Chemin complet du fichier dans le dossier actuel
            filepath = os.path.join(folderpath, filename)
            # Déplace le fichier dans le dossier de téléchargement
            shutil.move(filepath, os.path.join(download_directory, filename))
        # Supprime le dossier une fois que tous les fichiers ont été déplacés
        os.rmdir(folderpath)