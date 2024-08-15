# args
# Permet de rendre les fonctions flexibles en acceptant de prendre un nombre variable d'argument


def additionner(*args):
    # args est un tuple
    somme = 0
    for nombre in args:
        somme += nombre
    return somme

# Utilisation de la fonction
print(additionner(1, 2, 3))  # Affiche: 6
print(additionner(10, 20, 50, 20))


def creer_phrase(*mots):
    print(mots)
    return " ".join(mots)

# Utilisation de la fonction
print(creer_phrase("Bonjour", "à", "tous", "!"))  # Affiche: Bonjour à tous !
print(creer_phrase("Python", "est", "génial"))    # Affiche: Python est génial


# kwargs
# Permet de passer un nombre variable d'arguments nommés


def afficher_infos(**kwargs):
    # kwargs est un dict
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Utilisation de la fonction
print(afficher_infos(nom="Dupont", age=30, ville="Paris"))
# Affiche:
# nom: Dupont
# age: 30
# ville: Paris


def creer_profil(nom, *args, **kwargs):
    print(f"Nom: {nom}")
    print("Intérêts:", ", ".join(args))
    print("Informations personnelles:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Utilisation de la fonction
creer_profil("Alice", "Lecture", "Voyage", age=28, ville="Lyon")
# Affiche:
# Nom: Alice
# Intérêts: Lecture, Voyage
# Informations personnelles:
# age: 28
# ville: Lyon


