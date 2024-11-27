# AES filecrypt

Chiffrement et déchiffrement d'un fichier avec le système cryptographique AES en langage Python.

Ce programme est créé à des fins de *benchmarking* et d'étude comparative.

Le document à chiffrer/déchiffrer doit être nommé *input.txt*.
Le programme générera une clé cryptographique si aucune n'est spécifiée.
Le vecteur d'initialisation est fixé.

L'utilisation du programme est la suivante en ligne de commande : ```bash python3 filecrypt.py input.txt```

Assurez-vous d'installer la bibliothèque ```pycryptodome``` avant d'exécuter le code : ```bash pip install pycryptodome```
