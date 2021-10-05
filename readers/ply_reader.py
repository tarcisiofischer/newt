from geometry.polyhedron import Polyhedron
import numpy as np


def readPly(filename):
    """
    Helper method to read ply files.

    :param unicode filename:
    """
    reader = PlyReader()
    return reader.read(filename)


class PlyElement(object):
    def __init__(self, element_name, element_size):
        self.name = element_name
        self.size = element_size
        self.properties = []
        self.elements = []


class PlyReader(object):

    # Internal reader states
    READING_HEADER = 0
    READING_BODY = 1

    def __init__(self):
        self._state = self.READING_HEADER
        self._state_to_method = {
            self.READING_HEADER: self._read_header,
            self.READING_BODY: self._read_body,
        }
        self._elements = []
        self._data = {}

    def _read_body(self, n, line):
        if not hasattr(self, "_counter"):
            self._counter = 0
            self._current_element_idx = 0

        current_element = self._elements[self._current_element_idx]
        if not current_element.name in self._data.keys():
            self._data[current_element.name] = {}

        raw_data = line.split()
        idx = 0
        for property_name, property_type in current_element.properties:
            if not property_name in self._data[current_element.name].keys():
                self._data[current_element.name][property_name] = []
            current_property_data = self._data[current_element.name][property_name]

            if property_type == "list":
                list_size = int(raw_data[idx])
                converted_data = [
                    int(i) for i in raw_data[idx + 1 : idx + 1 + list_size]
                ]
                current_property_data.append(converted_data)
                idx += list_size + 1
            else:
                current_property_data.append(float(raw_data[idx]))
                idx += 1

        self._counter += 1
        if self._counter == current_element.size:
            self._counter = 0
            self._current_element_idx += 1

    def _read_header(self, n, line):
        if n == 0:
            assert (
                "ply" in line
            ), "Expected ply in document's first line, but got " + unicode(line)
            return

        if n == 1:
            assert (
                "format ascii 1.0" in line
            ), "This reader only supports format ascii 1.0"
            return

        if "element" in line:
            _, element_name, element_size = line.split()
            self._elements.append(PlyElement(element_name, int(element_size)))
            return

        if "property" in line:
            tokens = line.split()
            property_name = tokens[-1]
            property_type = tokens[1]
            # NOTE: If property type is list, the list types are ignored.
            self._elements[-1].properties.append((property_name, property_type))

        if "end_header" in line:
            self._state = self.READING_BODY
            return

    def read(self, filename):
        with open(filename, "r") as file_contents:
            for n, line in enumerate(file_contents):
                if "comment" in line:
                    # Ignore comment lines
                    continue
                self._state_to_method[self._state](n, line)
        points = np.array(
            list(
                zip(
                    self._data["vertex"]["x"],
                    self._data["vertex"]["y"],
                    self._data["vertex"]["z"],
                )
            )
        )
        faces = self._data["face"]["vertex_indices"]
        return Polyhedron(points, faces)
