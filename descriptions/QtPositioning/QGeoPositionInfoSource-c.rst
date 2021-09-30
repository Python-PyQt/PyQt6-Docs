.. sip:class-description::
    :status: todo
    :brief: Abstract base class for the distribution of positional updates
    :digest: f61ab0046c6011052642624fd1de61ed

The :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` class is an abstract base class for the distribution of positional updates.

The static function :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.createDefaultSource` creates a default position source that is appropriate for the platform, if one is available. Otherwise, :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` will check for available plugins that implement the QGeoPositionInfoSourceFactory interface.

Users of a :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` subclass can request the current position using :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.requestUpdate`, or start and stop regular position updates using :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.startUpdates` and :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.stopUpdates`. When an update is available, :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.positionUpdated` is emitted. The last known position can be accessed with :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.lastKnownPosition`.

If regular position updates are required, :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.setUpdateInterval` can be used to specify how often these updates should be emitted. If no interval is specified, updates are simply provided whenever they are available. For example:

::

    // Emit updates every 10 seconds if available
    QGeoPositionInfoSource *source = QGeoPositionInfoSource::createDefaultSource(0);
    if (source)
        source->setUpdateInterval(10000);

To remove an update interval that was previously set, call :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.setUpdateInterval` with a value of 0.

**Note:** The position source may have a minimum value requirement for update intervals, as returned by :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource.minimumUpdateInterval`.

**Note:** To use this class from Android service, see `Qt Positioning on Android <https://doc.qt.io/qt-6/qtpositioning-android.html>`_.
