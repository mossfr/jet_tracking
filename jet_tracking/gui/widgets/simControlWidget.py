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

        self.context.update_ave_time(float(self.box_ave_time.text()))
        self.context.update_left(float(self.box_left.text()))
        self.context.update_right(float(self.box_right.text()))
        self.context.update_step(float(self.box_step.text()))
        self.context.update_sim_tol(float(self.box_sim_tol.text()))
        self.context.update_thresh(float(self.box_thresh.text()))
        self.context.update_wait(float(self.box_wait.text()))

    def make_connections(self):
        self.box_motor_pos.checkVal.connect(self.context.update_motor_position)
        self.box_percent_drop.checkVal.connect(self.context.update_dropped_shots)
        self.box_int.checkVal.connect(self.context.update_peak_intensity)
        self.box_jet_radius.checkVal.connect(self.context.update_jet_radius)
        self.box_jet_center.checkVal.connect(self.context.update_jet_center)
        self.box_max_int.checkVal.connect(self.context.update_max_intensity)
        self.box_bg.checkVal.connect(self.context.update_background)

        self.box_ave_time.checkVal.connect(self.context.update_ave_time)
        self.box_left.checkVal.connect(self.context.update_left)
        self.box_right.checkVal.connect(self.context.update_right)
        self.box_step.checkVal.connect(self.context.update_step)
        self.box_sim_tol.checkVal.connect(self.context.update_sim_tol)
        self.box_thresh.checkVal.connect(self.context.update_thresh)
        self.box_wait.checkVal.connect(self.context.update_wait)

        self.cbox_sim_algorithm.currentTextChanged.connect(self.context.update_sim_algorithm)
        self.bttn_search.clicked.connect(self._start_search)
        self.bttn_start_tracking.clicked.connect(self._start_tracking)
        self.bttn_stop_tracking.clicked.connect(self._stop_tracking)

    def _start_search(self):
#        self.sim_status.start()
#        self._start()
        thread = threading.Thread(target=self._start, args=())
        thread.start()

    def _start_tracking(self):
#        self.update_tracking_status("enabled", green)
        self.context.update_sim_tracking(True)
#        self.set_tracking_status('Tracking', 'green')
#        self.sim_tracking()
        print("started tracking")
        thread2 = threading.Thread(target=self.sim_tracking, args=())
        thread2.start()

    def _stop_tracking(self):
#        self.update_tracking_status("disabled", red)
        self.context.update_sim_tracking(False)
        print("stopped tracking")

#    def set_tracking_status(self, status, color):
#        self.lbl_tracking_status.setText(status)
#        self.lbl_tracking_status.setStyleSheet(f"\
#                background-color: {color};")
