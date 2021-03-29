.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: b1ee5aaf6c2dc36d5e0fee9afd3e668d

Returns the relative amount that the wheel was rotated, in eighths of a degree. A positive value indicates that the wheel was rotated forwards away from the user; a negative value indicates that the wheel was rotated backwards toward the user. ``angleDelta().y()`` provides the angle through which the common vertical mouse wheel was rotated since the previous event. ``angleDelta().x()`` provides the angle through which the horizontal mouse wheel was rotated, if the mouse has a horizontal wheel; otherwise it stays at zero. Some mice allow the user to tilt the wheel to perform horizontal scrolling, and some touchpads support a horizontal scrolling gesture; that will also appear in ``angleDelta().x()``.

Most mouse types work in steps of 15 degrees, in which case the delta value is a multiple of 120; i.e., 120 units \* 1/8 = 15 degrees.

However, some mice have finer-resolution wheels and send delta values that are less than 120 units (less than 15 degrees). To support this possibility, you can either cumulatively add the delta values from events until the value of 120 is reached, then scroll the widget, or you can partially scroll the widget in response to each wheel event. But to provide a more native feel, you should prefer :sip:ref:`~PyQt6.QtGui.QWheelEvent.pixelDelta` on platforms where it's available.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qevent.py
    :lines: 64-77

**Note:** On platforms that support scrolling :sip:ref:`~PyQt6.QtGui.QWheelEvent.phase`, the delta may be null when:

* scrolling is about to begin, but the distance did not yet change (\ :sip:ref:`~PyQt6.QtCore.Qt.ScrollPhase.ScrollBegin`),

* or scrolling has ended and the distance did not change anymore (\ :sip:ref:`~PyQt6.QtCore.Qt.ScrollPhase.ScrollEnd`).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWheelEvent.pixelDelta`.
