import random
import os
import argparse

def generate_random_file(file_path, size_mb):
    # Convertir la taille de mégaoctets en octets
    size_bytes = size_mb * 1024 * 1024

    # Générer des caractères aléatoires jusqu'à atteindre la taille spécifiée
    with open(file_path, 'w') as f:
        while os.path.getsize(file_path) < size_bytes:
            # Générer un caractère aléatoire dans la plage des caractères UTF-8
            random_char = chr(random.randint(32, 126))
            f.write(random_char)

def main():
    # Configurer le parseur d'arguments
    parser = argparse.ArgumentParser(description='Générer un fichier texte rempli de caractères aléatoires')
    parser.add_argument('file_path', type=str, help='Chemin du fichier à générer')
    parser.add_argument('size_mb', type=float, help='Taille du fichier en mégaoctets')

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()

    # Appeler la fonction pour générer le fichier
    generate_random_file(args.file_path, args.size_mb)

if __name__ == '__main__':
    main() 
