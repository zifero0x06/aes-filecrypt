# AES filecrypt

Chiffrement et déchiffrement d'un fichier avec le système cryptographique AES et le mode opératoire CBC en langage Python.
Ce programme est créé à des fins de *benchmarking* et d'étude comparative.

Le document à chiffrer/déchiffrer doit être nommé *input.txt*.
Assurez-vous d'installer la bibliothèque ```pycryptodome``` avant d'exécuter le code : ```pip install pycryptodome```

### AES filecrypt existe en trois versions différentes

  - ```filecrypt-auto.py``` qui génère automatiquement un vecteur d'initialisation et une clé cryptographique AES en 256 bits :
  	- ```python3 filecrypt-auto.py input.txt``` et le programme va successivement générer IV et clé puis chiffrer et déchiffrer.

    
  - ```filecrypt-const.py``` qui contient un vecteur d'initialisation et une clé cryptographique AES en 256 bits fixes dans le code :
  	- ```python3 filecrypt-const.py input.txt encrypted.bin --encrypt``` pour chiffrer ;
   	- ```python3 filecrypt-const.py encrypted.bin decrypted.txt --decrypt``` pour déchiffrer.


  - ```filecrypt-opt.py``` qui génère automatiquement un vecteur d'initialisation et une clé cryptographique AES en 256 bits si aucun fichier IV ou clé n'est fourni en argument :
  	- ```python3 filecrypt-opt.py input.txt encrypted.bin --key_file key.bin --iv_file iv.bin --encrypt``` pour chiffrer (*key_file* et *iv_file* sont optionnels) ;
   	- ```python3 filecrypt-opt.py encrypted.bin decrypted.txt --key_file key.bin --decrypt``` pour déchiffrer.
