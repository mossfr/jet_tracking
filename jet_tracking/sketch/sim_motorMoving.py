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
        while self.t < 5:
            self.ratio_pt = []
            self.ratio_pt.append(context.ratio)
            time.sleep(1 / 20)
            self.t += 1
        return statistics.mean(self.ratio_pt)

    def _start(self):
        self.sim_algorithm = self.context.sim_algorithm
        if self.sim_algorithm == "Linear Scan":
            self.sim_linear(self.context)
        elif self.sim_algorithm == "Ternary Search":
            self.sim_ternary()

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

    def sim_ternary(self):
        print("ternary search")

    def sim_test(self):
        print("you are now tracking")
#        time.sleep(5)
        self.motor_position = 0.03
        print(self.motor_position)
        self.context.update_motor_position(float(self.motor_position))


