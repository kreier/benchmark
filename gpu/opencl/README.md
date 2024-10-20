# GPU performance in TFLOPS and TIOPs

This test is taken from https://github.com/ProjectPhysX/OpenCL-Benchmark 

| Device           | FP64<br>double | FP32<br>single | FP16<br>half | INT64<br>long | INT32<br>int | INT16<br>short | INT8<br>char |
|------------------|:--------:|---------:|---------:|:-------:|:-------:|:-------:|:-------:|
| units            | TFLOPs/s | TFLOPs/s | TFLOPs/s | TIOPs/s | TIOPs/s | TIOPs/s | TIOPs/s |
| i5 3320M         |   0.000  |   0.000  |   ---    |  0.003  |  0.016  |  0.032  |  0.018  |
| E3-1226 v3       |   0.047  |   0.046  |   ---    |  0.013  |  0.021  |  0.005  |  0.011  |
| 🔵 HD Gen11      |    ---   |   0.182  |   0.333  |  0.008  |  0.030  |  0.361  |  0.063  |
| 🔵 UHD 620       |   0.097  |   0.365  |   0.659  |  0.013  |  0.115  |  0.642  |  0.129  |
| 🔵 UHD 630       |   0.102  |   0.395  |   0.722  |  0.015  |  0.135  |  0.782  |  0.136  |
| 🔵 UHD 770       |    ---   |   0.688  |   1.287  |  0.060  |  0.251  |  2.821  |  0.511  |
| 🟢 Quadro M1000M |   0.035  |   0.734  |   ---    |  0.192  |  0.308  |  1.071  |  1.087  |
| ⚪ M1 GPU 8CU    |    ---   |   0.620  |   ---    |  0.439  |  0.603  |  0.645  |  0.638  |
| 🟢 GTX 960       |   0.086  |   2.597  |   ---    |  0.551  |  0.918  |  2.649  |  2.652  |
| 🔴 RX 470        |   0.306  |   1.218  |   4.749  |  0.686  |  0.985  |  1.920  |  1.914  |
| 🔴 RX 6600       |   0.570  |   8.324  |  16.641  |  0.466  |  1.845  |  7.498  |  5.564  |
| 🟢 T4            |   0.250  |   8.092  |   ---    |  1.939  |  6.326  |  5.257  |  5.279  |
| 🟢 RTX 3060 Ti   |   0.287  |  17.748  |  18.291  |  2.799  |  9.228  |  8.062  |  6.844  |
| 🟢 RTX 3070 Ti   |   0.368  |  22.572  |  23.276  |  3.049  | 11.721  | 10.198  |  8.681  |

Specification:

| Device           | OpenCL | CU | Freq. | Cores | TFLOPs/s | Memory |  PCIe |
|------------------|:------:|---:|------:|------:|---------:|-------:|------:|
| units            | version | # |   MHz |   # | theorerical | GB/s  |  GB/s |
| i5 3320M         |   1.2  |  4 |  2600 |     2 |    0.166 |  27.65 |  6.93 |
| E3-1226 v3       |   1.2  |  4 |  3300 |     2 |    0.211 |  22.11 |  8.73 |
| 🔵 HD Gen 11     |   1.2  | 16 |   750 |   128 |    0.192 |  16.13 |  6.26 |
| 🔵 UHD 620       |   3.0  | 24 |  1100 |   192 |    0.422 |  14.47 |  6.28 |
| 🔵 UHD 630       |   3.0  | 24 |  1100 |   192 |    0.422 |  29.89 | 15.30 |
| 🔵 UHD 770       |   3.0  | 32 |  1600 |   256 |    0.819 |  22.85 | 11.08 |
| 🟢 Quadro M1000M |   1.2  |  2 |  1071 |   512 |    1.097 |  71.74 |  6.35 |
| ⚪ M1 GPU 8CU    |   1.2  |  8 |  1000 |  1024 |    2.048 |  65.54 | 18.28 |
| 🟢 GTX 960       |        |  8 |  1266 |  1024 |    2.593 |  97.41 |  6.91 |
| 🔴 RX 470        |   2.0  | 32 |  1226 |  2048 |    5.022 | 193.25 |  4.63 |
| 🔴 RX 6600       |        | 16 |  2044 |  1792 |    7.326 | 204.61 |  4.57 |
| 🟢 T4            |   1.2  | 40 |  1590 |  2560 |    8.141 | 245.42 |  4.74 |
| 🟢 RTX 3060 Ti   |   1.2  | 38 |  1665 |  4864 |   16.197 | 423.68 |  9.83 |
| 🟢 RTX 3070 Ti   |   1.2  | 48 |  1770 |  6144 |   21.750 | 574.81 |  8.76 |

I need more time to find software and do the measurements, but I was inpired by the comparison of the graphics performance of my PS4 Pro to other consoles in 2020. Above results are taken early 2024.

## FP32 single

The performance of GPUs in the 2010 and 2020 years is optimized for FP32 single precision. Therefore the computing power in GFLOPS is often indicated for this size. FP64 or double precision is significantly slower. That is the size supercomputer in the 1970 to 1990 were measured in for scientifc calculations.

With the boom of AI and transformer models in machine learning edge computing is done in INT8 which is significantly easier to implement and more power efficient. NPUs since 2015 in smartphones use this metric for their speed. Since 2024 Microsoft calls PCs with at least 40 TOPS an AI PC to better support Copilot.

This is an old list of mine where I just collected data, but not measured:

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
- [XBox Series X](https://en.wikipedia.org/wiki/Xbox_Series_X_and_Series_S) 

In many cases it can be simple calculated by the CPU architecture and the frequency. For example my dual [Xeon X5550](https://ark.intel.com/content/www/us/en/ark/products/37106/intel-xeon-processor-x5550-8m-cache-2-66-ghz-6-40-gt-s-intel-qpi.html) with 2.67 GHz has a [multiplier of 8](https://en.wikipedia.org/wiki/FLOPS) (Nehalem EP) which results in 2.67 x 8 = 21.36 gflops.

## FP64 double

- RX 470 	237 GFLOPS

The old value for supercomputers. Refinement follows. And OpenCL might not be the best option. For example the T4 scores 5.2 TOPS in INT8 with OpenCL, but is actually capable of [130 TOPS with the 320 Turing Tensor cores](https://www.pny.com/en-eu/nvidia-t4).
