.. sip:method-description::
    :status: todo
    :pysig: f5a13b3bac878820b76483c7239f5b8c
    :realsig: (const QBluetoothUuid&)
    :digest: 9e898f0cc918c340c65d6187c87a840f

Sets the unique identifier *uuid* for Bluetooth devices, that do not have addresses. This happens on macOS and iOS, where the CoreBluetooth API hides addresses, but provides UUIDs to identify devices/peripherals.

This uuid is invalid on any other platform.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.deviceUuid`.
