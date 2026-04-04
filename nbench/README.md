# NBench

This is just a copy of the port Uwe F. Mayer did in November 1997, based on the Bytemark benchmark from October 1995. Version 2.2.3. With some optimizations the performance can be greatly increased.

## Installation

It is usually only 3 steps to get a result:

- Download the nbench.tar.gz and unpack the file
- Compile the benchmark with `make` (you have __make__ and __gcc__ installed)
- Run the benchmark

It will look like:

``` sh
mk@mbp:~ $ wget kreier.org/docs/nbench.tar.gz
mk@mbp:~ $ tar xf nbench.tar.gz
mk@mbp:~ $ cd nbench-byte-2.2.3
mk@mbp:~/nbench-byte-2.2.3 $ make
mk@mbp:~/nbench-byte-2.2.3 $ ./nbench
``` 

## Error messages under macOS - and fix

If you try to run the 5 steps under macOS the `make` command will throw the error `ld: library not found for -lcrt0.o` since static linking is not supported in macOS. Edit the file [Makefile](https://github.com/kreier/benchmark/blob/main/nbench/nbench-byte-2.2.3/Makefile) in the nbench folder with `nano Makefile`. Go down to line 25 and remove `-s --static`. Save with `Ctrl+O` and exit with `Ctrl+X`. 

The new error is now from sysspec.c that 'malloc.h' is not found. This is because a condition in [sysspec.h](https://github.com/kreier/benchmark/blob/main/nbench/nbench-byte-2.2.3/sysspec.h) from line36 to 38 is wrong interpreted. Just comment these three lines with some `//` in front of them. After that the `make` compiles the working nbench program.

## Data collection 2005 - 2026:

Sorted by Integer index (in reference to K6/233) since its most relevant to user experience. The Pentium 90 is really old 😊

|       __Device__      |       __CPU__       | MHz | Memory Index | __Integer Index__ | FP Index |  INT  | FLOAT | SuperPI 1M |__Test Date__|      ISA |
|:---------------------:|:----------------------:|-----:|-------------:|--------------:|---------:|------:|------:|-----------:|-----------:|----------:|
| Samsung Galaxy 3      | [Eclair 2.1] S5P6422   |  667 |        0.541 |         0.959 |    0.126 |   3.0 |   0.2 |          - | 2011-12-15 |     ARMv6 |
| Vobis PC              | Pentium II             |  233 |        1.238 |         1.330 |    2.409 |   5.1 |   4.3 |    8m16.4s | 2012-08-01 |     IA-32 |
| Huawei Ideos X3       | [Ideos X3 - 2.3] ARMv6 |  600 |        1.040 |         1.685 |    0.228 |   5.5 |   0.4 |          - | 2013-08-01 |     ARMv6 |
| TL-WR1043ND           | Atheros AR9132         |  400 |        1.379 |         1.712 |    0.035 |   6.3 |   0.1 |          - | 2013-08-03 |  MIPS 24K |
| Samsung GT-i5800      | [Froyo 2.2] ARMv6      |  667 |        1.024 |         1.821 |    0.238 |   5.7 |   0.4 |          - | 2012-08-01 |     ARMv6 |
| Raspberry Pi 1B       | BCM2835                |  700 |        2.456 |         3.106 |    2.029 |  11.3 |   3.7 |          - | 2014-08-10 |    ARMv6Z |
| Sony Tipo 4.0.4       | MSM7225A Cortex-A5     |  800 |        2.748 |         3.282 |    3.711 |  12.8 |   6.7 |          - | 2014-08-10 |   ARMv7-A |
| Thinkpad X30          | Pentium III            |  933 |        4.709 |         5.164 |    8.916 |  19.9 |  16.1 |    4m01.7s | 2014-08-10 |     IA-32 |
| Huawei Y300 4.1.1     | MSM8225 S4 Cortex-A5   | 1008 |        3.665 |         5.460 |    4.685 |  18.4 |   8.5 |          - | 2014-08-10 |   ARMv7-A |
| Raspberry Pi 2        | BCM2836                | 1000 |        4.665 |         6.481 |    5.059 |  22.6 |   9.1 |          - | 2014-08-10 |   ARMv7-A |
| Umi Fair              | MT6735                 |  988 |        5.799 |         6.717 |    8.055 |  25.3 |  14.5 |          - | 2015-08-01 |   ARMv8-A |
| Thinkpad X40          | Pentium M              | 1200 |        6.210 |         7.047 |   12.384 |  26.4 |  22.0 |    1m14.4s | 2014-06-07 |     IA-32 |
| Samsung N150          | Atom N450              | 1666 |        7.243 |         7.109 |    7.351 |  28.6 |  12.8 |    1m37.6s | 2010-04-01 |    x86-64 |
| Marc old PC           | Pentium 4              | 2000 |        9.394 |         7.529 |   13.164 |  33.2 |  23.7 |    1m34.2s | 2009-07-23 |     IA-32 |
| Toshiba NB100         | Atom N270              | 1600 |        7.752 |         7.579 |    7.068 |  30.6 |  12.8 |    1m37.6s | 2009-08-01 |     IA-32 |
| HP Mini 1100          | Atom N455              | 1666 |        9.386 |         8.390 |    7.313 |  35.3 |  13.2 |    1m30.9s | 2013-08-10 |    x86-64 |
| Raspberry Pi 3        | BCM2837 B0             | 1200 |        6.780 |         9.524 |    9.174 |  33.0 |  16.5 |          - | 2024-01-07 |   ARMv8-A |
| Nexus 4               | S4 Pro Krait APQ8064   | 1512 |        4.591 |         9.895 |    9.086 |  28.5 |  16.4 |          - | 2015-01-27 |   ARMv7-A |
| Tanix TX3 mini        | Amlogic S905W          | 1200 |        8.680 |        10.948 |   10.155 |  39.7 |  18.3 |          - | 2024-01-28 |   ARMv8-A |
| Silentium II          | Athlon64               | 1800 |       11.269 |        11.927 |   20.517 |  46.6 |  37.0 |    49.100s | 2011-05-09 |    x86-64 |
| Samsung R20 russisch  | Core Duo T2450         | 2000 |       12.138 |        12.568 |   21.144 |  49.6 |  38.1 |    33.800s | 2009-04-16 |     IA-32 |
| Medion Akoya P2212T   | Intel N2920            | 1860 |       18.433 |        15.150 |   16.636 |  66.0 |  30.0 |    42.056s | 2014-05-29 |    x86-64 |
| Jetson Nano A02 4GB   | Tegra X1               | 1400 |       14.399 |        15.947 |   17.788 |  61.2 |  32.1 |            | 2025-04-25 |   ARMv8-A |
| Silentium II          | 64bit Athlon64         | 1800 |       13.595 |        16.121 |   19.566 |  59.9 |  35.3 |    49.400s | 2011-05-09 |    x86-64 |
| Medion Akoya E1232T   | Intel N2807            | 1580 |       19.981 |        16.207 |   18.001 |  71.0 |  32.5 |    43.033s | 2014-07-31 |    x86-64 |
| MacBook Air 2013      | Intel i5-4250U         | 1299 |       19.051 |        17.286 |   25.289 |  72.2 |  45.6 |          - | 2014-08-10 |    x86-64 |
| Medion PC 2013        | Intel Core i3          | 2527 |       28.488 |        17.781 |   36.673 |  87.2 |  66.1 |    17.437s | 2013-07-02 |    x86-64 |
| Synology DS216+II     | Intel N3060            | 1600 |       23.695 |        17.817 |   25.516 |  80.7 |  46.0 |    50.264s | 2020-09-15 |    x86-64 |
| Acer C720             | Celeron 2955U          | 1400 |       18.776 |        17.878 |   29.106 |  73.2 |  52.5 |          - | 2019-06-25 |    x86-64 |
| Raspberry Pi 4        | BCM2711                | 1500 |       15.319 |        18.061 |   34.620 |  67.4 |  62.4 |          - | 2024-09-26 |   ARMv8-A |
| Medion 2010           | AthlonII X4            | 2607 |       18.265 |        18.958 |   31.843 |  74.8 |  57.4 |    30.700s | 2012-08-30 |    x86-64 |
| Mark old PC 2         | Sempron SI-42          | 2100 |       14.395 |        19.299 |   23.132 |  68.2 |  41.7 |   1m0.573s | 2009-09-04 |    x86-64 |
| Thinkpad X200         | Intel Core2 Duo P8400  | 2266 |       28.631 |        19.781 |   31.141 |  92.9 |  56.1 |    22.112s | 2016-12-09 |    x86-64 |
| Galaxy Note 8         | Exynos 8895            | 2400 |       23.448 |        32.408 |   50.742 | 113.1 |  91.5 |          - | 2026-04-04 |   ARMv8-A |
| Thinkpad T61          | Intel Core2 Duo T7300  | 2043 |       19.359 |        19.808 |   33.182 |  78.6 |  59.8 |    25.700s | 2014-10-07 |    x86-64 |
| Fujitsu Celsius W360  | Intel Core2 Duo E8300  | 2832 |       33.671 |        23.584 |   36.384 | 110.1 |  65.6 |    18.473s | 2016-03-14 |    x86-64 |
| Project IDEAcenter    | Intel Pentium E6600    | 3066 |       28.776 |        23.881 |   47.396 | 103.7 |  85.5 |    18.923s | 2022-05-10 |    x86-64 |
| Kramers PC            | Intel Core i3 550      | 3200 |       37.846 |        23.882 |   47.437 | 116.6 |  85.5 |          - | 2013-09-20 |    x86-64 |
| Timmy PC              | Intel Core i7 870S     | 2667 |       24.206 |        24.602 |   41.085 |     - |     - |    14.700s | 2011-05-20 |    x86-64 |
| Mark PC               | Athlon64 X2            | 2829 |       21.476 |        25.608 |   30.663 |  95.2 |  55.3 |    34.300s | 2009-03-24 |    x86-64 |
| HP Z600               | Xeon X5550             | 2667 |       27.461 |        26.342 |   27.894 | 107.5 |  86.4 |    14.800s | 2020-05-05 |    x86-64 |
| Eigenbau 5            | AMD Phenom II X4 955   | 3352 |       28.022 |        32.586 |   44.104 | 122.4 |  79.2 |    16.300s | 2015-11-07 |    x86-64 |
| MacBookAir            | i5 4250U               | 2300 |       39.050 |        33.215 |   54.260 | 142.7 |  97.8 |          - | 2016-01-28 |    x86-64 |
| Elitebook hp8460p     | i5 2520M               | 2500 |       40.699 |        37.018 |   52.635 | 154.5 |  94.9 |    13.145s | 2016-01-28 |    x86-64 |
| Thinkpad X230         | i5 3320M               | 2600 |       45.382 |        40.313 |   61.804 | 169.9 | 111.4 |    12.264s | 2017-03-23 |    x86-64 |
| zBook 15 G3           | i7 6820HQ              | 2700 |       57.200 |        43.732 |  107.954 | 196.6 | 194.6 |    10.712s | 2020-11-20 |    x86-64 |
| MacBookPro15 2013     | i7 4960HQ              | 2600 |       55.046 |        44.618 |   73.570 | 195.6 | 132.6 |   10.164s  | 2018-09-12 |    x86-64 |
| Asus ROG GL552VW      | Intel Core i7 6700HQ   | 2600 |       63.682 |        45.732 |   68.159 | 211.2 | 122.9 |      -     | 2018-02-15 |    x86-64 |
| Acer Aspire V15 Nitro | Intel Core i7 4710HQ   | 2500 |       50.423 |        46.117 |   70.039 | 192.0 | 126.3 |      -     | 2018-02-15 |    x86-64 |
| HP mini 800 G4        | i5 8500T               | 2112 |       61.249 |        46.227 |  113.619 | 209.0 | 204.9 |   10.900s  | 2024-01-07 |    x86-64 |
| Eigenbau 6 AI CUDA    | i3-6100                | 3700 |       68.150 |        48.103 |  118.447 | 223.8 | 216.6 |            | 2025-04-26 |    x86-64 |
| Eigenbau 7 AI CUDA    | Xeon 2696 v3           | 2295 |       59.666 |        49.441 |  116.922 | 214.8 | 210.8 |   11.801s  | 2024-01-07 |    x86-64 |
| Proxmox 1226          | E3-1226 v3             | 3700 |       62.206 |        49.951 |  112.593 | 219.9 | 203.0 |   10.044s  | 2024-09-26 |    x86-64 |
| Xigmatec Gemini       | i3 10100               | 4160 |       77.174 |        56.761 |  138.003 | 259.5 | 248.8 |   08.748s  | 2023-10-12 |    x86-64 |
| Galaxy Note 20        | Snapdragon 865         | 3090 |       63.435 |        66.735 |  143.465 | 261.7 | 258.7 |            | 2026-04-04 | ARMv8.2-A |
| MacBook Air 2020      | M1                     | 3200 |       66.939 |        79.733 |  216.304 | 296.4 | 389.9 |      -     | 2024-09-26 | ARMv8.5-A |
| HP mini 400 G9        | i7 13700T              | 4700 |      104.525 |        85.010 |  264.869 | 372.2 | 377.5 |   06.917s  | 2024-09-26 |    x86-64 |
| Galaxy Note 20        | Exynos 2400            | 3210 |       83.274 |        86.000 |  163.313 | 339.9 | 296.2 |      -     | 2026-04-04 | ARMv9.2-A |
|       __Device__      |       __CPU__       | MHz | Memory Index | __Integer Index__ | FP Index |  INT  | FLOAT | SuperPI 1M |__Test Date__|      ISA |

## Old list from 2020:

|CPU                                                                |Memory index|Integer index|Floating Point index|INTEGER|FLOAT|SuperPI 1M|
|-------------------------------------------------------------------|------------|-------------|--------------------|-------|-----|----------|
|[Eclair 2.1] S5P6422 @ 667 MHz                                     |0.541       |0.959        |0.126               |3      |0.2  |-         |
|Pentium II @ 233 MHz                                               |1.238       |1.33         |2.409               |5.1    |4.3  |8m16.4s   |
|[Ideos X3 - 2.3] ARMv6 @ 600 MHz                                   |1.04        |1.685        |0.228               |5.5    |0.4  |-         |
|TL-WR1043ND Atheros AR9132 @ 400 MHz                               |1.379       |1.712        |0.035               |6.3    |0.06 |-         |
|[Froyo 2.2] ARMv6 @ 667 MHz                                        |1.024       |1.821        |0.238               |5.7    |0.4  |-         |
|[Raspberry Pi] BCM2835 @ 700 MHz                                   |2.456       |3.106        |2.029               |11.3   |3.66 |-         |
|[Tipo ICS 4.0.4] ARMv7 @ 800 MHz Qualcomm MSM7225A Cortex-A5       |2.748       |3.282        |3.711               |12.8   |6.69 |-         |
|Pentium III @ 933 MHz                                              |4.709       |5.164        |8.916               |19.9   |16.1 |4m01.7s   |
|[Y300 JB 4.1.1] Dual ARMv7 @ 1008 MHz Qualcomm MSM8225 S4 Cortex-A5|3.665       |5.46         |4.685               |18.4   |8.45 |-         |
|[Raspberry Pi2] BCM2836 @ 1000 MHz                                 |4.665       |6.481        |5.059               |22.6   |9.1  |-         |
|[Umi Fair] MT6735 @ 988 MHz                                        |5.799       |6.717        |8.055               |25.3   |14.5 |-         |
|Pentium M @ 1200 MHz                                               |6.21        |7.047        |12.384              |26.4   |22   |1m14.4s   |
|Atom N450 @ 1666 MHz                                               |7.243       |7.109        |7.351               |28.6   |12.8 |1m37.6s   |
|Pentium 4 @ 2000 MHz                                               |9.394       |7.529        |13.164              |33.2   |23.7 |1m34.2s   |
|Atom N270 @ 1600 MHz                                               |7.752       |7.579        |7.068               |30.6   |12.8 |1m37.6s   |
|Atom N455 @ 1666 MHz                                               |9.386       |8.39         |7.313               |35.3   |13.2 |1m30.9s   |
|[Nexus 4 ICS 4.3] 4 ARMv7 @ 1512 MHz Qualcomm S4 Pro Krait APQ8064 |4.591       |9.895        |9.086               |28.5   |16.4 |-         |
|Athlon64 @ 1800 MHz                                                |11.269      |11.927       |20.517              |46.6   |37   |0m49.1s   |
|Core Duo T2450 @ 2000 MHz                                          |12.138      |12.568       |21.144              |49.6   |38.1 |0m33.8s   |
|DS216+II Intel N3060 @ 1600 MHz VM Windows 10 with Ubuntu WSL 2004 |10.021      |13.140       |23.395              |46.883 |42.2 |0m50.3s   |
|Intel N2920 @ 1860 MHz                                             |18.433      |15.15        |16.636              |66     |30   |0m42.1s   |
|64bit Athlon64 @ 1800 MHz                                          |13.595      |16.121       |19.566              |59.9   |35.3 |0m49.4s   |
|Intel N2807 @ 1580 MHz                                             |19.981      |16.207       |18.001              |71     |32.5 |0m43.0s   |
|MacBookAir Intel i5-4250U @ 1299 MHz                               |19.051      |17.286       |25.289              |72.2   |45.6 |-         |
|Intel Core i3 @ 2527 MHz                                           |28.488      |17.781       |36.673              |87.2   |66.1 |0m17.4s   |
|DS216+II Intel N3060 @ 1600 MHz                                    |23.695      |17.817       |25.516              |80.7   |46   |-         |
|Acer C720 Celeron 2955U @ 1400 MHz                                 |18.776      |17.878       |29.106              |73.2   |52.5 |-         |
|AthlonII X4 @ 2607 MHz                                             |18.265      |18.958       |31.843              |74.8   |57.4 |0m30.7s   |
|Sempron SI-42 @ 2100 MHz                                           |14.395      |19.299       |23.132              |68.2   |41.7 |1m00.6s   |
|Intel Core2 Duo P8400 @ 2266 MHz                                   |28.631      |19.781       |31.141              |92.9   |56.1 |0m22.1s   |
|Intel Core2 Duo @ 2043 MHz                                         |19.359      |19.808       |33.182              |78.6   |59.8 |0m25.7s   |
|Intel Core2 Duo E8300 @ 2832 MHz                                   |33.671      |23.584       |36.384              |110.1  |65.6 |0m18.5s   |
|Intel Core i3 550 @ 3200 MHz                                       |37.846      |23.882       |47.437              |116.6  |85.5 |-         |
|Intel Core i7 870S @ 2667 MHz                                      |24.206      |24.602       |41.085              |-      |-    |0m14.7s   |
|Athlon64 X2 @ 2829 MHz                                             |21.476      |25.608       |30.663              |95.2   |55.3 |0m34.3s   |
|AMD Phenom II X4 955 @ 3352 MHz                                    |25.034      |32.851       |40.967              |117.2  |73.9 |0m16.3s   |
|PhenomII 955 optimized @ 3352 MHz                                  |28.022      |32.586       |44.104              |122.4  |79.2 |0m16.3s   |
|MacBookAir i5 4250U @ 2300 MHz                                     |39.05       |33.215       |54.26               |142.7  |97.8 |-         |
|hp 8460p i5 2520M @ 2500 MHz                                       |40.699      |37.018       |52.635              |154.5  |94.9 |0m13.1s   |
|Lenovo X230 i5 3320M @ 2600 MHz                                    |45.382      |40.313       |61.804              |169.9  |111.4|0m12.3s   |
|Lenovo Yoga 370 i5 7300U @ 2600 MHz                                |55.043      |41.173       |105.528             |186.8  |190.3|0m11.6s   |
|HP ZBook 15 G3 i7 6820HQ @ 2700 MHz                                |57.200      |43.732       |107.954             |196.6  |194.6|0m10.7s   |
|MacBookPro15 i7 4960HQ @ 2600 MHz                                  |55.046      |44.618       |73.57               |195.6  |132.6|0m10.2s   |
|Intel Core i7 6700HQ @ 2600 MHz                                    |63.682      |45.732       |68.159              |211.2  |122.9|-         |
|Intel Core i7 4710HQ @ 2500 MHz                                    |50.423      |46.117       |70.039              |192    |126.3|-         |
|__CPU__                                    |__Memory index__|__Integer index__|__Floating Point index__|__INTEGER__|__FLOAT__|__SuperPI 1M__|

## Fix to run on a router with OpenWRT

First download the toolchain from [downloads.openwrt.org/releases/25.12.2/targets/ath79/generic/](https://downloads.openwrt.org/releases/25.12.2/targets/ath79/generic/) (at the very bottom):

``` sh
apt install build-essential libncurses-dev zlib1g-dev gawk git gettext libssl-dev xsltproc rsync wget unzip python3 zstd
wget https://downloads.openwrt.org/releases/25.12.2/targets/ath79/generic/openwrt-sdk-25.12.2-ath79-generic_gcc-14.3.0_musl.Linux-x86_64.tar.zst
tar xvf openwrt-sdk-25.12.2-ath79-generic_gcc-14.3.0_musl.Linux-x86_64.tar.zst
make defconfig
make toolchain/install
export PATH=~/github/openwrt-sdk-25.12.2-ath79-generic_gcc-14.3.0_musl.Linux-x86_64/staging_dir/toolchain-mips_24kc_gcc-14.3.0_musl/bin:$PATH
export STAGING_DIR=~/github/openwrt-sdk-25.12.2-ath79-generic_gcc-14.3.0_musl.Linux-x86_64/staging_dir
```

Then get nbench

``` sh
wget kreier.org/docs/nbench.tar.gz
tar xf nbench.tar.gz
cd nbench-byte-2.2.3
make
```

This will be stuck at the ASSIGNMENT part (see below). The fix: Change these lines 202 and 203 in `nbench1.h`:

``` h
/*************************
** ASSIGNMENT ALGORITHM **
*************************/

/*
** DEFINES
*/

#define ASSIGNROWS 101L
#define ASSIGNCOLS 101L
```

Reduce these values to 29. Then change the target compiler in the `MakeFile` line 22 from `CC = gcc` to .

``` c
CC = mips-openwrt-linux-musl-gcc
```

And then just run `make`. Copy the `nbench` to your router with `scp -O nbench root@192.168.17.1:/root/`.

## Example output

```sh
$ ./nbench

BYTEmark* Native Mode Benchmark ver. 2 (10/95)
Index-split by Andrew D. Balsa (11/97)
Linux/Unix* port by Uwe F. Mayer (12/96,11/97)

TEST                : Iterations/sec.  : Old Index   : New Index
                    :                  : Pentium 90* : AMD K6/233*
--------------------:------------------:-------------:------------
NUMERIC SORT        :            2531  :      64.91  :      21.32
STRING SORT         :          3192.8  :    1426.62  :     220.82
BITFIELD            :      1.1123e+09  :     190.79  :      39.85
FP EMULATION        :          1302.4  :     624.96  :     144.21
FOURIER             :       3.124e+05  :     355.29  :     199.55
ASSIGNMENT          :           104.2  :     396.51  :     102.84
IDEA                :           23861  :     364.94  :     108.35
HUFFMAN             :           13254  :     367.52  :     117.36
NEURAL NET          :          322.84  :     518.62  :     218.15
LU DECOMPOSITION    :          8783.2  :     455.01  :     328.56
==========================ORIGINAL BYTEMARK RESULTS==========================
INTEGER INDEX       : 345.458
FLOATING-POINT INDEX: 437.650
Baseline (MSDOS*)   : Pentium* 90, 256 KB L2-cache, Watcom* compiler 10.0
==============================LINUX DATA BELOW===============================
CPU                 : 24 CPU GenuineIntel 13th Gen Intel(R) Core(TM) i7-13700T 1382MHz
L2 Cache            : 30720 KB
OS                  : Linux 6.6.75.1-microsoft-standard-WSL2
C compiler          : gcc version 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1)
libc                : /lib/x86_64-linux-gnu/libc.so.6
MEMORY INDEX        : 96.728
INTEGER INDEX       : 79.072
FLOATING-POINT INDEX: 242.742
Baseline (LINUX)    : AMD K6/233*, 512 KB L2-cache, gcc 2.7.2.3, libc-5.4.38
* Trademarks are property of their respective holder.
```
