.. sip:method-description::
    :status: todo
    :pysig: 91acadc83f1c4e5f5454e50a0082bad7
    :realsig: (const QLineF&) const
    :digest: 8ae442f95a04b0d1095ec2128587ad5d

Returns the angle (in degrees) from this line to the given *line*, taking the direction of the lines into account. If the lines do not :sip:ref:`~PyQt6.QtCore.QLineF.intersects` within their range, it is the intersection point of the extended lines that serves as origin (see :sip:ref:`~PyQt6.QtCore.QLineF.IntersectionType.UnboundedIntersection`).

The returned value represents the number of degrees you need to add to this line to make it have the same angle as the given *line*, going counter-clockwise.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLineF.intersects`.
