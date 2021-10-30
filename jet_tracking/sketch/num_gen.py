import math
import random
import matplotlib.pyplot as plt

"""
Questions for Frank

-How would we make the values better reflect "real" values we should see for i0 and diffraction?
-right now if you change the amount of dropped shots, the ratio also goes down. As I understand it, that 
shouldn't be the case which is why i look for dropped shots separately. Can we change that?
- do we need "update vals" to update anything in data stream? if so, we should have those values update in "Context"
instead.

"""


def sinwv(x, shift):
    a = random.random()
    return (a * (math.sin(x) ** 2 + shift))


class SimulationGenerator(object):
    def __init__(self, context, signals):

        # initial values from the control widget
        self.context = context
        self.signals = signals
        self.percent_dropped = 10
        self.peak_intensity = 10
        self.motor_position = 0
        self.radius = 0.025
        self.center = 0.03
        self.max = 10
        self.bg = 0.05
        self.percent = 0

    def sim(self):

        val = {}
        val["i0"] = self.context.peak_intensity
        val["diff"] = self.context.max
        val["ratio"] = 1
        val["dropped"] = False

        a = random.random()
        # dropped shots. for input percentage of shots, 0 is returned for the scattering intensity
        b = random.random()
        c = random.random()
        self.percent = self.context.percent_dropped/100

# dropped shots
        if b < self.percent:
#            val["diff"] = 0
            val["dropped"] = True
            val["diff"] = (self.context.bg / 10) * (1 + (a - 0.5))
            val["i0"] = self.context.bg * (1 + (c - 0.5))

# on jet
        else:
            # calculates length of chord of a circle if on jet or sets diff to 0 (plus noise) if off jet
            if abs(self.context.motor_position - self.context.center) < self.context.radius:
                val["diff"] = self.context.max * ((2 * math.sqrt(self.context.radius ** 2 - abs(self.context.motor_position - self.context.center) ** 2)) / (2 * self.context.radius)) * (
                            1 + self.context.bg * (a - 0.5))
                val["dropped"] = False
                val["i0"] = self.context.peak_intensity * 1 + self.context.bg * (c - 0.5)

# off jet
            else:
                val["diff"] = self.context.bg * (1 + (a - 0.5))
                val["dropped"] = False
                val["i0"] = self.context.peak_intensity * 1 + self.context.bg * (c - 0.5)

        val["ratio"] = val["diff"] / val["i0"]
        self.context.update_ratio(val["ratio"])
        self.context.update_dropped(val["dropped"])
        return val
