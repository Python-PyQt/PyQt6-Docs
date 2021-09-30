.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: 935c744d41c88fb5f66e5d2c1a2cc7bc

Sets the NMEA data source to *device*. If the device is not open, it will be opened in QIODevice::ReadOnly mode.

The source device can only be set once and must be set before calling :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.startUpdates` or :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.requestUpdate`.

**Note:** The *device* must emit :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` for the source to be notified when data is available for reading. :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource` does not assume the ownership of the device, and hence does not deallocate it upon destruction.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QNmeaSatelliteInfoSource.device`.
