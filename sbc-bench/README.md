# Single Board Computer Benchmark - sbc-bench

What a great tool! So many things included we look for in our little single board computers like Raspberry Pi and TV boxes.

Some of my results:

- Raspberry Pi 1 model B, BCM2835 512 MB [ARMv6Z ARM11](https://en.wikipedia.org/wiki/ARM11) [2024-02-13](https://sprunge.us/WWgaCH)
- Rockchip rk3229 [ARMv7-A Cortex-A7](https://en.wikipedia.org/wiki/ARM_Cortex-A7) [2024-02-04](https://sprunge.us/ABPd1y) and throttled [in enclosure](https://sprunge.us/RMd57e)
- Raspberry Pi 3 model B 1.2, BCM2837 1 GB [ARMv8-A Cortex-A53](https://en.wikipedia.org/wiki/ARM_Cortex-A53) [2024-02-09 32bit](https://sprunge.us/MjKNxl) [unthrottled](https://sprunge.us/6Vndme) and [64bit](https://sprunge.us/YVrDcI)
- Raspberry Pi 4 model B, BCM2711 4GB [2024-02-09](https://sprunge.us/9HpkrB)
- i3 10100 [2024-02-04](https://sprunge.us/0lOI8m)

## Source and reason

All well described by Thomas Kaiser [in his repository](https://github.com/ThomasKaiser/sbc-bench). Since July 2018 already!

## Table

*The below table is also available sorted: [7-zip multi-threaded](Sorted-Results.md#7-zip-mips-multi-threaded), [7-zip single-threaded](Sorted-Results.md#7-zip-mips-single-threaded), [aes-256-cbc](Sorted-Results.md#openssl-speed--elapsed--evp-aes-256-cbc), [memcpy](Sorted-Results.md#memcpy), [memset](Sorted-Results.md#memset) and [clockspeed](Sorted-Results.md#clockspeed).*

| Device / details               | Clockspeed           | Kernel |        Distro        |   7-zip multi | 7-zip single |     AES | memcpy | memset | kH/s |
| ------------------------------ | :------------------: | :----: | :------------------: | ------------: | -----------: | ------: | -----: | -----: | ---: |
| Raspberry Pi Model B Rev 2     |  700 MHz (throttled) |  6.1   | Raspbian GNU/Linux 12 (bookworm) armv6l/armhf | 290 | 293 | 11530 | 330 | 1350 | - |
| Generic RK322x Tv Box board    | 1392 MHz (throttled) |  6.1   | Armbian 23.11.1 bookworm armhf/arm   |  2350 |  655 |   26940 |    890 |  2920 | - |
| Generic RK322x Tv Box board    | 1392 MHz             |  6.1   | Armbian 23.11.1 jammy armhf/arm      |  2650 |  811 |   26920 |    500 |  2390 | - |
| Raspberry Pi 3 Model B Rev 1.2 | 1200 MHz (throttled) |  5.10  | Raspbian GNU/Linux 10 (buster) armhf |  1830 |  688 |   26430 |    810 |  1490 | - |
| Raspberry Pi 3 Model B Rev 1.2 | 1200 MHz             |  5.10  | Raspbian GNU/Linux 10 (buster) armhf |  3220 |  956 |   36550 |    960 |  1490 | - |
| Raspberry Pi 3 Model B Rev 1.2 | 1200 MHz (throttled) |  6.1   | Debian GNU/Linux 12 (bookworm) arm64 |  2380 |  913 |   39770 |   1140 |  1630 | - |
| Raspberry Pi 3 Model B Rev 1.2 | 1200 MHz             |  6.1   | Debian GNU/Linux 12 (bookworm) arm64 |  2380 |  914 |   39770 |   1180 |  1630 | - |
| RPi 4 Model B Rev 1.1 / BCM2711 Rev B0 | 1500 MHz     |  6.1   | Debian GNU/Linux 12 (bookworm) arm64 |  5020 | 1506 |   30200 |   2460 |  3150 | - |
| i5-7300U @ 2.60GHz WSL2 VM     | ~3500 MHz            |  5.15  | Ubuntu 20.04.6 LTS (focal) x86_64/amd64 |  8110 | 3639 | 954110 |  2050 |  2690 | - |
| X5550 @ 2.67GHz WSL2 VM        | ~3020 MHz            |  5.15  | Ubuntu 18.04.6 LTS (bionic) x86_64/amd64 | 27300 | 3157 | 214670 | 5420 |  8170 | - |
| i5-8500T @ 2.10GHz WSL2 VM     | ~3350 MHz            |  5.15  | Ubuntu 22.04.3 LTS (jammy) x86_64/amd64 | 18320 | 3820 | 903660 | 15050 | 26470 | - |
| i7-6820HQ @ 2.70GHz WSL2 VM    | ~3520 MHz            |  5.15  | Ubuntu 20.04.6 LTS (focal) x86_64/amd64 | 18910 | 4150 | 961680 | 13230 | 31510 | - |
| i3-10100 @ 3.60GHz WSL2 VM     | ~4150 MHz            |  5.15  | Ubuntu 22.04.3 LTS x86_64/amd64      | 22270 | 4658 | 1113290 |  14250 | 31430 | - |
