.. sip:method-description::
    :status: todo
    :pysig: fdc70f3bad01cf8286a9480c94f9862d
    :realsig: (const QBluetoothAddress&,QObject*)
    :digest: ae36a19bf78b6d56d8cd49eba9d32aa3

Constructs a new :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent` for *deviceAdapter* and with *parent*.

It uses *deviceAdapter* for the service search. If *deviceAdapter* is default constructed the resulting :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent` object will use the local default Bluetooth adapter.

If a *deviceAdapter* is specified that is not a local adapter :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.error` will be set to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error.InvalidBluetoothAdapterError`. Therefore it is recommended to test the error flag immediately after using this constructor.

**Note:** On WinRT the passed adapter address will be ignored.

**Note:** On Android passing any *deviceAdapter* address is meaningless as Android 6.0 or later does not publish the local Bluetooth address anymore. Subsequently, the passed adapter address can never be matched against the local adapter address. Therefore the subsequent call to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.start` will always trigger :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.Error.InvalidBluetoothAdapterError`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothServiceDiscoveryAgent.error`.
