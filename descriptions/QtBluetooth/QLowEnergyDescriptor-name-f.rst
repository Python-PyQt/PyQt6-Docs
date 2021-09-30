.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: b1dcd7c31a15ffaae01853932207edcc

Returns the human-readable name of the descriptor.

The name is based on the descriptor's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor.type`. The complete list of descriptor types can be found under `Bluetooth.org Descriptors <https://developer.bluetooth.org/gatt/descriptors/Pages/DescriptorsHomePage.aspx>`_.

The returned string is empty if the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor.type` is unknown.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor.type`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothUuid.descriptorToString`.
