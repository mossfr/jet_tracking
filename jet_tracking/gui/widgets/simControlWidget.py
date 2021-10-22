from PyQt5.QtWidgets import QFrame
from gui.widgets.simControlWidgetUi import Sim_Ui
from datastream import StatusThread, MotorThread
import logging
from sketch.sim_motorMoving import SimulatedMotor
import threading

log = logging.getLogger(__name__)


class SimWidget(QFrame, Sim_Ui, SimulatedMotor):

    def __init__(self, context, signals):
        super(SimWidget, self).__init__()
        self.signals = signals
        self.context = context
        self.setupUi(self)
        self.initialize_threads()
        self.make_connections()
        self.set_sim_options()
        self.left = -0.1
        self.right = 0.1
        self.ratio = self.context.ratio
        self.ratios = []

    def initialize_threads(self):
        self.sim_status = StatusThread(self.context, self.signals)

    def set_sim_options(self):
        self.context.update_motor_position(float(self.box_motor_pos.text()))
        self.context.update_dropped_shots(float(self.box_percent_drop.text()))
        self.context.update_peak_intensity(float(self.box_int.text()))
        self.context.update_jet_radius(float(self.box_jet_radius.text()))
        self.context.update_jet_center(float(self.box_jet_center.text()))
        self.context.update_max_intensity(float(self.box_max_int.text()))
        self.context.update_background(float(self.box_bg.text()))

        self.context.update_sim_algorithm(self.cbox_sim_algorithm.currentText())

    def make_connections(self):
        self.box_motor_pos.checkVal.connect(self.context.update_motor_position)
        self.box_percent_drop.checkVal.connect(self.context.update_dropped_shots)
        self.box_int.checkVal.connect(self.context.update_peak_intensity)
        self.box_jet_radius.checkVal.connect(self.context.update_jet_radius)
        self.box_jet_center.checkVal.connect(self.context.update_jet_center)
        self.box_max_int.checkVal.connect(self.context.update_max_intensity)
        self.box_bg.checkVal.connect(self.context.update_background)

        self.cbox_sim_algorithm.currentTextChanged.connect(self.context.update_sim_algorithm)
        self.bttn_search.clicked.connect(self._start_search)

    def _start_search(self):
#        self.sim_status.start()
#        self._start()
        thread = threading.Thread(target=self._start, args=())
        thread.start()

#    def _enable_tracking(self):
#        self.update_tracking_status("enabled", green)
#        self.context.update_tracking(True)
#        self._start_motor()

#    def set_tracking_status(self, status, color):
#        self.lbl_tracking_status.setText(status)
#        self.lbl_tracking_status.setStyleSheet(f"\
#                background-color: {color};")
