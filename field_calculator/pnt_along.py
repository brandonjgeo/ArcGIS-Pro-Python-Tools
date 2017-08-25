def pnt_along(shape, value=0.0, use_fraction=False, XorY="X"):
    """Position X or Y coordinate, x/y meters or decimal fraction along a line.
    :Requires:
    :--------
    : shape field: python parser use !Shape!
    : value: (distance or decimal fraction, 0-1)
    : use_fraction: (True/False)
    : XorY: specify X or Y coordinates
    :
    :Returns: the specified coordinate (X or Y) meters or % along line or boundary
    :-------
    :
    :Useage: pnt_along(!Shape!, 100, False, "X") # X, 100 m from start point
    :
    """
    XorY = XorY.upper()
    if use_fraction and (value > 1.0):
        value = value/100.0
    if shape.type.lower() == "polygon":
        shape = shape.boundary()
    pnt = shape.positionAlongLine(value,use_fraction)
    if XorY == 'X':
        return pnt.centroid.X
    else:
        return pnt.centroid.Y