.. sip:method-description::
    :status: todo
    :pysig: 929edda6a97571ebce7151ff0802751f
    :realsig: (quint16,const QVariant&)
    :digest: 85f99989c35a6c5855070fc7d5b42069

Sets the attribute identified by *attributeId* to *value*.

If the service information is already registered with the platform's SDP database, the database entry will not be updated until :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.registerService` was called again.

**Note:** If an attribute expectes a byte-encoded value (e.g. Bluetooth HID services), it should be set as :sip:ref:`~PyQt6.QtCore.QByteArray`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.isRegistered`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.registerService`.
