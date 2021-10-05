import math
from physics.force_generator.force_generator import ForceGenerator

import numpy as np


class SpringForceGenerator(ForceGenerator):
    """
        A SpringForceGenerator has two ends, one in each side of the spring, like in the
        representation below:

        obj_a~~~~~~~~~~~obj_b

        The two objects will be updated by this force generator.
        The force is calculated from the hook's law:

        f = -k * dl

        where

        k = Spring constant
        dl = The distance the spring is extended or compressed

        In 3D, dl can be written as:

        dl = (md - l0) * ud

        where

        md = |d| = sqrt(x ** 2 + y ** 2 + z ** 2)  (Magnitude of d)
        l0 = The spring's natural length. Also called "rest length".
        ud = d / |d|  (unit-length direction of d)
        d = xa - xb  (Position of obj_a - position of obj_b)

        Reference: Game Physics Engine Development - Millington, Ian. 2007.
    """

    def __init__(self, obj_a, obj_b, rest_length, spring_constant):
        """
        :param object obj_a:
        :param object obj_b:
        """
        self.obj_a = obj_a
        self.obj_b = obj_b
        self.rest_length = rest_length
        self.spring_constant = spring_constant

    def _updateHelper(self, a, b):
        """
        Helper method to update all objects. See the formulas in the above documentation for
        details.

        :param object a:
        :param object b:
        """
        k = self.spring_constant
        d = a.position - b.position
        md = math.sqrt(np.sum(d ** 2))
        l0 = self.rest_length
        ud = d / md
        dl = (md - l0) * ud
        f = -k * dl
        a.force_accumulator += f

    def update(self):
        self._updateHelper(self.obj_a, self.obj_b)
        self._updateHelper(self.obj_b, self.obj_a)
