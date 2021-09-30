.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: 1946abe3c37a06cd32756d56ef7348ab

Sets the data to be advertised to *data*. If the value is not an empty byte array, it will be sent as-is as the advertising data and all other data in this object will be ignored. This can be used to send non-standard data.

**Note:** If *data* is longer than 31 bytes, it will be truncated. It is the caller's responsibility to ensure that *data* is well-formed.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData.rawData`.
