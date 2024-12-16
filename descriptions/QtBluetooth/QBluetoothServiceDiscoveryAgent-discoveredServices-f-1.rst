.. sip:method-description::
    :status: todo
    :pysig: 2c57c6f50829afbc876c9291f06bfda6
    :realsig: () const
    :digest: 24a6c2e3029677853441c6f5a47db18f

Returns the list of all discovered services.

This list of services accumulates newly discovered services from multiple calls to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.start`. Unless :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.clear` is called the list cannot decrease in size. This implies that if a remote Bluetooth device moves out of range in between two subsequent calls to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.start` the list may contain stale entries.

**Note:** The list of services should always be cleared before the discovery mode is changed.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.clear`.
