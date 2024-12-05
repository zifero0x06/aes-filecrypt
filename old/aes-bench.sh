#!/bin/bash

# Nombre d'exécutions
NUM_RUNS=10

# Tableau pour stocker les temps d'exécution
times=()

# Boucle pour exécuter le programme 10 fois
for ((i=1; i<=NUM_RUNS; i++)); do
    # Exécuter le programme avec time et capturer le temps d'exécution
    start=$(date +%s%N)
    python3 ./filecrypt-const.py input.txt output.bin --encrypt
    end=$(date +%s%N)

    # Calculer le temps d'exécution en secondes
    duration=$((end - start))
    duration_sec=$(echo "scale=3; $duration / 1000000000" | bc)

    # Ajouter le temps d'exécution au tableau
    times+=($duration_sec)

    # Afficher le temps d'exécution pour chaque itération
    echo "Run $i: $duration_sec seconds"
done

# Calculer la moyenne des temps d'exécution
sum=0
for time in "${times[@]}"; do
    sum=$(echo "$sum + $time" | bc)
done

average=$(echo "scale=3; $sum / $NUM_RUNS" | bc)

# Afficher la moyenne des temps d'exécution
echo "Average execution time: $average seconds"
