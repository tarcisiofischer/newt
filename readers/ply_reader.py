from geometry.polyhedron import Polyhedron


def readPly(filename):
    '''
    Helper method to read ply files.

    :param unicode filename:
    '''
    reader = PlyReader()
    return reader.read(filename)


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
        self._number_of_vertexes = 0
        self._number_of_faces = 0
        self._points = []
        self._faces = []


    def _read_body(self, n, line):
        if self._number_of_vertexes:
            x, y, z, _, _, _ = line.split()
            self._points.append([float(x), float(y), float(z)])
            self._number_of_vertexes -= 1
            return

        if self._number_of_faces:
            self._faces.append([int(i) for i in line.split()[1:]])
            self._number_of_faces -= 1
            return


    def _read_header(self, n, line):
        if n == 0:
            assert 'ply' in line, \
                "Expected ply in document's first line, but got " + unicode(line)
            return

        if n == 1:
            assert 'format ascii 1.0' in line, \
                "This reader only supports format ascii 1.0"
            return

        if 'element' in line:
            if 'vertex' in line:
                self._number_of_vertexes = int(line.split()[-1])
            elif 'face' in line:
                self._number_of_faces = int(line.split()[-1])
            else:
                print "Unknown element " + unicode(line)
            return

        if 'end_header' in line:
            self._state = self.READING_BODY
            return


    def read(self, filename):
        with open(filename, 'r') as file_contents:
            for n, line in enumerate(file_contents):
                if 'comment' in line:
                    # Ignore comment lines
                    continue
                self._state_to_method[self._state](n, line)
        return Polyhedron(self._points, self._faces)
