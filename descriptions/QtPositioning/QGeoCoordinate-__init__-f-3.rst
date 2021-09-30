.. sip:method-description::
    :status: todo
    :pysig: eed5c663a9110c04fdce085b268c2b9d
    :realsig: (double,double,double)
    :digest: 67293d8185c8d8d4ed7fa9d7842226f1

Constructs a coordinate with the given *latitude*, *longitude* and *altitude*.

If the latitude is not between -90 to 90 inclusive, or the longitude is not between -180 to 180 inclusive, none of the values are set and the :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.type` will be :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.CoordinateType.InvalidCoordinate`.

Note that *altitude* specifies the meters above sea level.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.isValid`.
