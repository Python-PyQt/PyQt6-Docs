.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 940fd2c333aaa73bc4b1eebab96bb5fc

Returns ``true`` if the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor` object is valid, otherwise returns ``false``.

An invalid descriptor instance is not associated with any service (default-constructed) or the associated service is no longer valid due to a disconnect from the underlying Bluetooth Low Energy device, for example. Once the object is invalid it cannot become valid anymore.

**Note:** If a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor` instance turns invalid due to a disconnect from the underlying device, the information encapsulated by the current instance remains as it was at the time of the disconnect. Therefore it can be retrieved after the disconnect event.
