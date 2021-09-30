.. sip:class-description::
    :status: todo
    :brief: Satellite information using an NMEA data source
    :digest: b1eb2868e36b6ffc93dfa49ec185b415

The :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource` class provides satellite information using an NMEA data source.

NMEA is a commonly used protocol for the specification of one's global position at a certain point in time. The :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource` class reads NMEA data and uses it to provide information about satellites in view and satellites in use in form of lists of :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfo` objects.

A :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource` instance operates in either :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode.RealTimeMode` or :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.UpdateMode.SimulationMode`. These modes allow NMEA data to be read from either a live source of data, or replayed for simulation purposes from previously recorded NMEA data.

The source of NMEA data is set via :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.setDevice`.

Use :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.startUpdates` to start receiving regular satellite information updates and :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.stopUpdates` to stop these updates. If you only require updates occasionally, you can call :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.requestUpdate` to request a single update of both satellites in view and satellites in use.

The information about satellites in view is received via the satellitesInViewUpdated() signal.

The information about satellites in use is received via the satellitesInUseUpdated() signal.
