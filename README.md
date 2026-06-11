# navaismo-gcode-scripts
This is a multi-purpose tool for manipulating Creality Print G-code files to support various features of [navaismo's Ender 3 v3 SE modified firmware](https://github.com/navaismo/Marlin_bugfix_2.1_E3V3SE).

## Installation
1. Get Python and preferably add it to PATH. Any version should be fine but I have 3.12.
2. In Creality Print, navigate to `Others` > `Post-processing scripts` (you may need to enable `Advanced` mode near the top of the settings drawer). Add: `python <full path to script>`. Linux users may need to use `python3` or similar instead.
3. Export any G-code and scroll to the very bottom. If you see something similar to the following:
```
; filament used [mm] = 30.00, 0.00, 0.00, 0.00, 4976.26, 0.00
; filament used [cm3] = 0.07, 0.00, 0.00, 0.00, 11.97, 0.00
; filament used [g] = 0.09, 0.00, 0.00, 0.00, 14.84, 0.00
; filament cost = 0.00, 0.00, 0.00, 0.00, 0.45, 0.00
; total filament cost = 0.45
; total layers count = 300
; estimated printing time (normal mode) = 55m 11s
```
Then the tool is working!

## Features
- Corrected detection of thumbnail
- Relocation of info footer to bottom so that the firmware reads it correctly