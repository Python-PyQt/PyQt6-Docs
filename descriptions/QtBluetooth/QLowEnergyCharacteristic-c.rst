.. sip:class-description::
    :status: todo
    :brief: Stores information about a Bluetooth Low Energy service characteristic
    :digest: 54ba135f34dcd04880494dc8a4f315bf

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic` class stores information about a Bluetooth Low Energy service characteristic.

:sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic` provides information about a Bluetooth Low Energy service characteristic's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.name`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.uuid`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.value`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.properties`, and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.descriptors`. To obtain the characteristic's specification and information, it is necessary to connect to the device using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService` and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController` classes.

The characteristic value may be written via the `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_ instance that manages the service to which this characteristic belongs. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeCharacteristic` function writes the new value. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.characteristicWritten` signal is emitted upon success. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.value` of this object is automatically updated accordingly.

Characteristics may contain none, one or more descriptors. They can be individually retrieved using the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.descriptor` function. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyCharacteristic.descriptors` function returns all descriptors as a list. The general purpose of a descriptor is to add contextual information to the characteristic. For example, the descriptor might provide format or range information specifying how the characteristic's value is to be interpreted.

.. seealso:: `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_, `QLowEnergyDescriptor <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergydescriptor>`_.
