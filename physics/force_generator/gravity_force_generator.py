import numpy as np
from physics.force_generator.force_generator import ForceGenerator


class GravityForceGenerator(ForceGenerator):

    G = np.array([0.0, -9.8, 0.0])  # [m/s]

    def __init__(self, obj):
        self._obj = obj

    def setGravity(self, new_gravity):
        """
        :param np.array(shape=(3,), dtype=np.float64) new_gravity:
        """
        self.G = new_gravity

    def update(self):
        self._obj.force_accumulator += self.G * self._obj.mass
