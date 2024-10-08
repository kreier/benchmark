# GPU performance in GFLOPS

On the way to a [GPGPU](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) and to compare the processing speed I tried to collect some theoretical GFLOPS data as well as measuring the computation speed in half-precision, single and double precision (FP16, FP32 and FP64) with OpenCL. In the near future some TOPS with INT8 for NPUs and __bf16__ numbers for GPUs will be interesting with tne new wave of AI and LLMs. 

![GFLOPS of some GPUs](./gpu2024.png)

In many cases the limiting factor for the performance of an LLM is not the sheer processing power of the CPU or GPU, but the bandwidth to access the memory. And the whole model has to fit into the RAM! This limits the size on many consumer GPUs, or makes it expensive to run these models. Fast memory is expensive. I compared the speed of a few links to memory from DDR3 over Ethernet and USB4 with the memory bus of some of my graphics cards:

<img src="comparison_speed_linear.png" width="49%"> <img src="comparison_speed_logarithmic.png" width="49%">

The difference spans several magnitudes, so I included a logarithmic graph to the right. Even DDR5 with dual channel is no match for GDDR6X RAM or even HBM (high bandwidth memory).


Below some text from 2020 when I started to collect some information:

## FP32 single precision

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

In many cases it can be simple calculated by the CPU architecture and the frequency. For example my dual [Xeon X5550](https://ark.intel.com/content/www/us/en/ark/products/37106/intel-xeon-processor-x5550-8m-cache-2-66-ghz-6-40-gt-s-intel-qpi.html) with 2.67 GHz has a [multiplier of 8](https://en.wikipedia.org/wiki/FLOPS) (Nehalem EP) which results in 2.67 x 8 = 21.36 gflops.

## FP64 double precision

- RX 470 	237 GFLOPS
