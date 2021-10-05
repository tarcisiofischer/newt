import os

from readers.ply_reader import readPly
import numpy as np


def getTestFile(filename):
    """
    :param unicode filename:
    """
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path + "/test_polyhedron/" + filename


def testMovePolyhedron():
    expected_points = np.loadtxt(getTestFile("expected_moved_points.txt"))
    polyhedron = readPly(getTestFile("small_sphere.ply"))
    polyhedron.move(np.array([1.0, 2.0, 3.0]))
    assert np.allclose(polyhedron.getPoints(), expected_points)


def testRotatePolyhedron():
    expected_points = np.loadtxt(getTestFile("expected_rotated_points.txt"))
    polyhedron = readPly(getTestFile("cube.ply"))
    polyhedron.rotate(np.array([45.0, 45.0, 45.0]))
    assert np.allclose(polyhedron.getPoints(), expected_points)
