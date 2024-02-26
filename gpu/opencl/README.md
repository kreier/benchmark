# GPU performance in TFLOPS and TIOPs

This test is taken from https://github.com/ProjectPhysX/OpenCL-Benchmark 

| Device           | FP64<br>double | FP32<br>single | FP16<br>half | INT64<br>long | INT32<br>int | INT16<br>short | INT8<br>char |
|------------------|:--------:|---------:|---------:|:-------:|:-------:|:-------:|:-------:|
| units            | TFLOPs/s | TFLOPs/s | TFLOPs/s | TIOPs/s | TIOPs/s | TIOPs/s | TIOPs/s |
| 🔵 UHD 620       |   0.097  |   0.365  |   0.659  |  0.013  |  0.115  |  0.642  |  0.129  |
| 🔵 UHD 630       |   0.100  |   0.393  |   0.722  |  0.015  |  0.134  |  0.779  |  0.135  |
| 🟢 Quadro M1000M |   0.035  |   0.734  |   ---    |  0.192  |  0.308  |  1.071  |  1.087  |
| ⚪ M1 GPU 8CU    |    ---   |   0.620  |   ---    |  0.439  |  0.603  |  0.645  |  0.638  |
| 🟢 GTX 960       |   0.086  |   2.597  |   ---    |  0.551  |  0.918  |  2.649  |  2.652  |
| 🔴 RX 470        |   0.306  |   1.218  |   4.749  |  0.686  |  0.985  |  1.920  |  1.914  |
| 🔴 RX 6600       |   0.570  |   8.324  |  16.641  |  0.466  |  1.845  |  7.498  |  5.564  |
| 🟢 RTX 3070 Ti   |   0.366  |  22.572  |   ---    |  3.049  | 11.502  |  9.993  |  8.681  |

Specification:

| Device           | OpenCL | CU | Freq. | Cores | TFLOPs/s | Memory |  PCIe |
|------------------|:------:|---:|------:|------:|---------:|-------:|------:|
| units            | version | # |   MHz |   # | theorerical | GB/s  |  GB/s |
| 🔵 UHD 620       |   1.2  | 24 |  1100 |   192 |    0.422 |  14.47 |  6.28 |
| 🔵 UHD 630       |        | 24 |  1100 |   192 |    0.422 |  28.31 | 14.12 |
| 🟢 Quadro M1000M |        |  2 |  1071 |   512 |    1.097 |  71.74 |  3.96 |
| ⚪ M1 GPU 8CU    |   1.2  |  8 |  1000 |  1024 |    2.048 |  65.54 | 18.28 |
| 🟢 GTX 960       |        |  8 |  1266 |  1024 |    2.593 |  97.41 |  6.91 |
| 🔴 RX 470        |        | 32 |  1226 |  2048 |    5.022 | 193.25 |  4.63 |
| 🔴 RX 6600       |        | 16 |  2044 |  1792 |    7.326 | 204.61 |  4.57 |
| 🟢 RTX 3070 Ti   |        | 48 |  1770 |  6144 |   21.750 | 574.81 |  8.76 |

I need more time to find software and do the measurements, but I was inpired by the comparison of the graphics performance of my PS4 Pro to other consoles in 2020. Above results are taken early 2024.

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
