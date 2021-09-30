.. sip:method-description::
    :status: todo
    :pysig: fdc70f3bad01cf8286a9480c94f9862d
    :realsig: (const QBluetoothAddress&,QObject*)
    :digest: 6972f06a0e769de2371d6143ccae57ba

Constructs a new Bluetooth device discovery agent with *parent*.

It uses *deviceAdapter* for the device search. If *deviceAdapter* is default constructed the resulting :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent` object will use the local default Bluetooth adapter.

If a *deviceAdapter* is specified that is not a local adapter :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.error` will be set to :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.Error.InvalidBluetoothAdapterError`. Therefore it is recommended to test the error flag immediately after using this constructor.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.error`.
