# Whetstone

copied from https://os.mbed.com/users/kirchnet/code/Nucleo_vs_Arduino_Speed_Test//file/466dbb9d16a8/arduino.txt/

Had to adjust T1 and T2 to t1 and t2 since the otheres are used by the ESP32 library.

### Results:

- Arduino Leonardo: 8.00 MIPS
- Arduino Uno:  8.01 MIPS - should be only 1.21 MIPS ...
- Mega 2560:    7.92 MIPS
- ESP8266: does not run
- ESP32:       14.94 MIPS

## Whetstone 1.2

Copied from https://raw.githubusercontent.com/ghalfacree/Arduino-Sketches/master/Whetstone/Whetstone.ino

- Arduino Leonardo:   7.96 MIPS
- Arduino Uno:        8.01 MIPS
- Arduino Mega 2560:  7.92 MIPS
- Wemos Lolin ESP32: 70.62 MIPS


### Original:

http://www.netlib.org/benchmark/

### Ubuntu

```
mkdir whetstone
cd whetstone
wget http://www.netlib.org/benchmark/whetstone.c
gcc whetstone.c -o whet -lm
whet -c 100000
```

### Roy Longbottom

```
mkdir whetstone
cd whetstone
wget http://www.roylongbottom.org.uk/whets.c
gcc -DUNIX whets.c -o whets -lm
whet
```

Calibrates itself, more output data. See [this documentation](http://www.roylongbottom.org.uk/whetstone%20results.htm). I got up to 680 MFLOPS and 2292 MWIPS.

### ESP IDF

on my to do list
