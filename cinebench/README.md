# Cinebench

## R23 for CPU Multi Core

| Device                   | CPU        | Cores | Single Core | Multi-Core | Watt |
|--------------------------|------------|------:|------------:|-----------:|-----:|
| Lenovo Thinkpad Yoga 370 | i5-7300U   |   2/4 |         475 |       1202 |      |
| HP EliteDesk 800 G4 mini | i5-8500T   |   6/6 |         828 |       3822 |      |
| HP zBook 15 G3           | i7-6820HQ  |   4/8 |         814 |       3950 |      |
| HP Z600 Workstation      | X5550 x2   |  8/16 |         476 |       4489 |      |
| Xigmatek Gemini          | i3-10100   |   4/8 |        1043 |       4683 |      |
| HP Elitedesk 800 G4 TWR  | i7-8700    |  6/12 |             |            |      |
| HP Pro Mini 400 G9       | i7-13700T  | 16/24 |        1759 |      10286 |   35 |
| Workstation II           | E5-2696 v3 | 18/36 |         724 |      11164 |  145 |


## Cinebench 2024 for CPU and GPU

Some argue that it is favored for Apple products, others are happy to get the same 3 categories as Geekbench: CPU single core, CPU multi-core and GPU if the graphics card has 8GB RAM or more and is a fairly recent model.

I tested some of my systems:

| Device                   | CPU        | Cores | Single Core | Multi-Core |     GPU       |  pts   |
|--------------------------|------------|------:|------------:|-----------:|---------------|-------:|
| HP Z600 Workstation      | X5550 x2   |  8/16 | – <sup>1</sup> | – <sup>1</sup> | RX 470 | – <sup>2</sup> |
| Lenovo Thinkpad Yoga 370 | i5-7300U   |   2/4 |          36 |         83 | UHD 620       | – <sup>2</sup> |
| HP zBook 15 G3           | i7-6820HQ  |   4/8 |          52 |        235 | Quadro M1000M | – <sup>2</sup> |
| HP EliteDesk 800 G4 mini | i5-8500T   |   6/6 |          54 |        258 | UHD 630       | – <sup>2</sup> |
| Xigmatek Gemini          | i3-10100   |   4/8 |          61 |        274 | RTX 3070 Ti   | 10263 |
| HP Elitedesk 800 G4 TWR  | i7-8700    |  6/12 |          70 |        417 | RTX 3060 Ti   |  8709 |
| Macbook Air 2022         | M1         |   8/8 |         111 |        465 | 8CU 16GB      |  1167 |
| Workstation II           | E5-2696 v3 | 18/36 |          51 |        530 | RX 6600       |       |
| HP Pro Mini 400 G9       | i7-13700T  | 16/24 |         104 |        602 | UHD 770       | – <sup>2</sup> |

Notes:
1. Requires CPU with [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2) support, also known as __Haswell New Instructions__
2. Requires a GPU with 8GB VRAM and architecture of Vega or newer or CUDA compute 5.0 (900 series) or later
