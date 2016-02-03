from OpenGL.GL import GL_TRIANGLES, glBegin, glColor3f, glVertex3f, glEnd

class PaintableParticle(object):

    def setParticle(self, particle):
        self._particle = particle
        self._size = 0.02


    def paint(self):
        tx, ty, tz = self._particle.position

        glBegin(GL_TRIANGLES)
        glColor3f(0.0, 0.0, 0.6)

        glVertex3f(self._size + tx, self._size + ty, -self._size + tz)
        glVertex3f(self._size + tx, -self._size + ty, self._size + tz)
        glVertex3f(-self._size + tx, self._size + ty, self._size + tz)

        glEnd()
