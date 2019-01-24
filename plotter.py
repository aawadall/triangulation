"""responsible for plotting data from multiple sources"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Line(object):
    def __init__(self, x, y, z, color):
        self.x=x
        self.y=y
        self.z=z
        self.color=color


class Plotter(object):
    def __init__(self):
        self.fig = plt.figure()
        self.lines = []

    def draw_line(self, x, y, z, color=None):
        line = Line(x, y, z, color)
        self.lines.append(line)
        ax = Axes3D(self.fig)
        for l in self.lines:
            if l.color is None:
                ax.plot3D(l.x, l.y, l.z)
            else:
                ax.plot3D(l.x, l.y, l.z, c=l.color)

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

    def show(self):
        plt.show(self.fig)

