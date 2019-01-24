"""responsible for plotting data from multiple sources"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Line(object):
    def __init__(self, x, y, z, color):
        self.x=x
        self.y=y
        self.z=z
        self.color=color


class Scatters(object):
    def __init__(self, x, y, z, color, marker):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.marker=marker

class Plotter(object):
    def __init__(self):
        self.fig = plt.figure()
        self.lines = []
        self.scatters = []
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
        scatter = Scatters(x, y, z, color, marker)
        self.scatters.append(scatter)

        ax = Axes3D(self.fig)

        for s in self.scatters:
            if s.color is None:
                if s.marker is None:
                    ax.scatter(s.x, s.y, s.z)
                else:
                    ax.scatter(s.x, s.y, s.z, marker=s.marker)
            else:
                if s.marker is None:
                    ax.scatter(s.x, s.y, s.z, c=s.color)
                else:
                    ax.scatter(s.x, s.y, s.z, marker=s.marker, c=s.color)

    def show(self):
        plt.show(self.fig)

