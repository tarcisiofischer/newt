import os

from readers.ply_reader import readPly
import numpy as np


def testReadPlyCube():
    current_path = os.path.dirname(os.path.abspath(__file__))
    expected_cube_points = np.loadtxt(current_path + "/test_ply_reader/expected_cube_points.txt")
    polyhedron = readPly(current_path + "/test_ply_reader/cube.ply")

    assert len(polyhedron.getFaces()) == 6
    assert len(polyhedron.getPoints()) == 24
    assert np.allclose(polyhedron.getPoints(), expected_cube_points)
