.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (double,double)
    :digest: e7bcee872870db7d0f7f4dc1e285d936

Constructs a coordinate with the given *latitude* and *longitude*.

If the latitude is not between -90 to 90 inclusive, or the longitude is not between -180 to 180 inclusive, none of the values are set and the :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.type` will be :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateType.InvalidCoordinate`.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.isValid`.
