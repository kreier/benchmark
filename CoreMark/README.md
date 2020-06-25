# CoreMark

The initial code was developed in 2009 by [EEMBC](https://github.com/eembc/coremark). Since 2018 it is additionally licenced with the Apache licence.

In 2019 [Paul Stoffregen](https://github.com/PaulStoffregen) from [PJRC](https://www.pjrc.com/) with the [Teensy project](https://www.pjrc.com/teensy/) ported it to Arduino. It runs out of the box on an ESP32. Multicore optimisation is not enabled yet.

Some of my results:

| Board                  | CoreMark |
| ---------------------- | :------: |
| STM32F103C8T6 128k     |       81 |
| STM32F401CCU6 256k     |       -- |
| STM32F411CEU6 512k     |      172 |
| T-Koala ESP32          |      351 |
| Xeon X5550             |    13643 |
| Xeon X5550 16 threads  |   124634 |

It does not run on ESP8266 yet. 

Bluepill STM32F103C8T6 only with ST-Link V2 programmer.
Blackpill STM32F401CCU6 not yet working over USB.
Blackpill STM32F411CEU6 with UART generic "Seiral" and Upload CubeProgrammer SWD.
