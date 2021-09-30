.. sip:class-description::
    :status: todo
    :brief: Stores information about the Bluetooth Low Energy descriptor
    :digest: b3016dc2ce694b155e127c320b448a6e

The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor` class stores information about the Bluetooth Low Energy descriptor.

:sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor` provides information about a Bluetooth Low Energy descriptor's :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor.name`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor.uuid`, and :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor.value`. Descriptors are encapsulated by Bluetooth Low Energy characteristics and provide additional contextual information about the characteristic (data format, notification activation and so on).

The descriptor value may be written via the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService` instance that manages the service to which this descriptor belongs. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.writeDescriptor` function writes the new value. The :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyService.descriptorWritten` signal is emitted upon success. The cached :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyDescriptor.value` of this object is updated accordingly.

.. seealso:: `QLowEnergyService <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergyservice>`_, `QLowEnergyCharacteristic <https://doc.qt.io/qt-6/qtbluetooth-changes-qt6.html#qlowenergycharacteristic>`_.
