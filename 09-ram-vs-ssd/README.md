# Which Wins? No. 9: RAM vs SSD

**Which is faster, RAM or an SSD?**

## Run it yourself

```
gcc -O2 -o ramssd ramssd.c
./ramssd mkfile data.bin          # writes a 1 GB test file here
./ramssd rnd-ram 100000
./ramssd rnd-ssd data.bin 100000   # reads straight from the drive (O_DIRECT, Linux)
rm data.bin
```

## Our result

Intel Core i9-14900HX laptop, NVMe SSD read from Linux inside WSL2 (which adds some delay to every disk request), gcc -O2, median of 5 runs. Round 1 reads with the system's in-memory copy switched off; read the normal way after one full read, the same lookups took about 58 ms.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Look up 100,000 records of 4 KB at random places in the same 1 GB | RAM 46 ms, SSD 11,249 ms: RAM 245x faster | RAM |
| 2 | The program holding the data is killed (kill -9) | RAM: 0 bytes left. SSD file: all 1,073,741,824 bytes back, same checksum | SSD |

Your numbers will differ by machine. The winner of each round should not.

## The rule

RAM is fast but forgets; disk is slow but remembers. Real systems use both.

## In an interview

**Why do databases write a log to disk before changing data?**
So that after a crash they can rebuild every change from the log; memory is wiped when the process dies.

[Watch the reel](https://www.instagram.com/reel/DfpBCuCDo2F/)
