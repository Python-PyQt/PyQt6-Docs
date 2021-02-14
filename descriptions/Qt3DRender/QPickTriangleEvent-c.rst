.. sip:class-description::
    :status: todo
    :brief: Holds information when a triangle is picked
    :realname: Qt3DRender::QPickTriangleEvent
    :digest: 5cd0082c51d9f1a79d474aa92c52adee

The :sip:ref:`~PyQt6.Qt3DRender.QPickTriangleEvent` class holds information when a triangle is picked.

When QPickingSettings::pickMode() is set to :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickMethod.TrianglePicking`, the signals on QObjectPicker will carry an instance of :sip:ref:`~PyQt6.Qt3DRender.QPickTriangleEvent`.

This contains the details of the triangle that was picked.

**Note:** In the case of indexed rendering, the point indices are relative to the array of coordinates, not the array of indices.

.. seealso:: QPickingSettings, QPickEvent, QObjectPicker.
