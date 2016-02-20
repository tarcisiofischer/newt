from geometry.particle_geometry import ParticleGeometry
import numpy as np


#===============================================================================
# Particle
#===============================================================================
class Particle(object):

    def __init__(self, mass=1e-8):
        '''
        :param float mass:
            The particle mass, in kilograms [kg].
        '''
        self.mass = mass  # [kg]
        self.velocity = np.array([0.0, 0.0, 0.0])  # m/s
        self.position = np.array([0.0, 0.0, 0.0])  # m
        self.force_accumulator = np.array([0.0, 0.0, 0.0])
        self.setGeometry(ParticleGeometry())


    def setGeometry(self, geometry):
        self.geometry = geometry
        self.geometry._position = self.position


    def setPosition(self, position):
        self.position[:] = position


    def resetForceAccumulator(self):
        '''
        Resets the current force accumulator. This method is meant to be called from the physics
        simulator, after one timestep ends.
        '''
        self.force_accumulator = np.array([0.0, 0.0, 0.0])


    def update(self, delta_t):
        '''
        Also known as "integrator", this method is used to update particle's variables in each
        simulation step.

        :param float delta_t:
        '''
        acceleration = self.force_accumulator * 1.0 / self.mass
        self.velocity += acceleration * delta_t
        self.position += self.velocity * delta_t
