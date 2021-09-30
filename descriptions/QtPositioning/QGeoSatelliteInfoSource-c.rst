.. sip:class-description::
    :status: todo
    :brief: Abstract base class for the distribution of satellite information updates
    :digest: a7f2d227f1d5fbb00d047f86f95aa7a8

The :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource` class is an abstract base class for the distribution of satellite information updates.

The static function :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.createDefaultSource` creates a default satellite data source that is appropriate for the platform, if one is available. Otherwise, available QGeoPositionInfoSourceFactory plugins will be checked for one that has a satellite data source available.

Call :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.startUpdates` and :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.stopUpdates` to start and stop regular updates, or :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.requestUpdate` to request a single update. When an update is available, :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.satellitesInViewUpdated` and/or :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.satellitesInUseUpdated` will be emitted.

If regular satellite updates are required, :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.setUpdateInterval` can be used to specify how often these updates should be emitted. If no interval is specified, updates are simply provided whenever they are available. For example:

::

    // Emit updates every 10 seconds if available
    QGeoSatelliteInfoSource *source = QGeoSatelliteInfoSource::createDefaultSource(0);
    if (source)
        source->setUpdateInterval(10000);

To remove an update interval that was previously set, call :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.setUpdateInterval` with a value of 0.

**Note:** The satellite source may have a minimum value requirement for update intervals, as returned by :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.minimumUpdateInterval`.

**Note:** To use this class from Android service, see `Qt Positioning on Android <https://doc.qt.io/qt-6/qtpositioning-android.html>`_.
