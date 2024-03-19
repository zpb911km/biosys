import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtWidgets

app = pg.mkQApp("Scatter Plot")

win = pg.GraphicsLayoutWidget(show=True)  ## GraphicsView with GraphicsLayout inserted by default

win.setWindowTitle('Biosys Simulator')


w1 = win.addPlot()
w1.setLabel('top')
w1.setLabel('left')
w1.setLabel('right')
w1.setLabel('bottom')

s1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(0, 255, 0), brush=pg.mkBrush(255, 255, 255))
spots = [{'pos': [0, 0]}]
s1.addPoints(spots)
w1.addItem(s1)

s2 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(0, 0, 255), brush=pg.mkBrush(255, 0, 0))
spots = [{'pos': [0, 1]}]
s2.addPoints(spots)
w1.addItem(s2)

if __name__ == '__main__':
    pg.exec()
