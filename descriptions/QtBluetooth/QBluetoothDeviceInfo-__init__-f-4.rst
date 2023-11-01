.. sip:method-description::
    :status: todo
    :pysig: f7b716ab5f657d53cbe881f4bf930bd6
    :realsig: (const QBluetoothAddress&, const QString&, quint32)
    :digest: 850b685aeb2f8a28619c7eac5985b2fc

Constructs a :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo` object with Bluetooth address *address*, device name *name* and the encoded class of device *classOfDevice*.

The *classOfDevice* parameter is encoded in the following format

+---------+------+---------------------+
| Bits    | Size | Description         |
+=========+======+=====================+
| 0 - 1   | 2    | Unused, set to 0.   |
+---------+------+---------------------+
| 2 - 7   | 6    | Minor device class. |
+---------+------+---------------------+
| 8 - 12  | 5    | Major device class. |
+---------+------+---------------------+
| 13 - 23 | 11   | Service class.      |
+---------+------+---------------------+
