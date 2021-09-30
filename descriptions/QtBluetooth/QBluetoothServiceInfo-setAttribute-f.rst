.. sip:method-description::
    :status: todo
    :pysig: def7920dcfebba64911d0b50b3573936
    :realsig: (quint16,const QBluetoothUuid&)
    :digest: 1f01b55c8cf35695ac2f7d7c9096d73b

This is a convenience function.

Sets the attribute identified by *attributeId* to *value*.

If the service information is already registered with the platform's SDP database, the database entry will not be updated until :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.registerService` was called again.
