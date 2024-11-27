# AES filecrypt

Chiffrement et déchiffrement d'un fichier avec le système cryptographique AES et le mode opératoire CBC (par défaut) en langage Python.
Ce programme est créé à des fins de *benchmarking* et d'étude comparative. Un fichier ```input.txt``` est donné à titre d'exemple.

Le document à chiffrer/déchiffrer doit être nommé *input.txt*.
Assurez-vous d'installer la bibliothèque ```pycryptodome``` avec la commande ```pip install pycryptodome``` avant d'exécuter le code.

## AES filecrypt existe en trois versions différentes

  - ```filecrypt-auto.py``` qui génère automatiquement un vecteur d'initialisation et une clé cryptographique AES en 256 bits :
  	- ```python3 filecrypt-auto.py input.txt``` et le programme va successivement générer IV et clé puis chiffrer et déchiffrer.

    
  - ```filecrypt-const.py``` qui contient un vecteur d'initialisation et une clé cryptographique AES en 256 bits fixes dans le code :
  	- ```python3 filecrypt-const.py input.txt encrypted.bin --encrypt``` pour chiffrer ;
   	- ```python3 filecrypt-const.py encrypted.bin decrypted.txt --decrypt``` pour déchiffrer.


  - ```filecrypt-opt.py``` qui génère automatiquement un vecteur d'initialisation et une clé cryptographique AES en 256 bits si aucun fichier IV ou clé n'est fourni en argument :
  	- ```python3 filecrypt-opt.py input.txt encrypted.bin --key_file key.bin --iv_file iv.bin --encrypt``` pour chiffrer (*key_file* et *iv_file* sont optionnels) ;
   	- ```python3 filecrypt-opt.py encrypted.bin decrypted.txt --key_file key.bin --decrypt``` pour déchiffrer.

## Benchmarking

Pour réaliser le *benchmarking* deux possibilités sont offertes ici par défaut avec le ```filecrypt-const.py``` où l'IV et la clé sont des constantes :
  - utiliser le script bash ```aes-bench.sh``` ;
  - ou utiliser le programme en code C dénommé ```aes-bench.c```.

Le script ```aes-bench.sh``` requiert d'être rendu exécutable avec ```chmod +x ./eas-bench.sh``` puis exécuté dans le même dossier que le ```.py``` avec ```./aes-bench.sh```.

Le programme en C nécessite d'être compilé avec par exemple ```gcc -o aes-bench aes-bench.c``` puis exécuté ```./aes-bench```.
Une version compilé du programme est mise à disposition sur le *repository*.
