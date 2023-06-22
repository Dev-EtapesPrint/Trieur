import os
import shutil

# Chemin du dossier de téléchargement
download_directory = '.'

# Boucle sur tous les fichiers dans le dossier de téléchargement
for filename in os.listdir(download_directory):
    if not filename.endswith('.ini') and filename not in ['trieur.py', 'détrieur.py']:
        # Chemin complet du fichier dans le dossier de téléchargement
        filepath = os.path.join(download_directory, filename)
        
        # Vérifie si c'est un fichier
        if os.path.isfile(filepath):
            # Trouve l'extension du fichier
            extension = os.path.splitext(filepath)[1][1:]
            
            # Crée le dossier pour cette extension s'il n'existe pas
            if not os.path.exists(os.path.join(download_directory, "Fichier " + extension)):
                os.makedirs(os.path.join(download_directory, "Fichier " + extension))
            
            # Déplace le fichier dans le bon dossier
            shutil.move(filepath, os.path.join(download_directory, "Fichier " + extension, filename))
