"""responsible for plotting data from multiple sources"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Plotter(object):
    def __init__(self):
        self.fig = plt.figure()
        self.ax = []

    def draw_line(self, x, y, z, color=None):
        self.ax.append(Axes3D(self.fig))
        if color is None:
            self.ax[-1].plot3D(x, y, z)
        else:
            self.ax[-1].plot3D(x, y, z, c=color)

    def drw_scatter(self, x, y, z, color=None, marker=None):
        self.ax.append(Axes3D(self.fig))
        if color is None:
            if marker is None:
                self.ax[-1].scatter(x, y, z)
            else:
                self.ax[-1].scatter(x, y, z, marker=marker)
        else:
            if marker is None:
                self.ax[-1].scatter(x, y, z, c=color)
            else:
                self.ax[-1].scatter(x, y, z, marker=marker, c=color)

    def show(self):
        plt.show(self.fig)

