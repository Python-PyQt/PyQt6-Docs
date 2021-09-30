.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 386a5ee2d59e8bca9a8c8b4508c3cc92

This is a convenience function. Returns the server channel for services which support the RFCOMM protocol, otherwise returns -1.

This function is equivalent to extracting the information from QBluetoothServiceInfo::Sequence returned by :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.attribute`\ (QBluetootherServiceInfo::ProtocolDescriptorList).
