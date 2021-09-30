.. sip:method-description::
    :status: todo
    :pysig: c64c662746ce4634701ef3dd9963c93e
    :realsig: (const QBluetoothAddress&)
    :digest: 458696966e93f6f62d7ef7dbd36c4ae5

Sets the remote device address to *address*. If *address* is default constructed, services will be discovered on all contactable Bluetooth devices. A new remote address can only be set while there is no service discovery in progress; otherwise this function returns false.

On some platforms the service discovery might lead to pairing requests. Therefore it is not recommended to do service discoveries on all devices. This function can be used to restrict the service discovery to a particular device.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.remoteAddress`.
