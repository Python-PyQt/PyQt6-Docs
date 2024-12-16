.. sip:method-description::
    :status: todo
    :pysig: 4ae99b47601b766b7bfa73b8b57e4387
    :realsig: () const
    :digest: 84cf5704ef4c55645f502d71f45c7e9e

Returns the complete set of all service data from advertisement packets.

Some devices may provide multiple service data entries per service data ID. An example might be a Bluetooth Low Energy device that sends a different service data via advertisement packets and scan response packets respectively. Therefore the returned hash table may have multiple entries per service data ID or hash key.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothDeviceInfo.setServiceData`.
