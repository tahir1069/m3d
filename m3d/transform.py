import numpy as np


class Vector(object):
    def __init__(self, data=None):
        if isinstance(data, (list, tuple)):
            self._data = np.array(data)
        elif isinstance(data, np.ndarray):
            self._data = data
        elif data is None:
            self._data = np.array([0, 0, 0])
        else:
            raise ValueError()

    @property
    def x(self):
        return self._data[0]

    @x.setter
    def x(self, val):
        self._data[0] = val

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self, val):
        self._data[1] = val

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self, val):
        self._data[2] = val

    def __str__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)
    __repr__ = __str__

    @property
    def data(self):
        return self._data


class Orientation(object):
    def __init__(self, data=None):
        if isinstance(data, np.ndarray):
            self._data = data
        elif data is None:
            self._data = np.identity(3)
        else:
            raise ValueError()

    def rotate_zb(self, val):
        pass

    def __str__(self):
        return "Orientation({})".format(self.data)
    __repr__ = __str__

    @property
    def inverse(self):
        return Orientation(np.linalg.inv(self.data))
    
    @property
    def data(self):
        return self._data



class Transform(object):
    def __init__(self, orientation=None, vector=None):
        self.data = np.identity(4)
        if orientation is None:
            pass
        elif isinstance(orientation, np.ndarray):
            self.data[:3, :3] = orientation
        elif isinstance(orientation, Orientation):
            self.data[:3, :3] = orientation.data
        else:
            raise ValueError("orientation argument should be a numpy array, Orientation or None")
        self._orient = Orientation(self.data[:3, :3])

        if vector is None:
            pass
        elif isinstance(vector, np.ndarray):
            self.data[:3, 3] = vector
        elif isinstance(vector, Vector):
            self.data[:3, 3] = vector.data
        else:
            raise ValueError("orientation argument should be a numpy array, Orientation or None")
        self._pos = Vector(self.data[:3, 3])

    def __str__(self):
        return "Transform(\n{},\n{}\n)".format(self.orient, self.pos)
    __repr__ = __str__

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, vector):
        self.data[:3, 3] = vector.data
        self._pos = Vector(self.data[:3, 3])

    @property
    def orient(self):
        return self._orient

    @orient.setter
    def orient(self, orient):
        self.data[:, 3] = orient.data
        self._pos = Orientation(self.data[:, 3])

    @property
    def inverse(self):
        return Transform(np.linalg.inv(self.orient.data), -self.pos.data)

    def __eq__(self):
        raise NotImplementedError


