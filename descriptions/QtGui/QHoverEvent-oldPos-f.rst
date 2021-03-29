.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: 9cc4c011c669ba2da51fd5322c9caa06

Returns the previous position of the mouse cursor, relative to the widget that received the event. If there is no previous position,  will return the same position as pos().

On :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverEnter` events, this position will always be :sip:ref:`~PyQt6.QtCore.QPoint`\ (-1, -1).

.. seealso:: pos().
