// Which Wins? No. 8: the C side. Add up the squares of 100,000,000 numbers, two ways.
// Build: gcc -O2 -o sum sum.c     Run: ./sum
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 100000000
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }
int main(void) {
    double *a = malloc(sizeof(double) * N);
    for (long i = 0; i < N; i++) a[i] = (double)(i % 1000);
    for (int run = 0; run < 5; run++) {
        double t0 = now(), total = 0;
        for (long i = 0; i < N; i++) total += a[i] * a[i];
        double t1 = now();
        printf("c_loop %.1f ms total %.0f\n", (t1 - t0) * 1e3, total);
    }
    free(a); return 0;
}
