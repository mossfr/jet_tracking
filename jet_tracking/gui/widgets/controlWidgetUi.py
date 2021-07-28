from PyQt5.QtWidgets import QVBoxLayout, QButtonGroup, QRadioButton, QGridLayout, QHBoxLayout, QPushButton, QLCDNumber, \
    QFrame, QTextEdit

from jet_tracking.gui.widgets.basicWidgets import CollapsibleBox, Label, LineEdit, ComboBox


class Controls_Ui(object):

    def setupUi(self, obj):
        #####################################################################
        # set up user panel layout and give it a title
        #####################################################################
        obj.layout_usr_cntrl = QVBoxLayout(obj)
        obj.box_graph = CollapsibleBox("Graphing/Data collection")
        obj.layout_usr_cntrl.addWidget(obj.box_graph)

        #####################################################################
        # make radiobutton for selecting live or simulated data
        #####################################################################

        obj.bttngrp1 = QButtonGroup()

        obj.rdbttn_live = QRadioButton("live data")
        obj.rdbttn_sim = QRadioButton("simulated data")
        obj.rdbttn_live.setChecked(True)
        obj.bttngrp1.addButton(obj.rdbttn_live, id=1)
        obj.bttngrp1.addButton(obj.rdbttn_sim, id=0)
        obj.bttngrp1.setExclusive(True)

        obj.bttngrp3 = QButtonGroup()
        obj.rdbttn_cali_live = QRadioButton("calibration in GUI")
        obj.rdbttn_cali = QRadioButton("calibration from results")
        obj.rdbttn_cali.setChecked(True)
        obj.bttngrp3.addButton(obj.rdbttn_cali, id=0)
        obj.bttngrp3.addButton(obj.rdbttn_cali_live, id=1)
        obj.bttngrp3.setExclusive(True)

        # setup layout
        ##############
        obj.layout_graph = QVBoxLayout()
        obj.layout_allrdbttns = QGridLayout()
        obj.layout_allrdbttns.setColumnStretch(0, 1)
        obj.layout_allrdbttns.setColumnStretch(1, 1)
        obj.layout_allrdbttns.setColumnStretch(2, 1)
        obj.layout_allrdbttns.addWidget(obj.rdbttn_live, 0, 0)
        obj.layout_allrdbttns.addWidget(obj.rdbttn_sim, 0, 1)
        obj.layout_allrdbttns.addWidget(obj.rdbttn_cali, 1, 0)
        obj.layout_allrdbttns.addWidget(obj.rdbttn_cali_live, 1, 1)
        obj.layout_graph.addLayout(obj.layout_allrdbttns)

        #####################################################################
        # make input box for changing the percent of allowed values from the
        # mean and the number of points for averaging on the graph and the
        # refresh rate to update the points/graph
        #####################################################################

        obj.lbl_percent = Label("Percent \n(1 - 100)")
        obj.le_percent = LineEdit("70")
        obj.le_percent.valRange(1, 100)

        obj.lbl_ave_graph = Label('Averaging (graph) \n(5 - 300)')
        obj.lbl_refresh_rate = Label('Refresh Rate \n(2 - 300)')
        obj.le_ave_graph = LineEdit("50")
        obj.le_ave_graph.valRange(5, 300)
        obj.le_refresh_rate = LineEdit("50")
        obj.le_refresh_rate.valRange(2, 300)

        # setup layout
        ##############

        obj.layout_samp = QHBoxLayout()
        obj.layout_samp.addWidget(obj.lbl_percent)
        obj.layout_samp.addWidget(obj.le_percent)
        obj.layout_samp.addWidget(obj.lbl_ave_graph)
        obj.layout_samp.addWidget(obj.le_ave_graph)
        obj.layout_samp.addWidget(obj.lbl_refresh_rate)
        obj.layout_samp.addWidget(obj.le_refresh_rate)
        obj.layout_graph.addLayout(obj.layout_samp)
        obj.box_graph.setContentLayout(obj.layout_graph)

        ###################################################################
        #  make section for editing motor parameters
        ###################################################################

        obj.box_motor = CollapsibleBox("Motor Controls")
        obj.layout_usr_cntrl.addWidget(obj.box_motor)

        obj.bttngrp2 = QButtonGroup()
        obj.rdbttn_manual = QRadioButton("manual motor moving")
        obj.rdbttn_auto = QRadioButton("automated motor moving")
        obj.rdbttn_manual.setChecked(True)
        obj.bttngrp2.addButton(obj.rdbttn_manual, id=1)
        obj.bttngrp2.addButton(obj.rdbttn_auto, id=0)
        obj.bttngrp2.setExclusive(True)

        obj.lbl_motor_hl = Label("High Limit")
        obj.lbl_motor_ll = Label("Low Limit")
        obj.lbl_motor_size = Label("Step Size")
        obj.lbl_motor_average = Label("Average Intensity")
        obj.lbl_algorithm = Label("Algorithm")

        obj.le_motor_hl = LineEdit("50")
        obj.le_motor_hl.valRange(-100, 100)

        obj.le_motor_ll = LineEdit("-50")
        obj.le_motor_ll.valRange(-100, 100)

        obj.le_size = LineEdit(".5")
        obj.le_size.valRange(0, 100)

        obj.le_ave_motor = LineEdit("10")
        obj.le_ave_motor.valRange(1, 300)

        obj.cbox_algorithm = ComboBox()
        obj.cbox_algorithm.addItem("Ternary Search")
        obj.cbox_algorithm.addItem("Full Scan")

        obj.bttn_search = QPushButton()
        obj.bttn_search.setText("Search")
        obj.bttn_search.setEnabled(False)

        obj.bttn_tracking = QPushButton()
        obj.bttn_tracking.setText("Track")
        obj.bttn_tracking.setEnabled(False)

        obj.bttn_stop_motor = QPushButton()
        obj.bttn_stop_motor.setText("Stop Tracking")
        obj.bttn_stop_motor.setEnabled(False)

        obj.lbl_tracking = Label("Tracking")
        obj.lbl_tracking.setSubtitleStyleSheet()
        obj.lbl_tracking_status = Label("False")
        obj.lbl_tracking_status.setStyleSheet(f"\
                background-color: red;")

        obj.layout_motor = QVBoxLayout()
        obj.layout_motor_manual = QHBoxLayout()
        obj.layout_motor_input = QGridLayout()
        obj.layout_motor_bttns = QHBoxLayout()
        obj.layout_tracking = QHBoxLayout()
        obj.layout_motor.addLayout(obj.layout_motor_manual)
        obj.layout_motor.addLayout(obj.layout_motor_input)
        obj.layout_motor.addLayout(obj.layout_motor_bttns)
        obj.layout_motor_manual.addWidget(obj.rdbttn_manual)
        obj.layout_motor_manual.addWidget(obj.rdbttn_auto)
        obj.layout_motor_input.addWidget(obj.lbl_motor_ll, 0, 0)
        obj.layout_motor_input.addWidget(obj.le_motor_ll, 0, 1)
        obj.layout_motor_input.addWidget(obj.lbl_motor_hl, 0, 2)
        obj.layout_motor_input.addWidget(obj.le_motor_hl, 0, 3)
        obj.layout_motor_input.addWidget(obj.lbl_motor_size, 1, 0)
        obj.layout_motor_input.addWidget(obj.le_size, 1, 1)
        obj.layout_motor_input.addWidget(obj.lbl_motor_average, 1, 2)
        obj.layout_motor_input.addWidget(obj.le_ave_motor, 1, 3)
        obj.layout_motor_input.addWidget(obj.lbl_algorithm, 2, 0)
        obj.layout_motor_input.addWidget(obj.cbox_algorithm, 2, 1)
        obj.layout_motor_bttns.addWidget(obj.bttn_search)
        obj.layout_motor_bttns.addWidget(obj.bttn_tracking)
        obj.layout_motor_bttns.addWidget(obj.bttn_stop_motor)
        obj.box_motor.setContentLayout(obj.layout_motor)

        #####################################################################
        # give a status area that displays values and current tracking
        # reliability based on various readouts
        #####################################################################

        obj.lbl_status = Label("Status")
        obj.lbl_status.setTitleStylesheet()

        obj.lbl_monitor = Label("Monitor")
        obj.lbl_monitor.setSubtitleStyleSheet()
        obj.lbl_monitor_status = Label("Not Started")

        obj.lbl_tracking = Label("Tracking")
        obj.lbl_tracking.setSubtitleStyleSheet()
        obj.lbl_tracking_status = Label("False")
        obj.lbl_tracking_status.setStyleSheet(f"\
                background-color: red;")

        obj.lbl_i0 = Label("Mean Initial intensity (I0)")
        obj.lbl_i0_status = QLCDNumber(7)

        obj.lbl_diff_i0 = Label("Mean I/I0")
        obj.lbl_diff_status = QLCDNumber(7)

        # setup layout
        ##############
        obj.layout_usr_cntrl.addWidget(obj.lbl_status)

        obj.frame_monitor_status = QFrame()
        obj.frame_monitor_status.setLayout(QHBoxLayout())
        obj.frame_monitor_status.layout().addWidget(obj.lbl_monitor)
        obj.frame_monitor_status.layout().addWidget(obj.lbl_monitor_status)

        obj.frame_tracking_status = QFrame()
        obj.frame_tracking_status.setLayout(QHBoxLayout())
        obj.frame_tracking_status.layout().addWidget(obj.lbl_tracking)
        obj.frame_tracking_status.layout().addWidget(obj.lbl_tracking_status)

        obj.frame_i0 = QFrame()
        obj.frame_i0.setLayout(QHBoxLayout())
        obj.frame_i0.layout().addWidget(obj.lbl_i0)
        obj.frame_i0.layout().addWidget(obj.lbl_i0_status)

        obj.frame_diff_i0 = QFrame()
        obj.frame_diff_i0.setLayout(QHBoxLayout())
        obj.frame_diff_i0.layout().addWidget(obj.lbl_diff_i0)
        obj.frame_diff_i0.layout().addWidget(obj.lbl_diff_status)

        obj.layout_usr_cntrl.addWidget(obj.frame_monitor_status)
        obj.layout_usr_cntrl.addWidget(obj.frame_tracking_status)
        obj.layout_usr_cntrl.addWidget(obj.frame_i0)
        obj.layout_usr_cntrl.addWidget(obj.frame_diff_i0)
        ###############################

        ########################################################################
        # text area for giving updates the user can see
        ########################################################################

        obj.text_area = QTextEdit("~~~read only information for user~~~")
        obj.text_area.setReadOnly(True)
        obj.layout_usr_cntrl.addWidget(obj.text_area)

        #########################################################################
        # main buttons!!!!
        #########################################################################

        obj.bttn_calibrate = QPushButton("Calibrate")
        obj.bttn_calibrate.setStyleSheet("\
            background-color: yellow;\
            font-size:12px;\
            ")
        obj.bttn_start = QPushButton("Start")
        obj.bttn_start.setStyleSheet("\
            background-color: green;\
            font-size:12px;\
            ")
        obj.bttn_stop = QPushButton("Stop")
        obj.bttn_stop.setStyleSheet("\
            background-color: red;\
            font-size:12px;\
            ")

        # setup layout
        ##############
        obj.frame_jjbttns = QFrame()
        obj.frame_jjbttns.setLayout(QHBoxLayout())
        obj.frame_jjbttns.layout().addWidget(obj.bttn_calibrate)
        obj.frame_jjbttns.layout().addWidget(obj.bttn_start)
        obj.frame_jjbttns.layout().addWidget(obj.bttn_stop)

        obj.layout_usr_cntrl.addWidget(obj.frame_jjbttns)
