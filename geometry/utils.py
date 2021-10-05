def boundingBox(polyhedron):
    points = polyhedron.getPoints()
    xmin = points[0][0]
    xmax = points[0][0]
    ymin = points[0][1]
    ymax = points[0][1]
    zmin = points[0][2]
    zmax = points[0][2]
    for x, y, z in points:
        xmin = x if x < xmin else xmin
        xmax = x if x > xmax else xmax
        ymin = y if y < ymin else ymin
        ymax = y if y > ymax else ymax
        zmin = z if z < zmin else zmin
        zmax = z if z > zmax else zmax
    return xmin, xmax, ymin, ymax, zmin, zmax


def hasBoundingBoxIntersection(polyhedron0, polyhedron1):
    xmin0, xmax0, ymin0, ymax0, zmin0, zmax0 = boundingBox(polyhedron0)
    xmin1, xmax1, ymin1, ymax1, zmin1, zmax1 = boundingBox(polyhedron1)

    return (
        (xmin0 < xmax1 and xmax0 > xmin1)
        and (ymin0 < ymax1 and ymax0 > ymin1)
        and (zmin0 < zmax1 and zmax0 > zmin1)
    )
