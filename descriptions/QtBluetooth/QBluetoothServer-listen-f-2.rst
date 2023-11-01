.. sip:method-description::
    :status: todo
    :pysig: 1a7d5907a910c7894ffec6fb029269de
    :realsig: (const QBluetoothUuid&, const QString&)
    :digest: 17cfc321ab0fadc3c14309cb5c8a9489

Convenience function for registering an SPP service with *uuid* and *serviceName*. Because this function already registers the service, the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` object which is returned can not be changed any more. To shutdown the server later on it is required to call :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo.unregisterService` and :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.close` on this server object.

Returns a registered :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo` instance if successful otherwise an invalid :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo`. This function always assumes that the default Bluetooth adapter should be used.

If the server object is already listening for incoming connections this function returns an invalid :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceInfo`.

For an RFCOMM server this function is equivalent to following code snippet.

.. literalinclude:: ../../../snippets/qtconnectivity-src-bluetooth-qbluetoothserver.py
    :lines: 215-243

.. literalinclude:: ../../../snippets/qtconnectivity-src-bluetooth-qbluetoothserver.py
    :lines: 247-249

.. literalinclude:: ../../../snippets/qtconnectivity-src-bluetooth-qbluetoothserver.py
    :lines: 253-255

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.isListening`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.newConnection`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServer.listen`.
