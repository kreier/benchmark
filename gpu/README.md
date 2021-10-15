# GPU performance in GFLOPS

I need more time to find software and do the measurements, but I was inpired by the comparison of the graphics performance of my PS4 Pro to other consoles. 

## FP32 single

Let's assume this is possible max raw performance in long (32 bit or single) FP32

- PS2			GFLOPS 		16 Pixel shaders
- PS3
- PS4 		1840 GFLOPS		18 CU, 8 GB GDDR5 memory 5500 MT/s
- PS4 Pro	4198 GFLOPS		36 CU, 32 ROPs, 144 TMUs, 2304 Cores, 256 bit bus, 217.6 GB/s
- PS5
- RX 470 	3793 GFLOPS
- Apple M1 	2600 GFLOPS (8-core, 128 CU or execution units, handle nearly 25,000 threads
- XBOX 360
- Xbos one S 
- XBox Series S 
- XBox Series X 

In many cases it can be simple calculated by the CPU architecture and the frequency. For example my dual [https://ark.intel.com/content/www/us/en/ark/products/37106/intel-xeon-processor-x5550-8m-cache-2-66-ghz-6-40-gt-s-intel-qpi.html](Xeon X5550) with 2.67 GHz has a [https://en.wikipedia.org/wiki/FLOPS](multiplier of 8) (Nehalem EP) which results in 2.67 x 8 = 21.36 gflops.

## FP64 double

- RX 470 	237 GFLOPS