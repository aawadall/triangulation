"""Building on fire behaviour"""
from mpl_toolkits.mplot3d import axes3d, Axes3D


class Building(object):
    def __init__(self, scale):
        self.scale = scale

    def draw(self, fig):
        ax = Axes3D(fig)
        x = []
        y = []
        z = []
        for x_idx in range(2):
            for y_idx in range(2):
                for z_idx in range(2):
                    x.append(x_idx * self.scale[0])
                    y.append(y_idx * self.scale[1])
                    z.append(z_idx * self.scale[2])
        return ax.plot3D(x, y, z, c='black')


