# GPU performance in GFLOPS

This is from this project https://github.com/ProjectPhysX/FluidX3D which got some of my results:

Colors: 🔴 AMD, 🔵 Intel, 🟢 Nvidia, ⚪ Apple, 🟡 ARM

|             Device              | FP32 [GFlops/s] | Mem [GB] | BW [GB/s] | FP32/FP32 [MLUPs/s] |
|:--------------------------------|----------------:|---------:|----------:|--------------------:|
| 🟡 Raspberry Pi 3               |                 |          |           |                     |
| 🔵 UHD Graphics 620 (i5 7300U)  |             422 |        6 |        10 |                  72 |
| 🔵 UHD Graphics 630 (i5 8500T)  |             422 |       13 |        23 |                 150 |
| 🔵 UHD Graphics 770 (i7 13700T) |             819 |        4 |        20 |                 135 |
| ⚪ Apple M1                     |           2,048 |       11 |        56 |                 727 |
| 🟢 GTX 960                      |           2,593 |        2 |        79 |                 513 |
| 🔴 RX 470                       |           5,022 |        4 |       152 |                1006 |
| 🟢 P106-100                     |           4,372 |        6 |       145 |                2045 |
| 🔴 RX 6600                      |           7,326 |        8 |       141 |                 922 |
| 🟢 RTX 3060 Ti                  |          16,197 |        8 |       398 |                2604 |
| 🟢 RTX 3070 Ti                  |          21,750 |        8 |       529 |                3465 |

A run looks like this

``` bash
.-----------------------------------------------------------------------------.
|                       ______________   ______________                       |
|                       \   ________  | |  ________   /                       |
|                        \  \       | | | |       /  /                        |
|                         \  \      | | | |      /  /                         |
|                          \  \     | | | |     /  /                          |
|                           \  \_.-"  | |  "-._/  /                           |
|                            \    _.-" _ "-._    /                            |
|                             \.-" _.-" "-._ "-./                             |
|                               .-"  .-"-.  "-.                               |
|                               \  v"     "v  /                               |
|                                \  \     /  /                                |
|                                 \  \   /  /                                 |
|                                  \  \ /  /                                  |
|                                   \  '  /                                   |
|                                    \   /                                    |
|                                     \ /               FluidX3D Version 2.13 |
|                                      '     Copyright (c) Dr. Moritz Lehmann |
|-----------------------------------------------------------------------------|
|----------------.------------------------------------------------------------|
| Device ID    0 | NVIDIA GeForce RTX 3070 Ti                                 |
|----------------'------------------------------------------------------------|
|----------------.------------------------------------------------------------|
| Device ID      | 0                                                          |
| Device Name    | NVIDIA GeForce RTX 3070 Ti                                 |
| Device Vendor  | NVIDIA Corporation                                         |
| Device Driver  | 551.23 (Windows)                                           |
| OpenCL Version | OpenCL C 1.2                                               |
| Compute Units  | 48 at 1770 MHz (6144 cores, 21.750 TFLOPs/s)               |
| Memory, Cache  | 8191 MB, 1344 KB global / 48 KB local                      |
| Buffer Limits  | 2047 MB global, 64 KB constant                             |
|----------------'------------------------------------------------------------|
| Info: OpenCL C code successfully compiled.                                  |
| Info: Allocating memory. This may take a few seconds.                       |
|-----------------.-----------------------------------------------------------|
| Grid Resolution |                                256 x 256 x 256 = 16777216 |
| Grid Domains    |                                             1 x 1 x 1 = 1 |
| LBM Type        |                                     D3Q19 SRT (FP32/FP32) |
| Memory Usage    |                                CPU 272 MB, GPU 1x 1488 MB |
| Max Alloc Size  |                                                   1216 MB |
| Time Steps      |                                                        10 |
| Kin. Viscosity  |                                                1.00000000 |
| Relaxation Time |                                                3.50000000 |
| Reynolds Number |                                                  Re < 148 |
|---------.-------'-----.-----------.-------------------.---------------------|
| MLUPs   | Bandwidth   | Steps/s   | Current Step      | Time Remaining      |
|    3456 |    529 GB/s |       206 |         9997  70% |                  0s |
|---------'-------------'-----------'-------------------'---------------------|
| Info: Peak MLUPs/s = 3465                                                   |
-------------------------------------------------------------------------------
```


I need more time to find software and do the measurements, but I was inpired by the comparison of the graphics performance of my PS4 Pro to other consoles. 

## FP32 single

Let's assume this is possible max raw performance in long (32 bit or single) FP32

- PS2			GFLOPS 		16 Pixel shaders
- PS3
- PS4 		1840 GFLOPS		18 CU, 8 GB GDDR5 memory 5500 MT/s
- PS4 Pro	4198 GFLOPS		36 CU, 32 ROPs, 144 TMUs, 2304 Cores, 256 bit bus, 217.6 GB/s
- PS5
- RX 470 	3793 GFLOPS
- Apple M1 	2600 GFLOPS (8-core, 128 CU or execution units, handle nearly 25,000 threads
- XBOX 360
- Xbos one S 
- XBox Series S 
- XBox Series X 

In many cases it can be simple calculated by the CPU architecture and the frequency. For example my dual [https://ark.intel.com/content/www/us/en/ark/products/37106/intel-xeon-processor-x5550-8m-cache-2-66-ghz-6-40-gt-s-intel-qpi.html](Xeon X5550) with 2.67 GHz has a [https://en.wikipedia.org/wiki/FLOPS](multiplier of 8) (Nehalem EP) which results in 2.67 x 8 = 21.36 gflops.

## FP64 double

- RX 470 	237 GFLOPS
