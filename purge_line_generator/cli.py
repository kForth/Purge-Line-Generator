"""Console script for purge_line_generator."""
import argparse
import sys

from .patterns.sine import SinePattern
from .patterns.straight import StraightPattern
from .patterns.zig_zag import ZigZagPattern


def main():
    """Console script for purge_line_generator."""

    parser = argparse.ArgumentParser(
        prog="purge_line_generator",
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("xmin", metavar="XMIN", type=float, help="Min X (mm)")
    parser.add_argument("xmax", metavar="XMAX", type=float, help="Max X (mm)")
    parser.add_argument("ymin", metavar="YMIN", type=float, help="Min Y (mm)")
    parser.add_argument("ymax", metavar="YMAX", type=float, help="Max Y (mm)")

    patterns = (ZigZagPattern, StraightPattern, SinePattern)
    pattern_codes = [f"{i}={e.NAME}" for i, e in enumerate(patterns)]
    parser.add_argument(
        "-p",
        "--pattern",
        type=int,
        default=0,
        choices=range(0, len(patterns)),
        help=f"Purge Pattern  ({', '.join(pattern_codes)})",
    )

    parser.add_argument(
        "-d",
        "--nozzle-diameter",
        type=float,
        default=0.4,
        help="Nozzle diameter (mm)",
    )

    parser.add_argument(
        "-t",
        "--thickness",
        type=int,
        default=50,
        help="Line thickness (%% of nozzle diameter)",
    )

    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=120,
        help="Line width (%% of nozzle diameter)",
    )

    parser.add_argument(
        "-l",
        "--lines",
        type=int,
        default=1,
        help="Number of parallel purge lines",
    )

    parser.add_argument(
        "-n",
        "--num-features",
        type=int,
        default=0,
        help="Number of features in each purge line. (0 = auto) (zigzag: num triangles, straight: NA)",
    )

    parser.add_argument(
        "-v",
        "--volumetric-flowrate",
        type=float,
        default=8,
        help="Volumetric Flowrate (mm^3/s)",
    )

    parser.add_argument(
        "-m",
        "--max-feedrate",
        type=float,
        default=25,
        help="Max Feedrate (mm/s)",
    )

    parser.add_argument(
        "-f",
        "--filament-diameter",
        type=float,
        default=1.75,
        help="Filament Diameter (mm)",
    )

    parser.add_argument(
        "-i",
        "--invert-pattern",
        action="store_true",
        help="Invert Pattern",
    )

    parser.add_argument(
        "--decimals",
        type=int,
        default=4,
        help="Number of decimal places in gcode file",
    )

    args = parser.parse_args()

    pattern_type = patterns[args.pattern]
    if pattern_type:
        pattern = pattern_type(
            xmin=args.xmin,
            xmax=args.xmax,
            ymin=args.ymin,
            ymax=args.ymax,
            nozzle_diameter=args.nozzle_diameter,
            thickness_p=args.thickness,
            width_p=args.width,
            n_features=args.num_features,
            n_lines=args.lines,
            flowrate=args.volumetric_flowrate,
            filament_diameter=args.filament_diameter,
            max_feedrate=args.max_feedrate,
            invert=args.invert_pattern,
            decimals=args.decimals,
        )
        gcode = pattern.make()
        for line in gcode:
            print(line)
    else:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
