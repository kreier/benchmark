# CoreMark

The initial code was developed in 2009 by [EEMBC](https://github.com/eembc/coremark). Since 2018 it is additionally licenced with the Apache licence.

In 2019 [Paul Stoffregen](https://github.com/PaulStoffregen) from [PJRC](https://www.pjrc.com/) with the [Teensy project](https://www.pjrc.com/teensy/) ported it to Arduino. It runs out of the box on an ESP32. Multicore optimisation is not enabled yet.

Some of my results:

| Board                  | CoreMark | LED |
| ---------------------- | -------: | :-: |
| STM32F103C8T6 128k     |       81 |  17 |
| STM32F401CCU6 256k     |      150 |  31 |
| STM32F411CEU6 512k     |      172 |  31 |
| T-Koala ESP32          |      351 |   5 |
| Xeon X5550             |    13643 |     |
| Xeon X5550 16 threads  |   124634 |     |

It does not run on ESP8266 yet. 

Bluepill STM32F103C8T6 only with ST-Link V2 programmer.

Blackpill STM32F401CCU6 and STM32F411CEU6 working with:
- Correct board and board part number
- U(S)ART support: "Enabled (generic 'Serial')"
- USB support (if available): "CDC (generic 'Serial' supersede U(S)ART)" to have COM port serial after reboot
- Upload method: "STM32CubeProgrammer (DFU)"

Programming mode activated by press and hold Boot0 and hit NRST. You have a new USB devices "STM32 BOOTLOADER".
