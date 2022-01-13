# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MplWidget(QWidget):

    def __init__(self, parent=None):


        QWidget.__init__(self, parent)
        self.figure = plt.figure()
        #self.MplWidget.canvas.pausar=plt.pause(0.01)
        #self.mat=plt.pause()
        self.style= plt.style.use('dark_background')

        self.figure.set_facecolor("black")
        self.canvas = FigureCanvas(self.figure)


        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)


        self.canvas.axes = self.canvas.figure.add_subplot(211)
        self.canvas.axes.spines['top'].set_visible(False)
        self.canvas.axes.spines['right'].set_visible(False)
        self.canvas.axes.spines['bottom'].set_visible(False)
        self.canvas.axes.spines['left'].set_visible(False)
        self.canvas.axes.get_yaxis().set_visible(False)
        self.canvas.axes.get_xaxis().set_visible(False)

        self.canvas.axes2 = self.canvas.figure.add_subplot(212)
        self.canvas.axes2.spines['top'].set_visible(False)
        self.canvas.axes2.spines['right'].set_visible(False)
        self.canvas.axes2.spines['bottom'].set_visible(False)
        self.canvas.axes2.spines['left'].set_visible(False)
        self.canvas.axes2.get_yaxis().set_visible(False)
        self.canvas.axes2.get_xaxis().set_visible(False)

        self.canvas.limite=self.canvas.figure.subplots_adjust(left=0, bottom=.1, right=1, top=0.9, wspace=None, hspace=0.2)
        #self.canvas.axes.grid()
        self.setLayout(vertical_layout)
