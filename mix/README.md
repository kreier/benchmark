# Mix of small benchmark sniplets

Every now and then there is a small test to estimate and compare speed. I started writing software like this in the early 90s using the Omicron Basic interpreter for my Atari ST 520STFM to calculate the prime numbers until 10000.

After upgrading my RAM to 1000 kByte with soldered sockets in early 1992 I was able to load compiler, linker and merger of Lattice C into the RAM of my computer. It was now much faster to write a program in C and test it out. To my disappointment the calculation of prime numbers was significantly slower that with the basic interpreter. My motivation to learn C diminished. It was not until October 2000 that I started to write programs in C (or now C++ for OO) again.

Starting 2015 I had to write C again for Arduino. My first Python program was written 2018 and sure enough it calculated prime numbers. 2019 I used this method to determine the speed of microcontrollers like Arduino Uno, ESP8266 or ESP32 in C and MicroPython.

Early 2020 I started with 32bit Microcontrollers like the bluepill STM32F103C8T6. And others had already done a speed comparison of these embedded controllers. Like [Fernando Koyanagi](https://www.instructables.com/member/Fernando+Koyanagi/) ([fernandok.com/](https://www.fernandok.com/)) from Brazil in his article on [instructables](https://www.instructables.com/id/SpeedTest-Arduinos-ESP32-8266s-STM32/). His excel data table exists only as a picture:

![Speed comparison microcontroller](speed_comparison.jpg)
