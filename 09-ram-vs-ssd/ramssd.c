// Which Wins? No. 9: RAM vs SSD. Build: gcc -O2 -o ramssd ramssd.c
//   ./ramssd mkfile F          write 1 GiB to F and force it onto the disk (fsync)
//   ./ramssd seq-ram           copy 1 GiB that is already in RAM, 8 MiB at a time
//   ./ramssd seq-ssd F         read F from the disk, 8 MiB at a time (O_DIRECT: no in-memory copy helps)
//   ./ramssd seq-cached F      read F the normal way (the system may serve it from its in-memory copy)
//   ./ramssd rnd-ram N         N lookups at random places in 1 GiB of RAM: copy a 4 KiB record out and add it up
//   ./ramssd rnd-ssd F N       the same N lookups in F on the disk (O_DIRECT)
//   ./ramssd rnd-cached F N    the same N lookups in F the normal way (the system may serve them from its in-memory copy)
//   ./ramssd hold F            keep 1 GiB in RAM, write the same 1 GiB to F (fsync), print its checksum, then wait to be killed
//   ./ramssd verify F          checksum of F
#define _GNU_SOURCE
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#define GB (1UL << 30)
#define CH (8UL << 20)
#define BLK 4096UL
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }
static uint64_t rng = 88172645463325252ULL;
static uint64_t next(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
static unsigned char *big(void) { unsigned char *p; if (posix_memalign((void **)&p, BLK, GB)) exit(1); for (size_t i = 0; i < GB; i += 8) *(uint64_t *)(p + i) = i * 2654435761UL; return p; }
static uint64_t sum(const unsigned char *p, size_t n) { uint64_t s = 0; for (size_t i = 0; i < n; i += 8) s += *(const uint64_t *)(p + i); return s; }
int main(int c, char **v) {
    if (c < 2) return 1; const char *m = v[1];
    if (!strcmp(m, "mkfile") || !strcmp(m, "hold")) {
        unsigned char *p = big(); int fd = open(v[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
        for (size_t i = 0; i < GB; i += CH) if (write(fd, p + i, CH) != (ssize_t)CH) return 2;
        fsync(fd); close(fd); printf("checksum %lu bytes %lu\n", sum(p, GB), GB); fflush(stdout);
        if (!strcmp(m, "hold")) { for (;;) pause(); } return 0; }
    if (!strcmp(m, "verify")) { unsigned char *b; posix_memalign((void **)&b, BLK, CH); int fd = open(v[2], O_RDONLY); uint64_t s = 0, n = 0; ssize_t k; while ((k = read(fd, b, CH)) > 0) { s += sum(b, k); n += k; } printf("checksum %lu bytes %lu\n", s, n); return 0; }
    if (!strcmp(m, "seq-ram")) { unsigned char *p = big(), *b; posix_memalign((void **)&b, BLK, CH); memset(b, 1, CH);
        for (int r = 0; r < 5; r++) { double t = now(); uint64_t s = 0; for (size_t i = 0; i < GB; i += CH) { memcpy(b, p + i, CH); s += b[r]; } printf("seq_ram %.1f ms %lu\n", (now() - t) * 1e3, s); } return 0; }
    if (!strcmp(m, "seq-ssd") || !strcmp(m, "seq-cached")) { unsigned char *b; posix_memalign((void **)&b, BLK, CH); int direct = !strcmp(m, "seq-ssd");
        for (int r = 0; r < (direct ? 3 : 4); r++) { int fd = open(v[2], O_RDONLY | (direct ? O_DIRECT : 0)); double t = now(); uint64_t n = 0; ssize_t k; while ((k = read(fd, b, CH)) > 0) n += k; printf("%s %.1f ms %lu\n", direct ? "seq_ssd" : "seq_cached", (now() - t) * 1e3, n); close(fd); } return 0; }
    if (!strcmp(m, "rnd-ram")) { long N = atol(v[2]); unsigned char *p = big(), b[BLK];
        for (int r = 0; r < 5; r++) { rng = 88172645463325252ULL; double t = now(); uint64_t s = 0; for (long i = 0; i < N; i++) { size_t off = (next() % (GB / BLK)) * BLK; memcpy(b, p + off, BLK); s += sum(b, BLK); } printf("rnd_ram %.2f ms %lu\n", (now() - t) * 1e3, s); } return 0; }
    if (!strcmp(m, "rnd-ssd") || !strcmp(m, "rnd-cached")) { long N = atol(v[3]); unsigned char *b; posix_memalign((void **)&b, BLK, BLK); int direct = !strcmp(m, "rnd-ssd");
        for (int r = 0; r < 3; r++) { int fd = open(v[2], O_RDONLY | (direct ? O_DIRECT : 0)); rng = 88172645463325252ULL; double t = now(); uint64_t s = 0; for (long i = 0; i < N; i++) { off_t off = (next() % (GB / BLK)) * BLK; if (pread(fd, b, BLK, off) != (ssize_t)BLK) return 3; s += sum(b, BLK); } printf("%s %.1f ms %lu\n", direct ? "rnd_ssd" : "rnd_cached", (now() - t) * 1e3, s); close(fd); } return 0; }
    return 1;
}
