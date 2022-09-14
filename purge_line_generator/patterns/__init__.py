__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2022, Kestin Goforth"
__license__ = "AGPLv3"
__version__ = "0.1.0"
__email__ = "kgoforth1503@gmail.com"

import math
from abc import abstractmethod


class _Pattern:
    NAME = "Pattern"

    def __init__(
        self,
        xmin,
        xmax,
        ymin,
        ymax,
        nozzle_diameter,
        thickness_p,
        width_p,
        n_lines,
        n_features,
        flowrate,
        filament_diameter,
        max_feedrate,
        invert,
        decimals,
    ):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.nozzle_diameter = nozzle_diameter
        self.thickness_p = thickness_p
        self.width_p = width_p
        self.n_lines = n_lines
        self.n_features = n_features
        self.flowrate = flowrate
        self.filament_diameter = filament_diameter
        self.max_feedrate = max_feedrate
        self.invert = invert
        self.decimals = decimals

    @property
    def bbox_size_x(self):
        """Pattern size in X-Axis"""
        return abs(self.xmax - self.xmin)

    @property
    def bbox_size_y(self):
        """Pattern size in Y-Axis"""
        return abs(self.ymax - self.ymin)

    @property
    def horz_pattern(self):
        """True if the pattern should run horizontally"""
        if self.invert:
            return self.bbox_size_x <= self.bbox_size_y
        return self.bbox_size_x >= self.bbox_size_y

    @property
    def pattern_length(self):
        """Length of pattern"""
        return self.bbox_size_x if self.horz_pattern else self.bbox_size_y

    @property
    def pattern_width(self):
        """Width of pattern"""
        return self.bbox_size_y if self.horz_pattern else self.bbox_size_x

    @property
    def line_width(self):
        """Actual width of extruded line"""
        return self.nozzle_diameter * self.width_p / 100

    @property
    def line_thickness(self):
        """Actual thickness of extruded line"""
        return self.nozzle_diameter * self.thickness_p / 100

    @property
    def line_area(self):
        """Cross-Sectional area of extruded line"""
        return self.line_thickness * self.line_width

    @property
    def fil_area(self):
        """Cross-Sectional area of filament"""
        return math.pi * (self.filament_diameter / 2) ** 2

    @property
    def feedrate(self):
        """Feedrate for printing move"""
        return math.floor(max(1, min(self.max_feedrate, self.flowrate / self.line_area)))

    @property
    def segments(self):
        """Auto fit n sections of approx width 20mm"""
        return (self.n_features or int(self.pattern_length // 20)) * 2

    def calc_e_dist(self, dist):
        """Calculate the extruder distance for a given travel distance"""
        return dist * self.line_area / self.fil_area

    def _do_print_move(self, x, y, e, f=None):
        x = f"%0.{self.decimals}f" % x
        y = f"%0.{self.decimals}f" % y
        e = f"%0.{self.decimals}f" % e
        f = math.floor((f or self.feedrate) * 60)
        return f"G1 X{x} Y{y} E{e} F{f:d}"

    def _do_travel_move(self, x, y, z=None, f=None):
        x = f"%0.{self.decimals}f" % x
        y = f"%0.{self.decimals}f" % y
        z = f"%0.{self.decimals}f" % (z or self.line_thickness)
        f = math.floor((f or self.feedrate) * 60)
        return f"G0 X{x} Y{y} Z{z} F{f:d}"

    @abstractmethod
    def make(self):
        """
        Generate the gcode for the current purge line pattern.
        """
        yield []
