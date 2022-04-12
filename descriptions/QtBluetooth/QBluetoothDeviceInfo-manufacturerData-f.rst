.. sip:method-description::
    :status: todo
    :pysig: d55e1f2ea2347f8437985af7e6d1bdde
    :realsig: () const
    :digest: 6d65b826a6c7c461a2fd3252b4fcf28b

Returns the complete set of all manufacturer data from advertisement packets.

Some devices may provide multiple manufacturer data entries per manufacturer ID. An example might be a Bluetooth Low Energy device that sends a different manufacturer data via advertisement packets and scan response packets respectively. Therefore the returned hash table may have multiple entries per manufacturer ID or hash key.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.setManufacturerData`.
