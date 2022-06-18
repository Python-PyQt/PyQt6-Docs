.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 549e2508211666993018878b2d9b1ec4

Returns ``true`` if the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice` represents an available local Bluetooth device; otherwise return false.

If the local Bluetooth adapter represented by an instance of this class is removed from the system (e.g. removal of the underlying Bluetooth dongle) then this instance will become invalid. An already invalid :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice` instance remains invalid even if the same Bluetooth adapter is returned to the system.

**Note:** Starting from Android 12 (API level 31), the construction of this class requires `bluetooth runtime permissions <https://developer.android.com/guide/topics/connectivity/bluetooth/permissions>`_ (\ *BLUETOOTH_SCAN* and *BLUETOOTH_CONNECT*). If the permissions are not granted, the device will not be valid.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.allDevices`.
