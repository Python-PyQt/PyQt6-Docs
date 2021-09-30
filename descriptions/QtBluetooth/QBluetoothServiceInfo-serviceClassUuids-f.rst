.. sip:method-description::
    :status: todo
    :pysig: d7fdc8bb4f184bdfd71909260960b254
    :realsig: () const
    :digest: f8ae7ebe4104a07115e8d0bdbaf4fa6e

Returns a list of UUIDs describing the service classes that this service conforms to.

This is a convenience function. It is equivalent to calling attribute(\ :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.AttributeId.ServiceClassIds`).value<QBluetoothServiceInfo::Sequence>() and subsequently iterating over its :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid` entries.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.attribute`.
