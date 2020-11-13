# Linpack DP

Results for Linpack DP (double precision)

| Platform        | CPU        | MFlops | MHz  |
|-----------------|------------|--------|------|
| Arduino Uno R3  | ATmega328P | 0.0943 | 16   |
| Node MCU 1.0    | ESP8266    | 1.207  | 80   |
| Node MCU32      | ESP32s     | 2.805  | 160  |
| NUCLEO F746ZG   | STM32F746Z | 3.588  | 216  |
| Raspberry Pi 1B | BCM2835    | 42     | 700  |
| Raspberry Pi 2  | BCM2836    | 170.92 | 900  |
| Raspberry Pi 3  | BCM2837    | 180.14 | 1200 |

Read more in [this article (paper ICIST 2017)](paper_ICIST_2017.pdf)

## HPL by Intel

The multithread version to measure the performance of supercomputers there is the High Performance Linpack:

- https://www.netlib.org/benchmark/hpl/

But you can't just download it and make/compile the benchmark and run it. You need MPI, BLAS and VSIPL. A simple solution is to download the compiled binaries from Intel

- https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-benchmarks-suite.html

For my i7-6820HQ it reached a maximum of 99.9978 GFlops for a size of 27000.
