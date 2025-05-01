# Linpack benchmark in DP (double precision, 64bit)

When the initial linpack was released in 1979 minicomputers like the [PDP-11](https://en.wikipedia.org/wiki/PDP-11) (from 1970) had just moved from 16bit to 32bit with superminicomputers like the [VAX-11](https://en.wikipedia.org/wiki/VAX-11) (1978). The supercomputer [Cray-1](https://en.wikipedia.org/wiki/Cray-1) uses 64bit for data since 1975. By the time the [TOP500](https://en.wikipedia.org/wiki/TOP500) of fastest supercomputers was created in 1993 most supercomputers were using 64bit. For comparison this value is been used ever since.

64bit for normal citizens took a little longer. In 2003 AMD starts shipping the [Athlon 64](https://en.wikipedia.org/wiki/Athlon_64) processor lines with the first x86-based 64-bit processor architecture. For smartphones to move to 64bit it took until 2013 with the [iPhone 5S](https://en.wikipedia.org/wiki/IPhone_5s).

## Test with the Phoronix Test Suite

<img src="https://kreier.github.io/benchmark/docs/pts_logo.png" align="right" width="12%">

It can be installed in WSL or Ubuntu with:

``` sh
sudo apt install php php-cli php-xml
git clone https://github.com/phoronix-test-suite/phoronix-test-suite/
cd phoronix-test-suite
sudo ./install-sh
phoronix-test-suite benchmark hpl
```

<img src="https://kreier.github.io/benchmark/docs/ob_logo.png" align="right" width="8%">

Some of my results are uploaded to [openbenchmarking.org](https://openbenchmarking.org/user/saiht).

|      Machine      |     CPU    |  MHz |      FLOPS      | Cores |
|:------------------|:----------:|-----:|----------------:|------:|
| Arduino Uno R3    | ATmega328P |   16 |          94,300 |     1 |
| Jetson Nano A02 🟢| Tegra X1   | 1500 |   3,848,500,000 |     4 |
| Elitebook hp8460p 🔵| i5-2520M | 3200 |  37,275,300,000 |     2 |
| hp zBook 15 G3 🔵 | i7-6820HQ  | 3600 |  99,997,800,000 |     4 |
| Xigmatek Gemini 🔵| i3-10100   | 4038 | 132,278,500,000 |     4 |
| hp mini 400 G9 🔵 | i7-13700T  | 1840 | 235,712,000,000 |    16 |
| hp MT 600 G4   🔴 | RX 6600    | 2044 | 570,000,000,000 |  1792 |

<img src="https://kreier.github.io/benchmark/docs/opencl_logo.png" align="right" width="15%">

This number can be measured much faster with **OpenCL**. Some results for CPUs and GPUs are in the [GPU benchmark section](../gpu/opencl/).

In this section I also included a graph for comparison of GFLOPS with DP (fp64) from the fastest supercomputer of their time to consumer hardware a few years later ([source Google Sheet](https://docs.google.com/spreadsheets/d/17QBJVa8wzo4B1aygXrlk0FWpG4UVwWn3Zo5LsfNnlJM/edit?usp=sharing)):

![comparison GFLOPS over years](https://kreier.github.io/benchmark/gpu/GFLOPS_time.png)

Earlier graph:

![updated comparison](../docs/GFLOPS_time1.png)

## Speed comparison results

|     CPU    |  MHz  |      FLOPS       |
| ---------- | ----: | ---------------: |
| ATmega328P |    16 |           94,300 |
|  i7-6820HQ | 3,600 |   99,997,800,000 |
|   i3-10100 | 4,038 |  132,278,500,000 |

Downloaded from [https://www.techpowerup.com/download/linpack-xtreme/](https://www.techpowerup.com/download/linpack-xtreme/).

## List from 2017

| Platform        | CPU/MCU     | Architecture                   | MFlops    | DMIPS     | MHz  | RAM kB  |
| --------------- | ----------- | ------------------------------ | --------- | --------- | ---: | ------: |
| Arduino Uno R3  | ATmega328P  | AVR 8bit RISC                  | 0.0943    | 10        | 16   | 2       |
| Embedded Pi     | STM32F103RB | ARM Cortex-M3 (ARMv7-M) 32bit  | 0.552     | 92        | 72   | 20      |
| Node MCU 1.0    | ESP8266     | Tensilica Xtensa LX106 32bit   | 1.207     | 113       | 80   | 64      |
| Node MCU32      | ESP32s      | Tensilica Xtensa LX106 32bit   | 2.805     | 176       | 160  | 520     |
| NUCLEO F746ZG   | STM32F746Z  | ARM Cortex-M7 (ARMv7E-M) 32bit | 3.588     | 763       | 216  | 320     |
| Raspberry Pi 1B | BCM2835     | ARM1176 (v6) 32bit             | 42        | 875       | 700  | 512000  |
| Raspberry Pi 2  | BCM2836     | ARM Cortex-A7 (v7-A) 32bit     | 170.92    | 2019      | 900  | 1024000 |
| Raspberry Pi 3  | BCM2837     | ARM Cortex-A53 (v8-A) 32bit    | 180.14    | 3039      | 1200 | 1024000 |
|                 |             |                                | LinpackDP | Dhrystone |      |         |

Read more in [this article - paper ICIST 2017](paper_ICIST_2017.pdf).


## HPL by Intel

The multithread version to measure the performance of supercomputers there is the High Performance Linpack:

- [https://www.netlib.org/benchmark/hpl/](https://www.netlib.org/benchmark/hpl/)

But you can't just download it and make/compile the benchmark and run it. You need MPI, BLAS and VSIPL. A simple solution is to download the compiled binaries from Intel

- [https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-benchmarks-suite.html](https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-benchmarks-suite.html)

For my i7-6820HQ it reached a maximum of 99.9978 GFlops for a size of 27000. That's $10^{11}$.
