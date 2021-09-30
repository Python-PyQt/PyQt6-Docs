.. sip:signal-description::
    :status: todo
    :pysig: 62a7437c83afe184456a35855c138dbd
    :realsig: (const QList<QGeoSatelliteInfo>&)
    :digest: 95f5f535753daba8b1d799c7e2fd1400

If :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.startUpdates` or :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.requestUpdate` is called, this signal is emitted when an update is available on the satellites that are currently in view.

The *satellites* parameter holds the satellites currently in view.
