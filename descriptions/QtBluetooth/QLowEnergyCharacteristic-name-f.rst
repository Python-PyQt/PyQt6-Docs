.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: cc2a389f7a3b54d83cba8e743c6e629b

Returns the human-readable name of the characteristic.

The name is based on the characteristic's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.uuid` which must have been standardized. The complete list of characteristic types can be found under `Bluetooth.org Characteristics <https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicsHome.aspx>`_.

The returned string is empty if the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.uuid` is unknown.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid.characteristicToString`.
