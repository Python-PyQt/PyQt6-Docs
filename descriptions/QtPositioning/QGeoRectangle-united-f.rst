.. sip:method-description::
    :status: todo
    :pysig: 97ade6beb971ab126d36ded094676d65
    :realsig: (const QGeoRectangle&) const
    :digest: 5b0ca7dc04afa2a776089f8e87309794

Returns the smallest geo rectangle which contains both this geo rectangle and *rectangle*.

If the centers of the two geo rectangles are separated by exactly 180.0 degrees then the width is set to 360.0 degrees with the leftmost longitude set to -180.0 degrees and the rightmost longitude set to 180.0 degrees. This is done to ensure that the result is independent of the order of the operands.
