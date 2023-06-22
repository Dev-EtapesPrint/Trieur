# Trieur

## Tri de fichiers en fonction de leur extension

Dans ce repo GitHub, il y a deux programmes Python nommés **trieur.py** et **détrieur.py**, qui permettent de trier les fichiers téléchargés en fonction de leur extension.

### Tri des fichiers

Le programme **trieur.py** parcourt tous les fichiers présents dans le dossier spécifié et vérifie leur extension. Si l'extension n'est pas .ini et que le nom du fichier ne correspond pas à trieur.py ou détrieur.py, le fichier est déplacé vers un dossier portant le nom de l'extension dans le répertoire de téléchargement. Les fichiers qui ont la même extension sont déplacés dans le même dossier. Si le dossier pour cette extension n'existe pas, le programme le crée.

### Classement de retour

Une fois que le programme a terminé le triage des fichiers, tous les fichiers sont classés par extensin dans un dossier distinct. 

### Déclassement des fichiers

Le programme **détrieur.py** parcourt tous les dossiers créés par le programme **trieur.py** et déplace tous les fichiers dans leur dossier de téléchargement, en supprimant les dossiers qui ont été créés par le programme de triage une fois que tous les fichiers ont été déplacés.

Pour utiliser le programme, modifiez le chemin du dossier de téléchargement dans les deux programmes pour qu'il corresponde à votre dossier de téléchargement. Ensuite, exécutez **trieur.py** et tous les fichiers du dossier de téléchargement seront triés par extension. Pour déplacer les fichiers dans le dossier de téléchargement initial, exécutez **détrieur.py** après que le programme de triage ait terminé de classer vos fichiers.