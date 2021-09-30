.. sip:method-description::
    :status: todo
    :pysig: fa75888c162e8eaa2fff2d6c42bbf0e0
    :realsig: (const QGeoCoordinate&) const
    :digest: 1583ecc6e00cf82e6117fd043eb4225f

Returns the distance (in meters) from this coordinate to the coordinate specified by *other*. Altitude is not used in the calculation.

This calculation returns the great-circle distance between the two coordinates, with an assumption that the Earth is spherical for the purpose of this calculation.

Returns 0 if the type of this coordinate or the type of *other* is :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateType.InvalidCoordinate`.
