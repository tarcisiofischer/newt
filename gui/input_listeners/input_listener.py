class InputListener(object):
    """
    Interface for input listener
    """

    def onMouseMove(self, x, y):
        """
        :param int x:
        :param int y:
        """

    def onMouseEvent(self, mouse_button, mouse_event, x, y):
        """
        :param int mouse_button:
            ..see: mouse_constants.py module
        :param int mouse_event:
            ..see: mouse_constants.py module
        :param int x:
        :param int y:
        """

    def onKeyPress(self, key, x, y):
        """
        :param str key:
        :param int x:
        :param int y:
        """

    def onKeyRelease(self, key, x, y):
        """
        :param str key:
        :param int x:
        :param int y:
        """
