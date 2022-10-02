.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: eba5988c846e89a532e26f3eed8fb168

Returns the previous position of the mouse cursor, relative to the widget that received the event. If there is no previous position, oldPosF() will return the same position as posF().

On :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverEnter` events, this position will always be :sip:ref:`~PyQt6.QtCore.QPointF`\ (-1, -1).

.. seealso:: posF().
