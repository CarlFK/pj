

# Install
in this dir (because it isn't setup as a module)
```
git clone https://github.com/realthunder/kicad_parser
```

# Usage
 * in Kicad: Schematic Editor
 * File/Export/Netlist
 * click (Export Netlist) button
 * filename: pj.net
 * click (Save) button.

```
$ python pj.py 0 6
TMS | BCM27 | 13 | 9 | GPIO6
TDI | BCM26 | 37 | 10 | GPIO7
TCK | BCM25 | 22 | 11 | GPIO8
TDO | BCM24 | 18 | 12 | GPIO9
RTCK | BCM23 | 16 | 14 | GPIO10
TRST | BCM22 | 15 | 15 | GPIO11

$ python pj.py 6 8
pico TX | BCM15_RXD | 10 | 1 | GPIO0
pico RX | BCM14_TXD | 8 | 2 | GPIO1

$ python pj.py 8 10
x1 | BCM4_GPCLK0 | 7 | 16 | GPIO12
x2 | BCM3_SCL | 5 | 17 | GPIO13
```


