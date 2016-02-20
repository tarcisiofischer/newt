from geometry.polyhedron import Polyhedron
import numpy as np



#===================================================================================================
# ParticleGeometry
#===================================================================================================
class ParticleGeometry(Polyhedron):

    def __init__(self):
        Polyhedron.__init__(
            self,
            points=np.array([
                [1.0, 1.0, -1.0],
                [1.0, -1.0, 1.0],
                [-1.0, 1.0, 1.0],
            ]),
            faces=[[0, 1, 2]],
        )
        self.scale(np.array([0.02, 0.02, 0.02]))
