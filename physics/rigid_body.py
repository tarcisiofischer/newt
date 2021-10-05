from geometry.polyhedron import Polyhedron
import numpy as np



class RigidBody(Polyhedron):

    def __init__(self, polyhedron=None):
        if polyhedron is not None:
            Polyhedron.__init__(self, polyhedron._points, polyhedron._faces)
        self.acceleration = np.array([0.0, 0.0, 0.0])  # m/s^2
        self.velocity = np.array([0.0, 0.0, 0.0])  # m/s
        self.angular_acceleration = np.array([0.0, 0.0, 0.0])  # deg/s^2
        self.angular_velocity = np.array([0.0, 0.0, 0.0])  # deg/s


    def update(self, delta_t):
        '''
        Forward delta_t time (in seconds) and update the rigid body variables.
        '''
        for i in range(len(self.acceleration)):
            self.velocity[i] += self.acceleration[i] * delta_t
            self.angular_velocity[i] += self.angular_acceleration[i] * delta_t

        self.move(self.velocity)
        self.rotate(self.angular_velocity)
