from gui.input_listeners.game_like_input_listener import GameLikeInputListener
from gui.main_window import MainWindow
from gui.paintables.paintable_connector import PaintableConnector
from gui.paintables.paintable_polyhedron import PaintablePolyhedron
from physics.force_generator.spring_force_generator import SpringForceGenerator
from physics.particle import Particle
from physics.physics_simulator import PhysicsSimulator
from readers.ply_reader import readPly
import numpy as np
import os


def createParticle(mass, color):
    particle = Particle(mass)
    current_path = os.path.dirname(os.path.abspath(__file__))
    particle.setGeometry(readPly(f"{current_path}/objects/sphere.ply"))
    particle.geometry.scale(np.repeat(mass / 2.0, 3))
    particle.geometry.setColor(color)
    return particle


if __name__ == "__main__":
    main_window = MainWindow("Spring Example", 400, 400)
    main_window.setInputListener(GameLikeInputListener(main_window))

    simulator = PhysicsSimulator()

    particle1 = createParticle(0.1, np.array([0.6, 0.2, 0.6]))
    particle2 = createParticle(0.5, np.array([0.2, 0.6, 0.6]))
    particle3 = createParticle(0.2, np.array([0.8, 0.2, 0.2]))

    simulator.addBody(particle1)
    simulator.addBody(particle2)
    simulator.addBody(particle3)

    main_window.addObject(PaintablePolyhedron(particle1.geometry))
    main_window.addObject(PaintablePolyhedron(particle2.geometry))
    main_window.addObject(PaintablePolyhedron(particle3.geometry))
    main_window.addObject(PaintableConnector(particle1, particle2))
    main_window.addObject(PaintableConnector(particle2, particle3))
    main_window.addObject(PaintableConnector(particle1, particle3))

    # Re-position particles for simulation
    # Particle1 is the fix particle (Will not have gravity)
    particle1.setPosition(np.array([-0.5, 0.5, 7.5]))
    # Particle2 is the moving particle (Will have the gravity force changing it)
    particle2.setPosition(np.array([0.5, -0.5, 7.0]))
    particle3.setPosition(np.array([0.5, 0.5, 6.0]))

    # Finally, add forces
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle2, 1.5, 5.0))
    simulator.addForceGenerator(SpringForceGenerator(particle2, particle3, 1.5, 1.0))
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle3, 1.2, 2.0))

    main_window.addBeforeDrawSceneCallback(simulator.update)
    main_window.mainLoop()
