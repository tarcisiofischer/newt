from OpenGL.GL import GL_LINES, glBegin, glColor3f, glVertex3f, glEnd, glLineWidth


class PaintableConnector:
    def __init__(self, obj_a, obj_b):
        self.obj_a = obj_a
        self.obj_b = obj_b

    def paint(self):
        glColor3f(0.0, 0.0, 0.6)
        glLineWidth(1.0)
        glBegin(GL_LINES)
        glVertex3f(*self.obj_a.position)
        glVertex3f(*self.obj_b.position)
        glEnd()
