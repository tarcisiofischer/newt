from OpenGL.GL import *
from itertools import izip


class PaintablePolyhedron(object):

    def __init__(self, polyhedron=None):
        self._color = (1.0, 0.0, 0.0)
        self._polyhedron = polyhedron


    def setPolyhedron(self, polyhedron):
        self._polyhedron = polyhedron


    def setColor(self, r, g, b):
        self._color = (r, g, b)


    def paint(self):
        for face in self._polyhedron.getFaces():
            glColor3f(*self._color)
            glBegin(GL_POLYGON)
            for point_id in face:
                x, y, z = self._polyhedron.getPoint(point_id)
                glVertex3f(x, y, z)
            glEnd()

            glLineWidth(1.0)
            glColor3f(0.0, 0.0, 0.0)
            x, y, z = self._polyhedron.getPoint(face[-1])
            glVertex3f(x, y, z)
            for point_id, next_point_id in izip(face, face[1:] + [face[0]]):
                glBegin(GL_LINES)
                x, y, z = self._polyhedron.getPoint(point_id)
                glVertex3f(x, y, z)
                x, y, z = self._polyhedron.getPoint(next_point_id)
                glVertex3f(x, y, z)
                glEnd()

