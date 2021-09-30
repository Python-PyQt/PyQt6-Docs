.. sip:method-description::
    :status: todo
    :pysig: fa75888c162e8eaa2fff2d6c42bbf0e0
    :realsig: (const QGeoCoordinate&) const
    :digest: e2d689f4dc671f57858ad3bafbc0e2b9

Returns the azimuth (or bearing) in degrees from this coordinate to the coordinate specified by *other*. Altitude is not used in the calculation.

The bearing returned is the bearing from the origin to *other* along the great-circle between the two coordinates. There is an assumption that the Earth is spherical for the purpose of this calculation.

Returns 0 if the type of this coordinate or the type of *other* is :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateType.InvalidCoordinate`.
