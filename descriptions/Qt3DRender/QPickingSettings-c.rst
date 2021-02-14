.. sip:class-description::
    :status: todo
    :brief: Specifies how entity picking is handled
    :realname: Qt3DRender::QPickingSettings
    :digest: 9f4421adb02b36d6ca0e43bfb3569059

The :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings` class specifies how entity picking is handled.

The picking settings determine how the entity picking is handled. For more details about entity picking, see QObjectPicker and QRayCaster component documentation.

When using QObjectPicker components, picking is triggered by mouse events.

When using QRayCaster or QScreenRayCaster components, picking can be explicitly triggered by the application.

In both cases, a ray will be cast through the scene to find geometry intersecting the ray.

.. seealso:: QObjectPicker, QPickEvent, QPickTriangleEvent, QRayCaster, QScreenRayCaster.
