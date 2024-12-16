.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: d6dcada840e82d790d7c1fe8e2b84b25

Sets the data to be advertised to *data*. If the value is not an empty byte array, it will be sent as-is as the advertising data and all other data in this object will be ignored. This can be used to send non-standard data.

**Note:** If *data* is longer than 31 bytes, it will be truncated. It is the caller's responsibility to ensure that *data* is well-formed.

Setting raw advertising data is only supported on the `Linux Bluetooth Kernel API <https://doc.qt.io/qt-6/qtbluetooth-index.html#linux-specific>`_ backend. Other backends do not allow to specify the raw advertising data as a global field.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData.rawData`.
