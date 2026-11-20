// Which Wins? GTA Online's 6-minute load, rebuilt small. The pattern t0st found in 2021 (nee.lv, 28 Feb 2021):
// a ~10 MB JSON shop catalogue of ~63,000 items, read with sscanf (which runs strlen over the rest of the buffer on every call),
// and each item checked against every earlier item before it is stored. "fixed" reads straight through and uses a hash set.
// This is our own reconstruction of that pattern, not Rockstar's code. Build: gcc -O2 load.c -o load   Run: ./load 63000
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef struct { char key[17]; int price; } Item;
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec / 1e9; }
static char *make_catalogue(int n) {                    // [{"key":"<16 hex>","price":N,"pad":"..."}, ...]  ~165 bytes per item
  size_t cap = (size_t)n * 200 + 16; char *s = malloc(cap), *p = s; unsigned long long x = 88172645463325252ULL;
  *p++ = '[';
  for (int i = 0; i < n; i++) {
    x ^= x << 13; x ^= x >> 7; x ^= x << 17;
    p += sprintf(p, "%s{\"key\":\"%016llx\",\"price\":%d,\"pad\":\"%.100s\"}", i ? "," : "", x, (int)(x % 9000000),
                 "................................................................................................................");
  }
  *p++ = ']'; *p = 0; return s;
}
static int original(const char *s, Item *out) {         // sscanf per item + linear duplicate check: the 2021 pattern
  int n = 0, used; const char *p = s + 1; Item it;
  while (sscanf(p, "{\"key\":\"%16[^\"]\",\"price\":%d,\"pad\":\"%*[^\"]\"}%n", it.key, &it.price, &used) == 2) {
    p += used; int dup = 0;
    for (int j = 0; j < n; j++) if (strcmp(out[j].key, it.key) == 0) { dup = 1; break; }
    if (!dup) out[n++] = it;
    if (*p == ',') p++; else break;
  }
  return n;
}
static unsigned long long hashkey(const char *k) { unsigned long long h = 1469598103934665603ULL; while (*k) h = (h ^ (unsigned char)*k++) * 1099511628211ULL; return h; }
static int fixed(const char *s, Item *out, int cap) {   // read straight through + hash set
  int n = 0, slots = 1; while (slots < cap * 2) slots <<= 1; int *set = malloc(sizeof(int) * slots); memset(set, -1, sizeof(int) * slots);
  const char *p = s + 1; Item it;
  while (*p == '{') {
    const char *k = p + 8; memcpy(it.key, k, 16); it.key[16] = 0;
    p = k + 16 + 10; it.price = (int)strtol(p, (char **)&p, 10);
    p = strchr(p + 8, '"') + 2;                          // skip ,"pad":"...."}
    unsigned long long h = hashkey(it.key) & (slots - 1); int dup = 0;
    while (set[h] >= 0) { if (strcmp(out[set[h]].key, it.key) == 0) { dup = 1; break; } h = (h + 1) & (slots - 1); }
    if (!dup) { set[h] = n; out[n++] = it; }
    if (*p == ',') p++; else break;
  }
  free(set); return n;
}
static int parse_fixed_dedup_old(const char *s, Item *out) {   // straight-through read, but still the linear duplicate check
  int n = 0; const char *p = s + 1; Item it;
  while (*p == '{') {
    const char *k = p + 8; memcpy(it.key, k, 16); it.key[16] = 0; p = k + 16 + 10; it.price = (int)strtol(p, (char **)&p, 10);
    p = strchr(p + 8, '"') + 2; int dup = 0;
    for (int j = 0; j < n; j++) if (strcmp(out[j].key, it.key) == 0) { dup = 1; break; }
    if (!dup) out[n++] = it;
    if (*p == ',') p++; else break;
  }
  return n;
}
int main(int argc, char **argv) {
  int n = argc > 1 ? atoi(argv[1]) : 63000; char *s = make_catalogue(n); Item *a = malloc(sizeof(Item) * n), *b = malloc(sizeof(Item) * n);
  double t0 = now(); int na = fixed(s, b, n); double tf = now() - t0;
  t0 = now(); int nb = original(s, a); double to = now() - t0;
  double ts = -1; if (argc > 2) { Item *c = malloc(sizeof(Item) * n); t0 = now(); parse_fixed_dedup_old(s, c); ts = now() - t0; free(c); }   // ./load N split: time "only the reading fixed"
  long long sum = 0; for (int i = 0; i < na && i < nb; i++) if (strcmp(a[i].key, b[i].key) != 0 || a[i].price != b[i].price) sum++;   // items that differ (0 = identical output)
  printf("{\"items\":%d,\"bytes\":%zu,\"original_s\":%.6f,\"fixed_s\":%.6f,\"read_fixed_only_s\":%.6f,\"parsed\":[%d,%d],\"diff\":%lld}\n", n, strlen(s), to, tf, ts, nb, na, sum);
  return na != nb || sum != 0;
}
