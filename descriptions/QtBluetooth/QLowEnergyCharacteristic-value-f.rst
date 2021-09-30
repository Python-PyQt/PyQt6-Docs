.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: ca5b8b1b73c679a68193b6838514b0d3

Returns the cached value of the characteristic.

If the characteristic's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.properties` permit writing of new values, the value can be updated using :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic`.

The cache is updated during the associated service's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.discoverDetails`, a successful :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.readCharacteristic`/\ :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic` operation or when an update notification is received.

The returned :sip:ref:`~PyQt6.QtCore.QByteArray` always remains empty if the characteristic does not have the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.PropertyType.Read`. In such cases only the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicChanged` or :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicWritten` may provice information about the value of this characteristic.
