# Phoronix Test Suite

Source and information [on github](https://github.com/phoronix-test-suite/phoronix-test-suite/).

For me just `me@i9:~$ sudo apt install php php-xml` and then followes by

``` bash
git clone https://github.com/phoronix-test-suite/phoronix-test-suite/
cd phoronix-test-suite
sudo ./install-sh
phoronix-test-suite system-info
```

And then the individual tests:

## CPU (Single Core)

``` bash
phoronix-test-suite install pts/encode-flac
phoronix-test-suite benchmark pts/encode-flac
```

https://openbenchmarking.org/result/2402098-NE-10100599594

## CPU (Multi-Core)

``` bash
phoronix-test-suite install pts/himeno
phoronix-test-suite benchmark pts/himeno
```

https://openbenchmarking.org/result/2402098-NE-10100690794

## RAM

``` bash
phoronix-test-suite install pts/ramspeed
phoronix-test-suite benchmark pts/ramspeed
```

## Flash Memory

``` bash
phoronix-test-suite install pts/iozone
phoronix-test-suite benchmark pts/iozone
```








## Inspiration

In 2015 with the new Raspberry Pi 2 and Intel Edison [Sparkfun compared their speed](https://learn.sparkfun.com/tutorials/single-board-computer-benchmarks/all).
