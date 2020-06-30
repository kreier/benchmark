# Whetstone

copied from https://os.mbed.com/users/kirchnet/code/Nucleo_vs_Arduino_Speed_Test//file/466dbb9d16a8/arduino.txt/

Had to adjust T1 and T2 to t1 and t2 since the otheres are used by the ESP32 library.

Results:

Arduino Uno:  8.01 MIPS - should be only 1.21 MIPS ...
ESP32:       14.94 MIPS

ESP8266 does not run.
Original:

http://www.netlib.org/benchmark/