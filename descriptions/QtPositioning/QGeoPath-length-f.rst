.. sip:method-description::
    :status: todo
    :pysig: c385c73ed1bf074ef3ea8fc2fe35c7d5
    :realsig: (qsizetype,qsizetype) const
    :digest: b6ed4b7cb562696f8400768f908e1d6d

Returns the length of the path, in meters, from the element *indexFrom* to the element *indexTo*. The length is intended to be the sum of the shortest distances for each pair of adjacent points.

If *indexTo* is -1 (the default value), the length will be including the distance between last coordinate and the first (closed loop). To retrieve the length for the path, use 0 for *indexFrom* and :sip:ref:`~PyQt6.QtPositioning.QGeoPath.size` - 1 for *indexTo*.
