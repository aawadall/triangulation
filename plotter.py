"""responsible for plotting data from multiple sources"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Plotter(object):
    def __init__(self):
        self.fig = plt.figure()

    def draw_line(self, x, y, z, color=None):
        ax = Axes3D(self.fig)
        if color is None:
            ax.plot(x, y, z)
        else:
            ax.plot(x, y, z, c=color)

    def drw_scatter(self, x, y, z, color=None, marker=None):
        ax = Axes3D(self.fig)
        if color is None:
            if marker is None:
                ax.scatter(x, y, z)
            else:
                ax.scatter(x, y, z, marker=marker)
        else:
            if marker is None:
                ax.scatter(x, y, z, c=color)
            else:
                ax.scatter(x, y, z, marker=marker, c=color)

    @staticmethod
    def show():
        plt.show()

