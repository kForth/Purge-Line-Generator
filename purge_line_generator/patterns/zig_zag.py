r"""
Generate the gcode for a zig-zag pattern to purge a 3D printer nozzle before printing.

+------+    +--------------------------------+ --
|    / |    |     /\        /\        /\     |  ^
|   /  |    |    /  \      /  \      /  \    |  |
|  /   |    |   /    \    /    \    /    \   |  | Amplitude
| /    |    |  /      \  /      \  /      \  |  |
| \    |    | /        \/        \/        \ |  v
|  \   |    +--------------------------------+ --
|   \  |                          |<------>|-- Period
|    \ |
|    / |
|   /  |
|  /   |
| /    |
| \    |
|  \   |
|   \  |
|    \ |
+------+
"""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2022, Kestin Goforth"
__license__ = "AGPLv3"
__version__ = "0.1.0"
__email__ = "kgoforth1503@gmail.com"

from . import _Pattern


class ZigZagPattern(_Pattern):
    """
    Generate the gcode for a zig-zag pattern to purge a 3D printer nozzle before printing.
    """

    NAME = "ZigZag"

    @property
    def amplitude(self):
        """Amplitude of a single Zig or Zag"""
        return self.pattern_width - (self.line_width * (self.n_lines - 1))

    @property
    def period(self):
        """Period of a single Zig or Zag"""
        return self.pattern_length / (self.segments - 1)

    @property
    def seg_length(self):
        """Length of single Zig or Zag"""
        return (self.amplitude**2 + self.period**2) ** 0.5 / 2

    def make(self):
        """
        Generate the gcode for a zig-zag pattern to purge a 3D printer nozzle before printing.
        """

        # Flip x and y axes for horizontal pattern
        _x, _y, _e = (0, 1, 2) if self.horz_pattern else (1, 0, 2)

        e_dist = self.calc_e_dist(
            self.seg_length
        )  # Length to extrude for a single Zig or Zag

        pos = [self.xmin, self.ymin, 0]  # Absolute X, Y, and E positions
        for i in range(self.n_lines):
            if i == 0:
                # Move to pattern start
                yield self._do_travel_move(pos[0], pos[1])
            else:
                # Move to line start
                pos[_y] += self.line_width
                pos[_e] += self.calc_e_dist(self.line_width)
                yield self._do_print_move(*pos)

            for j in range(self.segments):
                # Add pattern position
                pos[_x] += self.period * (-1 if (i % 2 == 1) else 1)
                pos[_y] += self.amplitude * (-1 if (j % 2 == 1) else 1)

                # Extrude segment
                pos[_e] += e_dist
                yield self._do_print_move(pos[0], pos[1], pos[2])
