import os
import pytest

from readers.ply_reader import readPly
import numpy as np


def getTestFile(filename):
    '''
    :param unicode filename:
    '''
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path + "/test_ply_reader/" + filename


@pytest.mark.parametrize(
    ('ply_name', 'expected_number_of_faces', 'expected_number_of_points'),
    [
        ('cube', 6, 24),
        ('sphere', 840, 422),
    ],
)
def testReadPlyCube(ply_name, expected_number_of_faces, expected_number_of_points):
    expected_cube_points = np.loadtxt(getTestFile("expected_" + ply_name + "_points.txt"))
    polyhedron = readPly(getTestFile(ply_name + ".ply"))

    assert len(polyhedron.getFaces()) == expected_number_of_faces
    assert len(polyhedron.getPoints()) == expected_number_of_points
    assert np.allclose(polyhedron.getPoints(), expected_cube_points)
