.. sip:method-description::
    :status: todo
    :pysig: 4066b103fce5180a2a88aa9d631f0351
    :realsig: (const QList<QBluetoothUuid>&)
    :digest: 5a9931c83c439354a189ff3952c2f08a

Sets the UUID filter to *uuids*. Only services matching the UUIDs in *uuids* will be returned. The matching applies to the service's :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.AttributeId.ServiceId` and :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.AttributeId.ServiceClassIds` attributes.

An empty UUID list is equivalent to a list containing only :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid.ServiceClassUuid.PublicBrowseGroup`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.uuidFilter`.
