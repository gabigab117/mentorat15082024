def additionner_nombres(nombre1, nombre2):
    """
    Additionne deux nombres.

    Cette fonction prend deux arguments numériques, les additionne et renvoie le résultat.
    Si l'un des arguments n'est pas un nombre (int ou float), une exception est levée.

    Args:
        nombre1 (int or float): Le premier nombre à additionner.
        nombre2 (int or float): Le second nombre à additionner.

    Returns:
        int or float: La somme des deux nombres.

    Raises:
        TypeError: Si l'un des arguments n'est pas un nombre.
    """
    if not isinstance(nombre1, (int, float)) or not isinstance(nombre2, (int, float)):
        raise TypeError("Les deux paramètres doivent être des nombres (int ou float).")

    return nombre1 + nombre2


assert "Additionne deux nombres." in additionner_nombres.__doc__, "La docstring doit contenir la description de la fonction."
assert "Args:" in additionner_nombres.__doc__, "La docstring doit contenir la section Args."
assert "Returns:" in additionner_nombres.__doc__, "La docstring doit contenir la section Returns."
assert "Raises:" in additionner_nombres.__doc__, "La docstring doit contenir la section Raises."

print(additionner_nombres.__doc__)

# Description courte
# Détail
# Arguments
# Valeur retour
# Exceptions


# https://peps.python.org/pep-0257/ (proposition d'amélioration Python)
