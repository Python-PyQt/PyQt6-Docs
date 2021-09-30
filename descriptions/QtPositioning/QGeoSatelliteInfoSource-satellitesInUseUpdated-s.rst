.. sip:signal-description::
    :status: todo
    :pysig: 62a7437c83afe184456a35855c138dbd
    :realsig: (const QList<QGeoSatelliteInfo>&)
    :digest: 45ce9ea0878d3d15fcfe20d40e6ec559

If :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.startUpdates` or :sip:ref:`~PyQt6.QtPositioning.QGeoSatelliteInfoSource.requestUpdate` is called, this signal is emitted when an update is available on the number of satellites that are currently in use.

These are the satellites that are used to get a "fix" - that is, those used to determine the current position.

The *satellites* parameter holds the satellites currently in use.
