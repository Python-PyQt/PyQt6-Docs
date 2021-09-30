.. sip:method-description::
    :status: todo
    :pysig: 15bb6dd4c08c32ed8272c0814d30eefa
    :realsig: () const
    :digest: ee3e2ee1d81150bd634bb57510efe92c

Returns the address of the local Bluetooth adapter being used for the communication.

If this class instance was requested to use the default adapter but there was no default adapter when creating this class instance, the returned :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress` will be null.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothAddress.isNull`.
