# Linpack DP

Results for Linpack DP (double precision)

| Platform        | CPU/MCU     | Architecture                   | MFlops    | DMIPS     | MHz  | RAM kB  |
| --------------- | ----------- | ------------------------------ | --------- | --------- | ---- | ------- |
| Arduino Uno R3  | ATmega328P  | AVR 8bit RISC                  | 0.0943    | 10        | 16   | 2       |
| Embedded Pi     | STM32F103RB | ARM Cortex-M3 (ARMv7-M) 32bit  | 0.552     | 92        | 72   | 20      |
| Node MCU 1.0    | ESP8266     | Tensilica Xtensa LX106 32bit   | 1.207     | 113       | 80   | 64      |
| Node MCU32      | ESP32s      | Tensilica Xtensa LX106 32bit   | 2.805     | 176       | 160  | 520     |
| NUCLEO F746ZG   | STM32F746Z  | ARM Cortex-M7 (ARMv7E-M) 32bit | 3.588     | 763       | 216  | 320     |
| Raspberry Pi 1B | BCM2835     | ARM1176 (v6) 32bit             | 42        | 875       | 700  | 512000  |
| Raspberry Pi 2  | BCM2836     | ARM Cortex-A7 (v7-A) 32bit     | 170.92    | 2019      | 900  | 1024000 |
| Raspberry Pi 3  | BCM2837     | ARM Cortex-A53 (v8-A) 32bit    | 180.14    | 3039      | 1200 | 1024000 |
|                 |             |                                | LinpackDP | Dhrystone |      |         |

Read more in [this article (paper ICIST 2017)](paper_ICIST_2017.pdf)

## HPL by Intel

The multithread version to measure the performance of supercomputers there is the High Performance Linpack:

- https://www.netlib.org/benchmark/hpl/

But you can't just download it and make/compile the benchmark and run it. You need MPI, BLAS and VSIPL. A simple solution is to download the compiled binaries from Intel

- https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-benchmarks-suite.html

For my i7-6820HQ it reached a maximum of 99.9978 GFlops for a size of 27000.
