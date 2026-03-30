.. sip:method-description::
    :status: todo
    :pysig: 219cadf8c718fb2f578a2aebdf728527
    :realsig: (const QBluetoothUuid&, const QString&, quint32)
    :digest: 915dd18801a9214fd371512ebbc23607

Constructs a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo` object with unique *uuid*, device name *name* and the encoded class of device *classOfDevice*.

This constructor is required for Low Energy devices on macOS and iOS. CoreBluetooth API hides addresses and provides unique UUIDs to identify a device. This UUID is not the same thing as a service UUID and is required to work later with CoreBluetooth API and discovered devices.
