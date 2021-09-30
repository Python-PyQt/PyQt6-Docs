.. sip:method-description::
    :status: todo
    :pysig: 8241c5f41d48cb313647c00abb0256dd
    :realsig: (const QBluetoothUuid&) const
    :digest: 8beaf191ce38b954c1574c7afce726fa

Returns the matching characteristic for *uuid*; otherwise an invalid characteristic.

The returned characteristic is invalid if this service instance's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.discoverDetails` was not yet called or there are no characteristics with a matching *uuid*.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristics`.
