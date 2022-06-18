.. sip:method-description::
    :status: todo
    :pysig: fdc70f3bad01cf8286a9480c94f9862d
    :realsig: (const QBluetoothAddress&,QObject*)
    :digest: b5fd8dc2003ab87e67cce461078af155

Construct new :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice` for *address*. If *address* is default constructed the resulting local device selects the local default device.

**Note:** Starting from Android 12 (API level 31), the construction of this class requires `bluetooth runtime permissions <https://developer.android.com/guide/topics/connectivity/bluetooth/permissions>`_ (\ *BLUETOOTH_SCAN* and *BLUETOOTH_CONNECT*). If the permissions are not granted, the device will not be valid.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.isValid`.
