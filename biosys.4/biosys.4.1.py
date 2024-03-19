import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from creatures import organism, pos

app = pg.mkQApp("Plotting Example")

win = pg.GraphicsLayoutWidget(show=True, title="Basic Test")
win.resize(1000, 600)


# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p5 = win.addPlot(title="Scatter plot")
x = [0]
y = [0]

p5.showAxis('left', False)
p5.showAxis('right', False)
p5.showAxis('top', False)
p5.showAxis('bottom', False)
P = organism(6)
P.setPosition(pos(0, 0))
A = organism(5)
A.setPosition(pos(200, 500))
G = organism(1)
G.setPosition(pos(300, 200))


def plot_single_oganism(obj: organism):
    p5.plot([obj.getDatas()[0][0]], [obj.getDatas()[0][1]], pen=None, symbolPen=None, symbolSize=obj.getDatas()[1]/10, symbolBrush=obj.getDatas()[2])


def update():
    global A, G, P
    if A.getDatas()[4] and G.getDatas()[4]:
        A.catch(G)
        G.flee(A)
        P.catch(A)
        #P.catch(G)
        G.flee(P)
        A.flee(P)
    else:
        exit()
    p5.clear()
    p5.plot([0], [0], pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(255, 255, 255))
    p5.plot([500], [500], pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(255, 255, 255))
    plot_single_oganism(A)
    plot_single_oganism(G)
    plot_single_oganism(P)


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(200)

if __name__ == '__main__':
    pg.exec()
