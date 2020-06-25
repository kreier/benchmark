# CoreMark

The initial code was developed in 2009 by [EEMBC](https://github.com/eembc/coremark). Since 2018 it is additionally licenced with the Apache licence.

In 2019 [Paul Stoffregen](https://github.com/PaulStoffregen) from [PJRC](https://www.pjrc.com/) with the [Teensy project](https://www.pjrc.com/teensy/) ported it to Arduino. It runs out of the box on an ESP32. Multicore optimisation is not enabled yet.

Some of my results:

| Board                  | CoreMark |
| ---------------------- | :------: |
| T-Koala ESP32          |      351 |
| Xeon X5550             |    13643 |
| Xeon X5550 16 threads  |   124634 |

It does not run on ESP8266 yet. Same for bluepill STM32F103 and blackpill STM32F411.
