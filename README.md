# Benchmark collection

There are countless benchmarks out there. This is just a collection of benchmarks I used myself over the years and a list of the results gained in this time. While some tests date back to 1972 and I measured the speed of my Lattice C compiler against Omicron Basic on my Atari ST in 1992, the presented data collection here started in 2007 with Memtest86+ and the website http://saiht.de/computer/benchmark.html .

## NBench

[This benchmark](https://en.wikipedia.org/wiki/NBench) form the mid 1990s runs on a variety of hardware and has been maintained [until 2012](http://www.math.utah.edu/~mayer/linux/bmark.html) by Uwe F. Mayer. For modern computers it is rather lightwight and can be compiled on a simple linux machine with gcc in merely seconds, then run for some minutes. I collect data for this benchmark since 2006.

## Linpack

Well described at [Wikipedia](https://en.wikipedia.org/wiki/LINPACK_benchmarks) this benchmark from 1979 is still usefull because it scales with instructions per second, frequency and number of cors (HPL). It took me some time to get it running.

## Whetstone

This [synthetic benchmark from 1972](https://en.wikipedia.org/wiki/Whetstone_(benchmark)) is one of the oldest ones to estimate the [FLOPS](https://en.wikipedia.org/wiki/FLOPS) a CPU can perform. Well described in an [article of arstechnica](https://arstechnica.com/information-technology/2013/05/native-level-performance-on-the-web-a-brief-examination-of-asm-js/2/) from 2013.

## Dhrystone

Not Whether it can perform, just dry integer operations lead to the [Dhrystone benchmark](https://en.wikipedia.org/wiki/Dhrystone) in 1984. Gave it a try as well.

## Memtest 86+

The data gives some inside to the architechture of the CPU and the speed of the connected memory.

## 3Dmark

Testing the speed of a 3D graphics card is inherent to its purpose of presenting a smooth image for the user. The benchmark from 1999 still runs on modern hardware. I longed for years to eventually have the hardware just to see the benchmark without stutter. Instead of investing in expensive hardware I relied on Moore's law and endurance payed off!

## Crystaldisk and hdtune

...

## Webbrowser

The benchmarks drove the innovation in browser development significantly, but became obsolete quite fast as well. Notable examples are Browermark 2.0, Basemark Web 3.0, peacekeeper, octane, sunspider, kraken, Jetstream and Speedometer.

