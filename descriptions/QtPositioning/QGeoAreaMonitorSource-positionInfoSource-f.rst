.. sip:method-description::
    :status: todo
    :pysig: 06c5b2efb6a490cca16c45e3ec0260d2
    :realsig: () const
    :digest: 70b8b8a2e0e538f3bca7f37126e28adf

Returns the current :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` used by this :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource` object. The function will return :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.createDefaultSource` if no other object has been set.

The function returns ``nullptr`` if not even a default :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` exists.

Any usage of the returned :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` instance should account for the fact that it may reside in a different thread.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource`, :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.setPositionInfoSource`.
