from geometry.polyhedron import Polyhedron



STATE_READING_HEADER = 0
STATE_READING_BODY = 1

def readPly(filename):
    '''
    Reader for the .ply file format. This reader is really very dummy and I'm
    only using it because it is easier to model 3d stuff in blender and then
    read it instead of making polyhedrons by hand :P

    :param unicode filename:
    :returns Polyhedron:
    '''
    points = []
    faces = []
    with open(filename, 'r') as file_contents:
        state = STATE_READING_HEADER
        for n, line in enumerate(file_contents):
            if 'comment' in line:
                # Ignore comment lines
                continue

            if state == STATE_READING_HEADER:
                if n == 0:
                    assert 'ply' in line, \
                        "Expected ply in document's first line, but got " + unicode(line)
                    continue
                elif n == 1:
                    assert 'format ascii 1.0' in line, \
                        "This reader only supports format ascii 1.0"
                    continue

                if 'element' in line:
                    if 'vertex' in line:
                        number_of_vertexes = int(line.split()[-1])
                    elif 'face' in line:
                        number_of_faces = int(line.split()[-1])
                    else:
                        print "Unknown element " + unicode(line)
                    continue

                if 'end_header' in line:
                    state = STATE_READING_BODY
                    continue

            elif state == STATE_READING_BODY:
                if number_of_vertexes:
                    x, y, z, _, _, _ = line.split()
                    points.append([float(x), float(y), float(z)])
                    number_of_vertexes -= 1
                    continue
                elif number_of_faces:
                    faces.append([int(i) for i in line.split()[1:]])
                    number_of_faces -= 1
                    continue
    return Polyhedron(points, faces)
