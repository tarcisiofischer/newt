import math

from geometry.utils import boundingBox
import numpy as np


class Polyhedron(object):

    def __init__(self, points, faces):
        '''
        :param np.array(dtype=float, shape=(n,3)) points:
        :param list(list(int)) faces:
            List of faces. Each face is represented as a list of points.
            Note that this approach enables non-convex polyhedrons
            representation, but it is probably not a good idea to use them, as
            some algorithms doesn't support it.
        '''
        self._faces = faces
        self._points = points
        self._color = np.array([0.0, 0.0, 0.0])
        self._position = np.array([0.0, 0.0, 0.0])


    def setColor(self, color):
        self._color = color


    def getColor(self):
        return self._color


    def scale(self, amount):
        '''
        :param np.array(dtype=np.float64, shape=(3,)) amount:
        '''
        self._points *= amount


    def move(self, amount):
        '''
        :param np.array(dtype=np.float64, shape=(3,)) amount:
        '''
        self._points += amount


    def rotate(self, angles):
        '''
        :param np.array(dtype=np.float64, shape=(3,)) angles:
        '''
        cos = math.cos
        sin = math.sin
        theta = angles[0]
        Rx = np.array([
            [1.0, 0.0, 0.0],
            [0.0, cos(theta), -sin(theta)],
            [0.0, sin(theta), cos(theta)],
        ])
        theta = angles[1]
        Ry = np.array([
            [cos(theta), 0.0, sin(theta)],
            [0.0, 1.0, 0.0],
            [-sin(theta), 0.0, cos(theta)],
        ])
        theta = angles[2]
        Rz = np.array([
            [cos(theta), -sin(theta), 0.0],
            [sin(theta), cos(theta), 0.0],
            [0.0, 0.0, 1.0],
        ])
        original_position = self.getCenterOfMass()

        # TODO: Is it possible to compute all rotations and translations once?
        self.move(-original_position)
        rotation_matrix = np.dot(Rx, Ry)
        rotation_matrix = np.dot(rotation_matrix, Rz)
        # TODO: Is it possible to do this for all points at once?
        for i in range(len(self._points)):
            self._points[i] = np.dot(rotation_matrix, self._points[i])
        self.move(original_position)


    def getCenterOfMass(self):
        '''
        :returns np.array(dtype=np.float64, shape=(3,)):
        '''
        # TODO: Calculate the real center of mass. Today's implementation gives
        # the geometric center...
        xmin, xmax, ymin, ymax, zmin, zmax = boundingBox(self)
        return np.array([
            (xmin + xmax) / 2.0,
            (ymin + ymax) / 2.0,
            (zmin + zmax) / 2.0
        ])


    def getFaces(self):
        '''
        :returns list(list(int)):
        '''
        return self._faces


    def getPoints(self):
        '''
        :returns np.array(dtype=np.float64, shape=(n, 3)):
        '''
        return self._points + self._position


    def getPoint(self, point_id):
        '''
        :param int point_id:
        :returns np.array(dtype=np.float64, shape=(3,)):
        '''
        return self._points[point_id] + self._position
