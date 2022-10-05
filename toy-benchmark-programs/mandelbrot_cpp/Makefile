.SILENT: test
all: compile test

compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge -fopenmp -mno-fma --std=c++14 mandelbrot.c++ -o mandelbrot.c++.o
	/usr/bin/g++ mandelbrot.c++.o -o mandelbrot.gpp_run -fopenmp

test:
	time ./mandelbrot.gpp_run > /dev/null
