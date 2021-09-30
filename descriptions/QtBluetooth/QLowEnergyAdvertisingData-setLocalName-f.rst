.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 58570a644dbe21a142b7929f28ab102f

Specifies that *name* should be broadcast as the name of the device. If the full name does not fit into the advertising data packet, an abbreviated name is sent, as described by the Bluetooth Low Energy specification.

On Android, the local name cannot be changed. Android always uses the device name. If this local name is not empty, the Android implementation includes the device name in the advertisement packet; otherwise the device name is omitted from the advertisement packet.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyAdvertisingData.localName`.
