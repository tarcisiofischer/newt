import unittest
from readers.ply_reader import readPly


class Test(unittest.TestCase):


    def testReadPlyCube(self):
        polyhedron = readPly("cube.ply")
        self.assertEqual(len(polyhedron.getFaces()), 6)
        self.assertEqual(polyhedron.getPoint(0), [1.0, 1.0, -1.0])


if __name__ == "__main__":
    unittest.main()
