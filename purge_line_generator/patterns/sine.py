"""
Generate the gcode for a sine wave pattern to purge a 3D printer nozzle before printing.
"""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2022, Kestin Goforth"
__license__ = "AGPLv3"
__version__ = "0.1.0"
__email__ = "kgoforth1503@gmail.com"

import math

from . import _Pattern


class SinePattern(_Pattern):
    """
    Generate the gcode for a sine-wave pattern to purge a 3D printer nozzle before printing.
    """

    NAME = "Sine"

    @property
    def amplitude(self):
        """Amplitude of a sine wave"""
        return (self.pattern_width - (self.line_width * (self.n_lines - 1))) / 2

    @property
    def period(self):
        """Period of a sine wave"""
        return self.pattern_length / (self.segments - 1)

    def make(self):
        """
        Generate the gcode for a sine wave pattern to purge a 3D printer nozzle before printing.
        """

        # Flip x and y axes for horizontal pattern
        _x, _y, _e = (0, 1, 2) if self.horz_pattern else (1, 0, 2)

        pos = [self.xmin, self.ymin, 0]  # Absolute X, Y, and E positions
        for i in range(self.n_lines):
            if i == 0:
                # Move to pattern start
                yield self._do_travel_move(pos[_x], pos[_y])
            else:
                # Move to line start
                pos[_y] += self.line_width
                pos[_e] += self.calc_e_dist(self.line_width)
                yield self._do_print_move(*pos)

            for _ in range(self.segments):
                _dx = self.period / 15  # Solve 15 points per segment
                dx = 0
                while dx <= self.period:
                    dy = -self.amplitude * (math.cos(dx / self.period * 2 * math.pi) - 1)
                    pos[_e] += self.calc_e_dist((dx**2 + dy**2) ** 0.5)

                    # Extrude segment
                    seg_pos = list(pos)
                    seg_pos[_x] += dx * (-1 if (i % 2 == 1) else 1)
                    seg_pos[_y] += dy
                    yield self._do_print_move(*seg_pos)
                    dx += _dx

                pos[_x] += self.period * (-1 if (i % 2 == 1) else 1)
                pos[_e] += self.calc_e_dist(
                    ((pos[_x] - seg_pos[_x]) ** 2 + (pos[_y] - seg_pos[_y]) ** 2) ** 0.5
                )
                yield self._do_print_move(*seg_pos)
