# Dhrystone

This gives you integer performance (DMIPS).

Software from:

https://www.netlib.org/benchmark/dhry-c

A little more modifications done for Dhrystone 2.2

'' sh 
me@z840:~/$ wget https://homepages.cwi.nl/~steven/dry.c
me@z840:~/$ sh dry.c
''

### Results:

Run 13/11/2020 on i7-6820HQ: 32 DMIPS

- Arduino Leonardo: 8.00 MIPS
- Arduino Uno:  8.01 MIPS - should be only 1.21 MIPS ...
- Mega 2560:    7.92 MIPS
- ESP8266: does not run
- ESP32:       14.94 MIPS



### Original:

http://www.netlib.org/benchmark/


