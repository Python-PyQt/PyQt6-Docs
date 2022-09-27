.. sip:enum-description::
    :status: todo
    :digest: 957c6e7b92cf0f7d7a3bfc6e1de774a8

This enum describes the most of the local Bluetooth device.

**Note:** On macOS, it is not possible to set the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.hostMode` to  or .

**Note:** On Windows, it is not possible to set the :sip:ref:`~PyQt6.QtBluetooth.QBluetoothLocalDevice.hostMode` to  or . Using these modes is equivalent to .

**Note:** Starting from Android 13 (API level 33) the  state relies on non-public Android API as the public one has been deprecated, see (`disable() <https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#disable()>`_). This may change in a future version of Android.

**Note:** At least on Android 12 the device's Bluetooth visibility setting may dictate the result of setting either  or . For example if the visibility is set *off*, it may not be possible to enter the  mode, but  will be used instead. This may change in future version of Android.
