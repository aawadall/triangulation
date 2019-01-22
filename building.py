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

        # Base 0,0
        px = 0
        py = 0
        pz = 0
        x.append(px)
        y.append(py)
        z.append(pz)

        # Col 0
        pz += self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        pz -= self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Base x+
        px += self.scale[0]
        x.append(px)
        y.append(py)
        z.append(pz)

        # col 1
        pz += self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        pz -= self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Base y+
        py += self.scale[1]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Col 2
        pz += self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        pz -= self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Base x-
        px -= self.scale[0]
        x.append(px)
        y.append(py)
        z.append(pz)

        #Col 3
        pz += self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        pz -= self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Base y-
        py -= self.scale[1]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Go up
        pz += self.scale[2]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Ceiling
        px += self.scale[0]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Base y+
        py += self.scale[1]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Base x-
        px -= self.scale[0]
        x.append(px)
        y.append(py)
        z.append(pz)

        # Base y-
        py -= self.scale[1]
        x.append(px)
        y.append(py)
        z.append(pz)
        return ax.plot3D(x, y, z, c='black')


