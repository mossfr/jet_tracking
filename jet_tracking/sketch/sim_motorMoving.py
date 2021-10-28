import math
import statistics
import random
import matplotlib.pyplot as plt
import time
import logging
from datastream import ValueReader
from PyQt5.QtCore import QThread
import threading

log = logging.getLogger(__name__)


class SimulatedMotor(object):

    def __init__(self, context, signals):

        # initial values from the control widget
        self.context = context
        self.signals = signals
        self.motor_position = 0
        self.i0 = 0
        self.ratio = 0
        self.ratio_ave = 0
        self.ratio_pt = []
        self.positions = []
        self.max_ratio = 0
        self.index_max = 0
        self.max_motor = 0
        self.motor_initial = 0
        self.ratio_initial = 0
        self.t = 0
        self.ratios = []
        self.left = -0.1
        self.right = 0.1
        self.step = 0.01
        self.wait = 5
        self.sim_algorithm = "Linear Scan"
        # get current simulated motor position
#        self.signals.update.connect(self.updateVals)
        self.signals.changeMotorPosition.connect(self.change_motor)
        self.signals.changeSimAlgorithm.connect(self.change_algorithm)

#        self.make_connections()
        self.set_sim_options()

    def set_sim_options(self):
        self.context.update_motor_position(float(self.motor_position))
        self.context.update_sim_algorithm(str(self.sim_algorithm))

    def change_motor(self, motor_position):
        self.motor_position = motor_position

    def change_algorithm(self, al):
        self.sim_algorithm = al

    def average_intensity(self, context):
        self.t = 0
        while self.t < 10:
            if context.dropped is False:
                self.ratio_pt = []
                self.ratio_pt.append(context.ratio)
                time.sleep(1 / 10)
                self.t += 1
            else:
                time.sleep(1 / 10)
                pass
        return statistics.mean(self.ratio_pt)

    def _start(self):
        self.sim_algorithm = self.context.sim_algorithm
        if self.sim_algorithm == "Linear Scan":
            self.sim_linear(self.context)
        elif self.sim_algorithm == "Ternary Search":
            self.sim_ternary(self.context)

    def sim_linear(self, context):
        self.motor_initial = context.motor_position
        self.ratio_initial = self.average_intensity(context)
        self.motor_position = self.left
        self.ratio_pt = []
        self.t = 0
        self.left = -0.1
        self.right = 0.1
        self.ratios = []
        self.positions = []
        self.max_ratio = 0
        self.index_max = 0
        self.max_motor = 0
        while self.motor_position <= self.right:
            self.ratio_ave = self.average_intensity(context)
            self.ratios.append(self.ratio_ave)
            self.positions.append(self.motor_position)
            self.motor_position += 0.01
            self.context.update_motor_position(self.motor_position)
        self.max_ratio = max(self.ratios)
        self.index_max = self.ratios.index(self.max_ratio)
        self.max_motor = self.positions[self.index_max]
        if self.max_ratio >= self.ratio_initial:
            self.context.update_motor_position(self.max_motor)
        else:
            self.context.update_motor_position(self.motor_initial)

    def sim_ternary(self, context):
        self.left = -0.3
        self.right = 0.3
        self.left_third = 0
        self.right_third = 0
        self.tol = 0.01
        self.motor_position = context.motor_position
        self.ratio_left = 0
        self.ratio_right = 0
        self.center = 0
        while abs(self.left - self.right) >= self.tol:
            self.left_third = self.left + (self.right - self.left) / 3
            self.motor_position = self.left_third
            self.context.update_motor_position(self.motor_position)
            self.ratio_left = self.average_intensity(context)
            self.right_third = self.right - (self.right - self.left) / 3
            self.motor_position = self.right_third
            self.context.update_motor_position(self.motor_position)
            self.ratio_right = self.average_intensity(context)
            if self.ratio_left < self.ratio_right:
                self.left = self.left_third
            else:
                self.right = self.right_third
        self.motor_position = (self.right + self.left) / 2
        self.context.update_motor_position(self.motor_position)
#        print(self.motor_position)

    def sim_golden_section(self):
        print("golden section search")

    def sim_tracking(self):
        self.track(self.context)

    def track(self, context):
        self.low = 0.9 * 1
        self.ratio_ave = 1
        while context.simTracking is True:
            time.sleep(5)
#            print("tracking")
            self.ratio_ave = self.average_intensity(context)
            print(self.ratio_ave)
            if self.ratio_ave < self.low:
#                print("starting search")
                self._start()
            else:
                time.sleep(1)
                self.ratio_ave = self.average_intensity(context)


