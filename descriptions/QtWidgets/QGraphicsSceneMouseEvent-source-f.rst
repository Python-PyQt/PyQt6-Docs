.. sip:method-description::
    :status: todo
    :pysig: 93fbf94e8837c538b71d95bda070f076
    :realsig: () const
    :digest: b69c4c6bd2d10248b707c772b12860fc

Returns information about the mouse event source.

The mouse event source can be used to distinguish between genuine and artificial mouse events. The latter are events that are synthesized from touch events by the operating system or Qt itself.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.MouseEventSource`, QMouseEvent::source().
