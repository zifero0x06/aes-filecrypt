#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_RUNS 10

int main() {
    double times[NUM_RUNS];
    double sum = 0;
    double average;
    char command[] = "python3 ./filecrypt-const.py input.txt output.bin --encrypt";
    clock_t start, end;
    double cpu_time_used;

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
