.. sip:method-description::
    :status: todo
    :pysig: ba8e50cf2ec60987e3e15776baf9592c
    :realsig: (QBluetoothLocalDevice::HostMode)
    :digest: 75108c418d9b65c544625dc2c760b3ae

Sets the host mode of this local Bluetooth device to *mode*.

Some transitions such as turning the device on or off may take some time. Therefore subsequent calls should only be made once the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.hostModeStateChanged` signal has concluded the previous request. If this is ignored the result of such a series of calls is not well defined.

**Note:** Due to varying security policies on the supported platforms, this method may have differing behaviors on the various platforms. For example the system may ask the user for confirmation before turning Bluetooth on or off and not all host modes may be supported. On macOS, it is not possbile to programmatically change the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.hostMode`. A user can only switch Bluetooth on/off in the System Preferences. Please refer to the platform specific Bluetooth documentation for details.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.hostMode`.
