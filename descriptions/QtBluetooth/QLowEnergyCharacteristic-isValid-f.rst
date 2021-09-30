.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d43b62367a8b2b3fd662a931240eba97

Returns ``true`` if the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic` object is valid, otherwise returns ``false``.

An invalid characteristic object is not associated with any service (default-constructed) or the associated service is no longer valid due to a disconnect from the underlying Bluetooth Low Energy device, for example. Once the object is invalid it cannot become valid anymore.

**Note:** If a `QLowEnergyCharacteristic <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycharacteristic>`_ instance turns invalid due to a disconnect from the underlying device, the information encapsulated by the current instance remains as it was at the time of the disconnect. Therefore it can be retrieved after the disconnect event.
