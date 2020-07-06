# Benchmark collection

There are countless benchmarks out there. This is just a collection of benchmarks I used over the years and the results. Some tests date back to 1972. I measured the speed of a Lattice C compiler against Omicron Basic in 1992 on my Atari ST. Data presented here started in 2007 with Memtest86+ and the website http://saiht.de/computer/benchmark.html .

## [Whetstone](whetstone)

This [synthetic benchmark from 1972](https://en.wikipedia.org/wiki/Whetstone_(benchmark)) is one of the oldest ones to estimate the [FLOPS - floating point operations](https://en.wikipedia.org/wiki/FLOPS) a CPU can perform per second. Well described in an [article of arstechnica](https://arstechnica.com/information-technology/2013/05/native-level-performance-on-the-web-a-brief-examination-of-asm-js/2/) from 2013. And it is neither related to wet nor a [whetstone](https://en.wikipedia.org/wiki/Sharpening_stone), but the town of [Whetstone](https://en.wikipedia.org/wiki/Whetstone,_Leicestershire) in England.

## Linpack

Well described at [Wikipedia](https://en.wikipedia.org/wiki/LINPACK_benchmarks) this benchmark from 1979 is still usefull because it scales with instructions per second, frequency and number of cors (HPL). It took me some time to get it running.

## Dhrystone

If whet (wet) is for floating point operations, then dhry (dry) is for integer performance. This led to the [Dhrystone benchmark](https://en.wikipedia.org/wiki/Dhrystone) in 1984. Gave it a try as well. 

## [NBench](nbench)

[This benchmark (Wikipedia)](https://en.wikipedia.org/wiki/NBench) form the mid 1990s runs on a variety of hardware and has been maintained [until 2012](http://www.math.utah.edu/~mayer/linux/bmark.html) by Uwe F. Mayer. For modern computers it is rather lightwight and can be compiled on a simple linux machine with gcc in merely seconds, then run for some minutes. I collect data for this benchmark since 2006.

## [Memtest 86+](memtest86)

The data gives some inside to the architechture of the CPU and the speed of the connected memory.

## [CoreMark](CoreMark)

Intended for embedded systems by [EEMBC](https://github.com/eembc/coremark) in 2009 for embedded system it is too large for an Arduino Uno, but runs from an Arduino Mega 2560 onwards to multithreaded Octacore Xeon processor. The results show that it scales with frequency and improved IPC.

## [embench](embench)

When [comparing the power](https://content.riscv.org/wp-content/uploads/2019/06/9.25-Embench-RISC-V-Workshop-Patterson-v3.pdf) of the new [RISC-V](https://en.wikipedia.org/wiki/RISC-V) ISA some people used drystone and coremark on May 12th, 2018. Not everybody was happy. While 4.9 CoreMarks/MHz and 2.5 DMIPS/Mhz sound interesting, there are shortcomings. To provide a proper tool for comparison they developed this suite from 2019 on. Version 0.5 was released  in June 2020 at the Embedded World Conference in Nürnberg, Germany.

## [3Dmark](3Dmark)

Testing the speed of a 3D graphics card is inherent to its purpose of presenting a smooth image for the user. The benchmark from 1999 still runs on modern hardware. I longed for years to eventually have the hardware just to see the benchmark without stutter. Instead of investing in expensive hardware I relied on Moore's law and waited. Endurance payed off!

## [GeekBench](geekbench)

Some collected values from version 2 to 5 and compared in a table.

## [Crystaldisk and hdtune for non volatile memory](nvm)

Evolved speed of non volatile memory NVM over the years.

## Webbrowser

The benchmarks drove the innovation in browser development significantly, but became obsolete quite fast as well. Notable examples are Browermark 2.0, Basemark Web 3.0, peacekeeper, octane, sunspider, kraken, Jetstream and Speedometer.

