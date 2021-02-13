.. sip:class-description::
    :status: todo
    :brief: Describes a device from which a QInputEvent originates
    :digest: 65a5479062a1b5499ebdfce357202a38

The :sip:ref:`~PyQt6.QtGui.QInputDevice` class describes a device from which a :sip:ref:`~PyQt6.QtGui.QInputEvent` originates.

Each :sip:ref:`~PyQt6.QtGui.QInputEvent` contains a :sip:ref:`~PyQt6.QtGui.QInputDevice` pointer to allow accessing device-specific properties like type, capabilities and seat. It is the responsibility of the platform or generic plug-ins to discover, create and register an instance of this class corresponding to each available input device, via , before generating any input event referring to that device.

Applications do not need to instantiate this class, but can read the instances pointed to by :sip:ref:`~PyQt6.QtGui.QInputEvent.device` and :sip:ref:`~PyQt6.QtGui.QInputDevice.devices`.
