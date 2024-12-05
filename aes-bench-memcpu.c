/****

Ce programme limite son exécution à un seul coeur de processeur et à 512 Mo de mémoire. 
Il exécute ensuite une commande Python spécifiée en argument un certain nombre de fois (défini par NUM_RUNS) et mesure le temps d'exécution de chaque itération.

Pour compiler ce programme, vous pouvez utiliser la commande suivante :
gcc -o your_program your_program.c

****/

#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sched.h>
#include <unistd.h>
#include <sys/resource.h>

#define NUM_RUNS 10
#define MEMORY_LIMIT_MB 512

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <python_command>\n", argv[0]);
        return 1;
    }

    // Set memory limit to 512 MB
    struct rlimit rl;
    rl.rlim_cur = MEMORY_LIMIT_MB * 1024 * 1024; // Convert MB to bytes
    rl.rlim_max = MEMORY_LIMIT_MB * 1024 * 1024; // Convert MB to bytes
    if (setrlimit(RLIMIT_AS, &rl) != 0) {
        perror("setrlimit");
        return 1;
    }

    double times[NUM_RUNS];
    double sum = 0;
    double average;
    char *command = argv[1];
    clock_t start, end;
    double cpu_time_used;

    // Set CPU affinity to a specific core (e.g., core 0)
    cpu_set_t mask;
    CPU_ZERO(&mask);
    CPU_SET(0, &mask);
    if (sched_setaffinity(0, sizeof(mask), &mask) == -1) {
        perror("sched_setaffinity");
        return 1;
    }

    for (int i = 0; i < NUM_RUNS; i++) {
        start = clock();
        system(command);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        times[i] = cpu_time_used;
        printf("Run %d: %f seconds\n", i + 1, cpu_time_used);
    }

    for (int i = 0; i < NUM_RUNS; i++) {
        sum += times[i];
    }

    average = sum / NUM_RUNS;
    printf("Average execution time: %f seconds\n", average);

    return 0;
}
