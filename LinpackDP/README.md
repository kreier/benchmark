# Linpack benchmark in DP (double precision, 64bit)

When the initial linpack was released in 1979 minicomputers like the [PDP-11](https://en.wikipedia.org/wiki/PDP-11) (from 1970) had just moved from 16bit to 32bit with superminicomputers like the [VAX-11](https://en.wikipedia.org/wiki/VAX-11) (1978). The supercomputer [Cray-1](https://en.wikipedia.org/wiki/Cray-1) uses 64bit for data since 1975. By the time the [TOP500](https://en.wikipedia.org/wiki/TOP500) of fastest supercomputers was created in 1993 most supercomputers were using 64bit. For comparison this value is been used ever since.

64bit for normal citizens took a little longer. In 2003 AMD starts shipping the [Athlon 64](https://en.wikipedia.org/wiki/Athlon_64) processor lines with the first x86-based 64-bit processor architecture. For smartphones to move to 64bit it took until 2013 with the [iPhone 5S](https://en.wikipedia.org/wiki/IPhone_5s).

## Test with the Phoronix Test Suite

It can be installed in WSL or Ubuntu with:

``` sh
m@x:~/$ git clone https://github.com/phoronix-test-suite/phoronix-test-suite.git
m@x:~/$ ./phoronix-test-suite/install-sh pts
m@x:~/$ sudo apt install php-cli php-xml
m@x:~/$ 
m@x:~/$ 
```

## Speed comparison results

|     CPU    |  MHz  |      FLOPS       |
| ---------- | ----: | ---------------: |
| ATmega328P |    16 |           94,300 |
|  i7-6820HQ | 3,600 |   99,997,800,000 |
|   i3-10100 | 4,038 |  132,278,500,000 |

Downloaded from [https://www.techpowerup.com/download/linpack-xtreme/](https://www.techpowerup.com/download/linpack-xtreme/).

## List from 2017

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

Read more in [this article - paper ICIST 2017](paper_ICIST_2017.pdf).


## HPL by Intel

The multithread version to measure the performance of supercomputers there is the High Performance Linpack:

- [https://www.netlib.org/benchmark/hpl/](https://www.netlib.org/benchmark/hpl/)

But you can't just download it and make/compile the benchmark and run it. You need MPI, BLAS and VSIPL. A simple solution is to download the compiled binaries from Intel

- [https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-benchmarks-suite.html](https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-benchmarks-suite.html)

For my i7-6820HQ it reached a maximum of 99.9978 GFlops for a size of 27000. That's $10^{11}$.
