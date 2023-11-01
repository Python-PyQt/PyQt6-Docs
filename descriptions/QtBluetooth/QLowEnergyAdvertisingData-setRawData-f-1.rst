.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 10b442c37a63a31533103e12884bbf75

Sets the data to be advertised to *data*. If the value is not an empty byte array, it will be sent as-is as the advertising data and all other data in this object will be ignored. This can be used to send non-standard data.

**Note:** If *data* is longer than 31 bytes, it will be truncated. It is the caller's responsibility to ensure that *data* is well-formed.

Providing the raw advertising data is not supported on BlueZ DBus backend as BlueZ does not support it. This may change in a future release.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData.rawData`.
