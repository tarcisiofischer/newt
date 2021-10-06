import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import deg2rad

from gui.input_listeners.mouse_constants import (
    MOUSE_BUTTON_PRESSED,
    MOUSE_BUTTON_LEFT,
    MOUSE_BUTTON_RIGHT,
)


class RotateHelper:
    def __init__(self):
        self.xc = 200
        self.yc = 200
        self.max_rotation = 20

    def __call__(self, x, y, w):
        delta_x = x - self.xc
        delta_y = y - self.yc

        if delta_x == 0 and delta_y == 0:
            return

        w.rotation_x += delta_x * 0.2
        if w.rotation_y < self.max_rotation and w.rotation_y > -self.max_rotation:
            w.rotation_y += delta_y * 0.2
        elif w.rotation_y < self.max_rotation and delta_y > 0:
            w.rotation_y += delta_y * 0.2
        elif w.rotation_y > -self.max_rotation and delta_y < 0:
            w.rotation_y += delta_y * 0.2

        glutWarpPointer(self.xc, self.yc)


class MoveHelper:
    def __init__(self):
        self._theta = 90.0
        self.moving_left = False
        self.moving_right = False
        self.moving_forward = False
        self.moving_backward = False

    def onPress(self, key):
        if key == "a":
            self.moving_left = True
        elif key == "d":
            self.moving_right = True
        elif key == "w":
            self.moving_forward = True
        elif key == "s":
            self.moving_backward = True

    def onRelease(self, key):
        if key == "a":
            self.moving_left = False
        elif key == "d":
            self.moving_right = False
        elif key == "w":
            self.moving_forward = False
        elif key == "s":
            self.moving_backward = False

    def updateCamera(self, w):
        theta = 90.0 + w.rotation_x
        if self.moving_left:
            w.translation_x += 0.1 * math.cos(deg2rad(theta - 90.0))
            w.translation_z += 0.1 * math.sin(deg2rad(theta - 90.0))
        if self.moving_right:
            w.translation_x += 0.1 * math.cos(deg2rad(theta + 90.0))
            w.translation_z += 0.1 * math.sin(deg2rad(theta + 90.0))
        if self.moving_forward:
            w.translation_x += 0.1 * math.cos(deg2rad(theta))
            w.translation_z += 0.1 * math.sin(deg2rad(theta))
        if self.moving_backward:
            w.translation_x += 0.1 * math.cos(deg2rad(theta + 180.0))
            w.translation_z += 0.1 * math.sin(deg2rad(theta + 180.0))


class GameLikeInputListener:
    def __init__(self, main_window):
        self._main_window = main_window
        self._is_interacting = False
        self._rotate_helper = RotateHelper()
        self._move_helper = MoveHelper()
        update_camera = lambda *args, **kwargs: self._move_helper.updateCamera(
            main_window
        )
        main_window.addBeforeDrawSceneCallback(update_camera)

    def onMouseMove(self, x, y):
        if self._is_interacting:
            self._rotate_helper(x, y, self._main_window)

    def onMouseEvent(self, mouse_button, mouse_event, x, y):
        if mouse_event == MOUSE_BUTTON_PRESSED:
            if mouse_button == MOUSE_BUTTON_LEFT:
                self._is_interacting = True
                glutSetCursor(GLUT_CURSOR_NONE)
                glutWarpPointer(self._rotate_helper.xc, self._rotate_helper.yc)
            if mouse_button == MOUSE_BUTTON_RIGHT:
                self._is_interacting = False
                glutSetCursor(GLUT_CURSOR_INHERIT)

    def onKeyPress(self, key, x, y):
        self._move_helper.onPress(key)

    def onKeyRelease(self, key, x, y):
        self._move_helper.onRelease(key)
