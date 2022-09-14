"""
Generate the gcode for a straght line pattern to purge a 3D printer nozzle before printing.

+-------+    +--------------------------+
|  _    |    | _______________________  |
| | | ! |    |  ______________________| |
| | | | |    | |______________________  |
| | | | |    |                          |
| | | | |    +--------------------------+
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| ! |_| |
+-------+
"""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2022, Kestin Goforth"
__license__ = "AGPLv3"
__version__ = "0.1.0"
__email__ = "kgoforth1503@gmail.com"

from . import _Pattern


class StraightPattern(_Pattern):
    """
    Generate the gcode for a straight line pattern to purge a 3D printer nozzle before printing.
    """

    NAME = "Straight"

    @property
    def spacing(self):
        """Spacing between each line"""
        return self.pattern_width / (self.n_lines - 1)

    def make(self):
        """
        Generate the gcode for a straight pattern to purge a 3D printer nozzle before printing.
        """

        # Flip x and y axes for horizontal pattern
        _x, _y, _e = (0, 1, 2) if self.horz_pattern else (1, 0, 2)

        e_dist = self.calc_e_dist(
            self.pattern_length
        )  # Length to extrude for a single line

        pos = [self.xmin, self.ymin, 0]  # Absolute X, Y, and E Positions
        for i in range(self.n_lines):
            if i == 0:
                # Move to pattern start
                yield self._do_travel_move(pos[0], pos[1])
            else:
                # Move to line start
                pos[_y] += self.spacing
                pos[_e] += self.calc_e_dist(self.spacing)
                yield self._do_print_move(*pos)

            # Extrude segment
            pos[_x] += self.pattern_length * (-1 if (i % 2 == 1) else 1)
            pos[_e] += e_dist
            yield self._do_print_move(*pos)
