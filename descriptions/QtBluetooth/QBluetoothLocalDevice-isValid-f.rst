.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 5cb61eef87f6291316ee1a5aba44df58

Returns ``true`` if the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice` represents an available local Bluetooth device; otherwise return false.

If the local Bluetooth adapter represented by an instance of this class is removed from the system (e.g. removal of the underlying Bluetooth dongle) then this instance will become invalid. An already invalid :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice` instance remains invalid even if the same Bluetooth adapter is returned to the system.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.allDevices`.
