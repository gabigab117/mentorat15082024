import re


# Ce qu'on cherche et combien de fois on le cherche

# ".": "N'importe quel caractère sauf nouvelle ligne",
# "\d": "Chiffre eq [0-9]",
# "\D": "Non-chiffre", eq [^0-9]
# "\w": "Caractère alphanumérique [a-zA-Z0-9]",
# "\W": "Non-alphanumérique",
# "\s": "Espace blanc (espace, tabulation, nouvelle ligne)",
# "\S": "N'importe quel caractère non-espace blanc",
# "[abc]": "Un des caractères listés",
# "[^abc]": "Aucun des caractères listés",
# "[a-z]": "Intervalle de caractères (de a à z)",
# "\b": "Limite de mot", ex chat chateau
# "^": "Début de ligne",
# "$": "Fin de ligne",
# "\.": "Caractère d'échappement" pourc chercher un . par exemple

# Pour quantifier

# "*": "0 ou plus",
# "+": "1 ou plus",
# "?": "0 ou 1",
# "{n}": "Exactement n fois",
# "{n,}": "n fois ou plus",
# "{n,m}": "Entre n et m fois"

# "|": "Ou (alternative)", (dupont|dupond)
# "()": "Groupe de capture",

# Penser à utiliser une chaine "brut" avec r, pour ne pas avoir un espace avec \n. Mais n'affecte pas les back
# pour le moteur d'expressions régulières.





# 1. Fonction match qui permet de chercher dans une str ce qui correspond à notre regex (en partant du DEBUT)

a = re.match(r".{2}", "Dupond et Dupont")
print(a)
print(a.group())
print("-------")

# On peut créer des groupes
b = re.match(r"(\w+)\s(\w+)\s(\w+)", "Dupond et Dupont")  # (\s) je créer un autre groupe
print(b.group())  # Tout le match
print(b.group(1))  # Premier groupe
print(b.group(2))
print(b.group(3))
print(b.groups())  # Tous les groupes capturés en une seule fois

print("---- fin match")
# 2. Fonction search dans toutes la str, première occurence

print("Avec search")
a = re.search(r'([\w.]+)@(\w+)\.([a-z]{2,4})', "Salut tout le mon son email c'est gabriel.trouve5@gmail.com, gt45@outlook.com")
print(a.groups())

# 3. Fonction findall, toutes la str et pas uniquement la première occurence

print("avec findall")
a = re.findall(r'([\w.]+)@(\w+)\.([a-z]{2,4})', "Salut tout le mon son email c'est gabriel.trouve5@gmail.com, gt45@outlook.com")
print(a)

# 3. re split

texte = "Chien, chat, mouton | bélier"
print(re.split(r", | \| ", texte))


print("____ en desssous, sans groupe")
b = re.match(r"\w+\s\w+\s\w+", "Dupond et Dupont")  # (\s) je créer un autre groupe
print(b.group())
