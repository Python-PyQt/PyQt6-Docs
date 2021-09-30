.. sip:method-description::
    :status: todo
    :pysig: d519914b5e226f1a12bcf2e8e4c5ad8b
    :realsig: (const QBluetoothAddress&,QObject*)
    :digest: e9f7e6864cda211ef26de39f76ef309f

Returns a new object of this class that is in the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole` and has the parent object *parent* and is using *localDevice*. Typically, the next steps are to add some services and finally call :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.startAdvertising` on the returned object.

The peripheral is created on *localDevice*. If *localDevice* is invalid, the local default device is automatically selected. If *localDevice* specifies a local device that is not a local Bluetooth adapter, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.error` is set to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Error.InvalidBluetoothAdapterError`.

Selecting *localDevice* is only supported on Linux. On other platform, the parameter is ignored.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Role.PeripheralRole`.
