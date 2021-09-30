.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: e0ad9323185f8af6f9afbdf919613a35

Sets the maximum search time for Bluetooth Low Energy device search to *timeout* in milliseconds. If *timeout* is ``0`` the discovery runs until :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.stop` is called.

This reflects the fact that the discovery process for Bluetooth Low Energy devices is mostly open ended. The platform continues to look for more devices until the search is manually stopped. The timeout ensures that the search is aborted after *timeout* milliseconds. Of course, it is still possible to manually abort the discovery by calling :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.stop`.

The new timeout value does not take effect until the device search is restarted. In addition the timeout does not affect the classic Bluetooth device search. Depending on the platform the classic search may add more time to the total discovery process beyond *timeout*.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceDiscoveryAgent.lowEnergyDiscoveryTimeout`.
