.. sip:method-description::
    :status: todo
    :pysig: 18a421b18c8a73aa210b6d1009d4ab80
    :realsig: (const QGeoRectangle&) const
    :digest: 07a558cbd377872243d132ed26ed12a8

Returns whether the geo rectangle *rectangle* intersects this geo rectangle.

If the top or bottom edges of both geo rectangles are at one of the poles the geo rectangles are considered to be intersecting, since the longitude is irrelevant when the edges are at the pole.
