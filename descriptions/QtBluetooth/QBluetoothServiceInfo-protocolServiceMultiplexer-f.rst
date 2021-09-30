.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 410ff1e6b3fcbe766f78867cfd3565d5

This is a convenience function. Returns the protocol/service multiplexer for services which support the L2CAP protocol, otherwise returns -1.

This function is equivalent to extracting the information from QBluetoothServiceInfo::Sequence returned by :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.attribute`\ (\ :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.AttributeId.ProtocolDescriptorList`).
