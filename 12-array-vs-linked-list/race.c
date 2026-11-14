// Which Wins? No. 12: array vs linked list in C. Build: gcc -O2 -o race race.c   Run: ./race
// Round 1: add up 10,000,000 numbers stored in an array, and the same numbers in a linked list whose nodes sit at
//          shuffled places in memory (as nodes made at different times usually do). Also, for fairness, a list whose nodes sit in order.
// Round 2: put 2,000 new numbers at the front of a 200,000-number array (every number shifts one place each time)
//          and at the front of a linked list (one new node, one pointer).
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10000000
#define BASE 200000
#define K 2000
typedef struct Node { long v; struct Node *next; } Node;
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }
static unsigned long rng = 88172645463325252UL;
static unsigned long next_rand(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
int main(void) {
    long *a = malloc(sizeof(long) * N); Node *nodes = malloc(sizeof(Node) * N); long *perm = malloc(sizeof(long) * N);
    for (long i = 0; i < N; i++) { a[i] = i; perm[i] = i; }
    for (long i = N - 1; i > 0; i--) { long j = next_rand() % (i + 1), t = perm[i]; perm[i] = perm[j]; perm[j] = t; }
    for (long i = 0; i < N; i++) { nodes[perm[i]].v = i; nodes[perm[i]].next = i + 1 < N ? &nodes[perm[i + 1]] : NULL; }
    Node *shuffled = &nodes[perm[0]];
    Node *ordered = malloc(sizeof(Node) * N); for (long i = 0; i < N; i++) { ordered[i].v = i; ordered[i].next = i + 1 < N ? &ordered[i + 1] : NULL; }
    for (int r = 0; r < 3; r++) {
        double t = now(); long s1 = 0; for (long i = 0; i < N; i++) s1 += a[i]; double ta = now() - t;
        t = now(); long s2 = 0; for (Node *p = shuffled; p; p = p->next) s2 += p->v; double tl = now() - t;
        t = now(); long s3 = 0; for (Node *p = ordered; p; p = p->next) s3 += p->v; double to = now() - t;
        if (s1 != s2 || s1 != s3) return 1;
        printf("r1_array %.2f ms\nr1_list %.2f ms\nr1_list_ordered %.2f ms\ntotal %ld\n", ta * 1e3, tl * 1e3, to * 1e3, s1);
    }
    for (int r = 0; r < 3; r++) {
        long *b = malloc(sizeof(long) * (BASE + K)), n = BASE; for (long i = 0; i < n; i++) b[i] = i;
        double t = now(); for (int k = 0; k < K; k++) { for (long i = n; i > 0; i--) b[i] = b[i - 1]; b[0] = k; n++; } double tai = now() - t;
        Node *h = NULL, *pool = malloc(sizeof(Node) * K); t = now(); for (int k = 0; k < K; k++) { pool[k].v = k; pool[k].next = h; h = &pool[k]; } double tli = now() - t;
        if (b[0] != K - 1 || h->v != K - 1) return 2;
        printf("r2_array %.3f ms\nr2_list %.4f ms\n", tai * 1e3, tli * 1e3); free(b); free(pool);
    }
    return 0;
}
