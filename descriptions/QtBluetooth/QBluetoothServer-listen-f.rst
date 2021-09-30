.. sip:method-description::
    :status: todo
    :pysig: 4047002afdb9b4f99f54887954e6e3f9
    :realsig: (const QBluetoothAddress&,quint16)
    :digest: 399101f167316ea02eeab5eb5bbcda64

Start listening for incoming connections to *address* on *port*. *address* must be a local Bluetooth adapter address and *port* must be larger than zero and not be taken already by another Bluetooth server object. It is recommended to avoid setting a port number to enable the system to automatically choose a port.

Returns ``true`` if the operation succeeded and the server is listening for incoming connections, otherwise returns ``false``.

If the server object is already listening for incoming connections this function always returns ``false``. :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.close` should be called before calling this function.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.isListening`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.newConnection`.
