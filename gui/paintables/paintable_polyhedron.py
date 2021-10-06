from OpenGL.GL import *


class PaintablePolyhedron:
    def __init__(self, polyhedron=None, draw_outline=False):
        self._polyhedron = polyhedron
        self._draw_outline = draw_outline

    def setPolyhedron(self, polyhedron):
        self._polyhedron = polyhedron

    def paint(self):
        for face in self._polyhedron.getFaces():
            glColor3f(*self._polyhedron.getColor())
            glBegin(GL_POLYGON)
            for point_id in face:
                x, y, z = self._polyhedron.getPoint(point_id)
                glVertex3f(x, y, z)
            glEnd()

            if self._draw_outline:
                glLineWidth(1.0)
                glColor3f(0.0, 0.0, 0.0)
                x, y, z = self._polyhedron.getPoint(face[-1])
                glVertex3f(x, y, z)
                for (point_id, next_point_id) in zip(face, face[1:] + [face[0]]):
                    glBegin(GL_LINES)
                    x, y, z = self._polyhedron.getPoint(point_id)
                    glVertex3f(x, y, z)
                    x, y, z = self._polyhedron.getPoint(next_point_id)
                    glVertex3f(x, y, z)
                    glEnd()
