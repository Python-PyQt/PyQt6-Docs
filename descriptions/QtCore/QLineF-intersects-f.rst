.. sip:method-description::
    :status: todo
    :pysig: bb119203c1b54f56e59a239738e29c96
    :realsig: (const QLineF&,QPointF*) const
    :digest: 9600111a712c7050781819420b426a6e

Returns a value indicating whether or not *this* line intersects with the given *line*.

The actual intersection point is extracted to *intersectionPoint* (if the pointer is valid). If the lines are parallel, the intersection point is undefined.
