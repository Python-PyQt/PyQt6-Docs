.. sip:class-description::
    :status: todo
    :brief: Positional information using a NMEA data source
    :digest: cf0be8a460cada0bd5d180351bd902f7

The :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource` class provides positional information using a NMEA data source.

NMEA is a commonly used protocol for the specification of one's global position at a certain point in time. The :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource` class reads NMEA data and uses it to provide positional data in the form of :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfo` objects.

A :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource` instance operates in either :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.UpdateMode.RealTimeMode` or :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.UpdateMode.SimulationMode`. These modes allow NMEA data to be read from either a live source of positional data, or replayed for simulation purposes from previously recorded NMEA data.

The source of NMEA data is set with :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.setDevice`.

Use :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.startUpdates` to start receiving regular position updates and :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.stopUpdates` to stop these updates. If you only require updates occasionally, you can call :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.requestUpdate` to request a single update.

In both cases the position information is received via the positionUpdated() signal and the last known position can be accessed with :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.lastKnownPosition`.

:sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource` supports reporting the accuracy of the horizontal and vertical position. To enable position accuracy reporting an estimate of the User Equivalent Range Error associated with the NMEA source must be set with :sip:ref:`~PyQt6.QtPositioning.QNmeaPositionInfoSource.setUserEquivalentRangeError`.
