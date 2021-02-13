.. sip:class-description::
    :status: todo
    :brief: Describes a device from which mouse, touch or tablet events originate
    :digest: 4ad5c7b376f57fb07e710a437f006ae7

The :sip:ref:`~PyQt6.QtGui.QPointingDevice` class describes a device from which mouse, touch or tablet events originate.

Each :sip:ref:`~PyQt6.QtGui.QPointerEvent` contains a :sip:ref:`~PyQt6.QtGui.QPointingDevice` pointer to allow accessing device-specific properties like type and capabilities. It is the responsibility of the platform or generic plug-ins to register the available pointing devices via QWindowSystemInterface before generating any pointer events. Applications do not need to instantiate this class, they should just access the global instances pointed to by QPointerEvent::device().
