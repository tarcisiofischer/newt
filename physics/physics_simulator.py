class PhysicsSimulator:
    def __init__(self):
        self._bodies = []
        self._force_generators = []

    def addForceGenerator(self, generator):
        self._force_generators.append(generator)

    def addBody(self, body):
        self._bodies.append(body)

    def update(self, delta_t):
        for generator in self._force_generators:
            generator.update()

        for body in self._bodies:
            body.update(delta_t)
            body.resetForceAccumulator()
