import random


# Float entre 0 et 1 exclus
print(random.random())


# Aléatoire N entre a <= N <= b donc inclus
print(random.randint(1, 10))

# Variante avec un pas et exclusion de b
print(random.randrange(1, 10, 3))

# Séquences
seq = ["Pain", "Beurre", "Jambon"]
# Mélange
random.shuffle(seq)
print(seq)

# Choisir k élément(s) dans une liste
print(random.sample(seq, 1))
