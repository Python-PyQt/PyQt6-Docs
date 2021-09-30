.. sip:method-description::
    :status: todo
    :pysig: 1ccd3bd1e3b4dd9d72affda4dece4431
    :realsig: (qreal,qreal,qreal) const
    :digest: 71b5b7d97f11cf40c44c0d5c02bc985b

Returns the coordinate that is reached by traveling *distance* meters from the current coordinate at *azimuth* (or bearing) along a great-circle. There is an assumption that the Earth is spherical for the purpose of this calculation.

The altitude will have *distanceUp* added to it.

Returns an invalid coordinate if this coordinate is invalid.
