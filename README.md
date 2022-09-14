# Purge Line Generator

<!-- <a href="https://pypi.python.org/pypi/purge_line_generator" target="_blank" rel="noopener">
    <img src="https://img.shields.io/pypi/v/purge_line_generator.svg" alt="PyPi">
</a> -->

## Description

Generate various purge lines for cleaning your 3d printer nozzle:

| Pattern  | Image |
|:---------|:-----:|
| ZigZag   | ![]() |
| Straight | ![]() |
| Sine     | ![]() |

## Insallation

### Requirements
- Python >= 3.6

### Setup

Install using pip:

    pip install git+https://github.com/kForth/Purge-Line-Generator.git

Or clone this repository and install locally:

    git clone https://github.com/kForth/Purge-Line-Generator.git
    cd Purge-Line-Generator
    pip install -e .

## Usage

```
usage: purge_line_generator [-h] [-p {0,1,2}] [-d NOZZLE_DIAMETER] [-t THICKNESS] [-w WIDTH] [-l LINES] [-n NUM_FEATURES] [-v VOLUMETRIC_FLOWRATE] [-m MAX_FEEDRATE] [-f FILAMENT_DIAMETER] [-i] [--decimals DECIMALS] XMIN XMAX YMIN YMAX

Console script for purge_line_generator.

positional arguments:
  XMIN                  Min X (mm)
  XMAX                  Max X (mm)
  YMIN                  Min Y (mm)
  YMAX                  Max Y (mm)

options:
  -h, --help            show this help message and exit
  -p {0,1,2}, --pattern {0,1,2}
                        Purge Pattern (0=ZigZag, 1=Straight, 2=Sine) (default: 0)
  -d NOZZLE_DIAMETER, --nozzle-diameter NOZZLE_DIAMETER
                        Nozzle diameter (mm) (default: 0.4)
  -t THICKNESS, --thickness THICKNESS
                        Line thickness (% of nozzle diameter) (default: 50)
  -w WIDTH, --width WIDTH
                        Line width (% of nozzle diameter) (default: 120)
  -l LINES, --lines LINES
                        Number of parallel purge lines (default: 1)
  -n NUM_FEATURES, --num-features NUM_FEATURES
                        Number of features in each purge line. (0 = auto) (zigzag: num triangles, straight: NA) (default: 0)
  -v VOLUMETRIC_FLOWRATE, --volumetric-flowrate VOLUMETRIC_FLOWRATE
                        Volumetric Flowrate (mm^3/s) (default: 8)
  -m MAX_FEEDRATE, --max-feedrate MAX_FEEDRATE
                        Max Feedrate (mm/s) (default: 25)
  -f FILAMENT_DIAMETER, --filament-diameter FILAMENT_DIAMETER
                        Filament Diameter (mm) (default: 1.75)
  -i, --invert-pattern  Invert Pattern (default: False)
  --decimals DECIMALS   Number of decimal places in gcode file (default: 4)
```

## Sample Output
`purge_line_generator 0 5 0 100 -d 0.6 -v 4 -p 2`

```gcode
G0 X0.0000 Y0.0000 Z0.3000 F1080
G1 X0.0000 Y0.0000 E0.0000 F1080
G1 X0.2161 Y0.7407 E0.0693 F1080
G1 X0.8272 Y1.4815 E0.2217 F1080
G1 X1.7275 Y2.2222 E0.4744 F1080
G1 X2.7613 Y2.9630 E0.8381 F1080
G1 X3.7500 Y3.7037 E1.3115 F1080
G1 X4.5225 Y4.4444 E1.8809 F1080
G1 X4.9454 Y5.1852 E2.5244 F1080
G1 X4.9454 Y5.9259 E3.2175 F1080
G1 X4.5225 Y6.6667 E3.9409 F1080
...
```

## License

Copyright © 2022 [Kestin Goforth](https://github.com/kforth/).

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) for more details.
