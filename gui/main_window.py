from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from physics.delta_t_calculators import DefaultDeltaTCalculator


#===================================================================================================
# MainWindow
#===================================================================================================
class MainWindow(object):

    def __init__(self, title, width, height):
        self._initWindow(title, width, height)

        # To override the delta_t calculator, simply override this public member
        self.calculateDeltaT = DefaultDeltaTCalculator()

        self._before_draw_scene = []
        self._after_draw_scene = []

        self.rotation_x = 0.0
        self.rotation_y = 0.0
        self.rotation_z = 0.0
        self.translation_x = 0.0
        self.translation_y = 0.0
        self.translation_z = -10.0
        self._paintables = []

        glutDisplayFunc(self._drawScene)
        glutIdleFunc(self._drawScene)

        glClearColor(0.8, 0.8, 0.8, 0.0)
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.0, 0.1, 999.0)
        glMatrixMode(GL_MODELVIEW)


    def setInputListener(self, listener):
        glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
        glutKeyboardFunc(listener.onKeyPress)
        glutKeyboardUpFunc(listener.onKeyRelease)
        glutMotionFunc(listener.onMouseMove)
        glutPassiveMotionFunc(listener.onMouseMove)
        glutMouseFunc(listener.onMouseEvent)


    def mainLoop(self):
        glutMainLoop()


    def addObject(self, paintable_object):
        assert 'paint' in dir(paintable_object), \
            "paintable_object must implement 'paint' method"
        self._paintables.append(paintable_object)


    def addBeforeDrawSceneCallback(self, callback):
        self._before_draw_scene.append(callback)


    def addAfterDrawSceneCallback(self, callback):
        self._after_draw_scene.append(callback)


    def _initWindow(self, title, width, height):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        glutCreateWindow(title)


    def _drawScene(self):
        delta_t = self.calculateDeltaT()
        for callback in self._before_draw_scene:
            callback(delta_t)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(self.rotation_y, 1.0, 0.0, 0.0)
        glRotatef(self.rotation_x, 0.0, 1.0, 0.0)
        glRotatef(self.rotation_z, 0.0, 0.0, 1.0)
        glTranslatef(self.translation_x, self.translation_y, self.translation_z)

        for obj in self._paintables:
            obj.paint()

        glutSwapBuffers()
        for callback in self._after_draw_scene:
            callback(delta_t)
