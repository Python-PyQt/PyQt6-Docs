.. sip:method-description::
    :status: todo
    :pysig: 06c5b2efb6a490cca16c45e3ec0260d2
    :realsig: (QGeoPositionInfoSource*)
    :digest: 0d043a1fda60011f8dc5f98c5cd7cba1

Sets the new :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` to be used by this :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource` object. The area monitoring backend becomes the new :sip:ref:`~PyQt6.QtCore.QObject` parent for *newSource*. The previous :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` object will be deleted. All :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource` instances based on the same :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.sourceName` share the same :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` instance.

This may be useful when it is desirable to manipulate the positioning system used by the area monitoring engine.

Note that ownership must be taken care of by subclasses of :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource`. Due to the singleton pattern behind this class *newSource* may be moved to a new thread.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.positionInfoSource`.
