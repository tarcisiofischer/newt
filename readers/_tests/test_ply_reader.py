import os

from readers.ply_reader import readPly
import numpy as np


def testReadPlyCube():
    current_path = os.path.dirname(os.path.abspath(__file__))
    polyhedron = readPly(current_path + "/test_ply_reader/cube.ply")
    assert len(polyhedron.getFaces()) == 6
    assert len(polyhedron.getPoints()) == 24
    assert np.allclose(
        polyhedron.getPoints(),
        np.array([
            [ 1.0, 1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [ 1.0, 1.0, 1.0],
            [-1.0, 1.0, 1.0],
            [-1.0, -1.0, 1.0],
            [ 1.0, -1.0, 1.0],
            [ 1.0, 1.0, -1.0],
            [ 1.0, 1.0, 1.0],
            [ 1.0, -1.0, 1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0, -1.0, -1.0],
            [ 1.0, -1.0, 1.0],
            [-1.0, -1.0, 1.0],
            [-1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0],
            [-1.0, -1.0, 1.0],
            [-1.0, 1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [ 1.0, 1.0, 1.0],
            [1.0, 1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0],
        ])
    )
