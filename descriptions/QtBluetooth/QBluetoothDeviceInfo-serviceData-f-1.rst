.. sip:method-description::
    :status: todo
    :pysig: 6d2c9ac0ef6c86632f53738d8d93078e
    :realsig: (const QBluetoothUuid&) const
    :digest: ca1c0770ea8c84e92535f831d4a1c90a

Returns the data associated with the given *serviceId*.

Service data is defined by the Supplement to the Bluetooth Core Specification and consists of two segments:

* Service UUID

* Sequence of arbitrary data octets

**Note:** The remote device may provide multiple data entries per *serviceId*. This function only returns the first entry. If all entries are needed use :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.serviceData` which returns a multi hash.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.serviceIds`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.setServiceData`.
