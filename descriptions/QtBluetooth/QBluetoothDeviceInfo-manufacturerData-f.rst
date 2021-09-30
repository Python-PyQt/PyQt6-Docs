.. sip:method-description::
    :status: todo
    :pysig: d55e1f2ea2347f8437985af7e6d1bdde
    :realsig: () const
    :digest: 4c1d64291da1249bf684670e97e28d5d

Returns the complete set of all manufacturer data.

Some devices may provide multiple manufacturer data entries per manufacturer ID. An example might be a Bluetooth Low Energy device that sends a different manufacturer data via advertisement packets and scan response packets respectively. Therefore the returned hash table may have multiple entries per manufacturer ID or hash key.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.setManufacturerData`.
