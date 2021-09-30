.. sip:class-description::
    :status: todo
    :brief: Used to create GATT service data
    :digest: 5417bb3e07181563293a4afe12d4ee61

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptorData` class is used to create GATT service data.

An object of this class provides a descriptor to be added to a :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristicData` object via :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristicData.addDescriptor`.

**Note:** The member functions related to access permissions are only applicable to those types of descriptors for which the Bluetooth specification does not prescribe if and how their values can be accessed.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristicData`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyServiceData`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.addService`.
