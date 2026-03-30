.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: 6aee4bc6a7d2764767cb4e8b38ac486a

Returns the previous position of the mouse cursor, relative to the widget that received the event. If there is no previous position, oldPos() will return the same position as position().

On :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverEnter` events, this position will always be :sip:ref:`~PyQt6.QtCore.QPoint`\ (-1, -1).

.. seealso:: position().
