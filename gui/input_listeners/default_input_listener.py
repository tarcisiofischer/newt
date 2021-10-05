from gui.input_listeners.input_listener import InputListener
from gui.input_listeners.mouse_constants import *


class DefaultInputListener(InputListener):
    def __init__(self):
        self._mouse_state = MOUSE_STATE_NONE
        self._mouse_move_position = None

    def setMainWindow(self, main_window):
        self._main_window = main_window

    def onMouseMove(self, x, y):
        if self._mouse_state == MOUSE_STATE_ROTATING:
            if self._mouse_move_position is not None:
                self._main_window.rotation_x += x - self._mouse_move_position[0]
                self._main_window.rotation_y += y - self._mouse_move_position[1]
            self._mouse_move_position = [x, y]
        elif self._mouse_state == MOUSE_STATE_TRANSLATING:
            self._main_window.translation_x += (
                x - self._mouse_move_position[0]
            ) / 100.0
            self._main_window.translation_y -= (
                y - self._mouse_move_position[1]
            ) / 100.0
            self._mouse_move_position = [x, y]
        elif self._mouse_state == MOUSE_STATE_Z_ROTATING:
            if self._mouse_move_position is not None:
                self._main_window.rotation_z += y - self._mouse_move_position[1]
            self._mouse_move_position = [x, y]

    def onMouseEvent(self, mouse_button, mouse_event, x, y):
        if mouse_event == MOUSE_BUTTON_PRESSED:
            if mouse_button == MOUSE_BUTTON_LEFT:
                self._mouse_state = MOUSE_STATE_ROTATING
                self._mouse_move_position = None
            elif mouse_button == MOUSE_BUTTON_MIDDLE:
                self._mouse_state = MOUSE_STATE_Z_ROTATING
                self._mouse_move_position = None
            elif mouse_button == MOUSE_BUTTON_RIGHT:
                self._mouse_state = MOUSE_STATE_TRANSLATING
                self._mouse_move_position = [x, y]
            elif mouse_button == MOUSE_WHEEL_UP:
                self._translation_z += 10.0
            elif mouse_button == MOUSE_WHEEL_DOWN:
                self._translation_z -= 10.0
        elif mouse_event == MOUSE_BUTTON_RELEASED:
            self._mouse_state = MOUSE_STATE_NONE
