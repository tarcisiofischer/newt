from physics.particle import Particle
import numpy as np


class ParticleArray:
    """
    A bunch of particles that will be calculated together.
    This class is meant to be more performant than the single particle implementation ..see: Particle
    """

    def __init__(self, mass=1e-8, number_of_particles=100):
        """
        :param float mass:
            The particle mass, in kilograms [kg].

        :param int number_of_particles:
            The number os particles in the particle array. All particles will
            have the same mass.
        """
        self.mass = mass  # [kg]
        self.velocity = np.zeros(dtype=np.float, shape=(number_of_particles, 3))  # m/s
        self.position = np.zeros(dtype=np.float, shape=(number_of_particles, 3))  # m
        self.force_accumulator = np.array([0.0, 0.0, 0.0])
        self.number_of_particles = number_of_particles

    def getReadOnlyParticle(self, i):
        """
        Get a single particle (a view in the numpy array structures).
        The particle is READ ONLY, that is, it is not expected to be changed.

        :param int i:
            The particle index in the array.
        """
        p = Particle()
        p.mass = self.mass
        p.velocity = self.velocity[i]
        p.position = self.position[i]
        p.geometry._position = p.position
        return p

    def resetForceAccumulator(self):
        """
        Resets the current force accumulator. This method is meant to be called from the physics
        simulator, after one timestep ends.
        """
        self.force_accumulator = np.array([0.0, 0.0, 0.0])

    def update(self, delta_t):
        """
        Also known as "integrator", this method is used to update particle's variables in each
        simulation step.

        :param float delta_t:
        """
        acceleration = self.force_accumulator * 1.0 / self.mass
        self.velocity += acceleration * delta_t
        self.position += self.velocity * delta_t
