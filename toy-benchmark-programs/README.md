# Toy Benchmark Programs

This name is not my idea, I found the term and related pitfalls here: [https://benchmarksgame-team.pages.debian.net/benchmarksgame/why-measure-toy-benchmark-programs.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/why-measure-toy-benchmark-programs.html)

For more information in 24 languages:

## [Benchmark game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/) - Which programming language is the fastest?

Compiled in 2018 (with history going back to 2002) several benchmarks compare the execution speed of programs in 24 languages. Many are optimized for multicore parallel execution, to make modern processors comparable. Probably disable the efficiency cores might speed up the processes.

At least I got the mandelbrot in C++ running:

## Mandelbrot in C++

In [this subfolder](mandelbrot_cpp) I copied the sourcecode from [benchmarksgame-team.debian](https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/mandelbrot.html#mandelbrot) and wrote a little `Makefile` that works in Ubuntu in WSL. Original taken form [this source](https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/mandelbrot-gpp-6.html).

<img src="../docs/1x1.png" width="20%"><img src="../docs/mandelbrot200.png" width="30%">
