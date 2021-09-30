.. sip:method-description::
    :status: todo
    :pysig: f5a13b3bac878820b76483c7239f5b8c
    :realsig: () const
    :digest: 8291bb705c31f0925c6c35101855e800

This is a convenience function. It is equivalent to calling attribute(\ :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.AttributeId.ServiceId`).value<\ :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid`>().

Returns the custom UUID of the service. This UUID may be null. UUIDs based on `Bluetooth SIG standards <https://bluetooth.org>`_ should be retrieved via :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.serviceClassUuids`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.setServiceUuid`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.attribute`.
