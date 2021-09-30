.. sip:method-description::
    :status: todo
    :pysig: aeaf3eb3aa263437ce2b8fcdd983fc37
    :realsig: (quint16) const
    :digest: 32f77d4d6a522cfc3896ca5e58e0f531

Returns the data associated with the given *manufacturerId*.

Manufacturer data is defined by the Supplement to the Bluetooth Core Specification and consists of two segments:

* Manufacturer specific identifier code from the `Assigned Numbers <https://www.bluetooth.com/specifications/assigned-numbers>`_ Company Identifiers document

* Sequence of arbitrary data octets

The interpretation of the data octets is defined by the manufacturer specified by the company identifier.

**Note:** The remote device may provide multiple data entries per manufacturerId. This function only returns the first entry. If all entries are needed use :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.manufacturerData` which returns a multi hash.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.manufacturerIds`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.setManufacturerData`.
