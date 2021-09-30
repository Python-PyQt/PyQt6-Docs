.. sip:method-description::
    :status: todo
    :pysig: 3b243ff47efe657fc01663c06aec7197
    :realsig: (const QBluetoothDeviceInfo&,const QBluetoothAddress&,QObject*)
    :digest: ff167a9edd81235c91184679152a6fe7

Returns a new instance of this class with *parent*.

The *remoteDevice* must contain the address of the remote Bluetooth Low Energy device to which this object should attempt to connect later on.

The connection is established via *localDevice*. If *localDevice* is invalid, the local default device is automatically selected. If *localDevice* specifies a local device that is not a local Bluetooth adapter, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.error` is set to :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Error.InvalidBluetoothAdapterError` once :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectToDevice` is called.

Note that specifying the local device to be used for the connection is only possible when using BlueZ. All other platforms do not support this feature.
