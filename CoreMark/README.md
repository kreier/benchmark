# CoreMark

The initial code was developed in 2009 by [EEMBC](https://github.com/eembc/coremark). Since 2018 it is additionally licenced with the Apache licence.

In 2019 [Paul Stoffregen](https://github.com/PaulStoffregen) from [PJRC](https://www.pjrc.com/) with the [Teensy project](https://www.pjrc.com/teensy/) ported it [to Arduino](https://github.com/PaulStoffregen/CoreMark). It runs out of the box on an ESP32. Multicore optimisation is not enabled yet. In ubuntu it works with

```
make XCFLAGS="-g -DMULTITHREAD=4 -DUSE_FORK=1"
``` 

Some of my results:

| Board                   | CoreMark | LED | MHz  |
| ----------------------- | -------: | :-: | ---: |
| Arduino MEGA 2560       |        7 |  13 |   16 |
| STM32F103C8T6 128k      |       81 |  17 |   72 |
| STM32F401CCU6 256k      |      150 |  31 |   84 |
| STM32F411CEU6 512k      |      172 |  31 |  100 |
| T-Koala ESP32           |      351 |   5 |  160 |
| Raspberry Pi 3 Model B  |     3800 |     | 1200 |
| Amlogic S905W tanix tx3 |     3913 |     | 1200 |
| Xeon X5550              |    13643 |     | 3060 |
| i5-3320M                |    21245 |     | 3300 |

Multithread

| Board                   | CoreMark | MHz  |
| ----------------------- | -------: | ---: |
| RPi3 Model B  4 threads |    15194 | 1200 |
| Amlogic S905W 4 threads |    15393 | 1200 |
| i5-3320M 4 threads      |    53450 | 3300 |
| Xeon X5550 16 threads   |   124634 | 3060 |


Bluepill STM32F103C8T6 only with ST-Link V2 programmer.

Blackpill STM32F401CCU6 and STM32F411CEU6 working with:
- Correct board and board part number
- U(S)ART support: "Enabled (generic 'Serial')"
- USB support (if available): "CDC (generic 'Serial' supersede U(S)ART)" to have COM port serial after reboot
- Upload method: "STM32CubeProgrammer (DFU)"

Programming mode activated by press and hold Boot0 and hit NRST. You have a new USB devices "STM32 BOOTLOADER".

It does not run on ESP8266 yet. Look at solution from [ochrin](https://github.com/ochrin/coremark). He uses the esp8266 toolchain. My results:

| Board            | CoreMark |
| ---------------- | -------: |
| ESP8266  80 MHz  |      155 |
| ESP8266  80 MHz  |      262 |
| ESP32    80 MHz  |          |
| ESP32   240 MHz  |          |

With multicore it was compiled under linux by [ochrin](https://github.com/ochrin/coremark) in March 2020 and he got both ESP8266 running and dualcore results on ESP32. Still no match for the 2200 of the Teensy 4.0. I can't make the ESP32 toolchain running.

