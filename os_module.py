import os
import shutil


# Vérifier le répertoire courant
current = os.getcwd()
print(current)

# Présence d'un fichier
if os.path.exists("file.txt"):
    print("file.txt est présent")
else:
    print("Non présent !")

# Vérifier si un fichier
print(os.path.isfile("dossier_test"))

# os.mkdir("nouveau")

# Supprimer fichier
# os.remove("nom.txt")

# Supprimer un répertoire VIDE
# os.rmdir("dossier_test")
# os.removedirs("dossier_test")  # Plusieurs dossiers de manière récursive

# Renommer
# os.rename("file.txt", "new_file.txt")


# liste des fichiers
files = os.listdir()
print(files)

# Tout supprimer avec shutil
# shutil.rmtree("dossier")
