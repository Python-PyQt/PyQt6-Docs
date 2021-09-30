.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: 12f83f57d1fc62226bba77492a38a9a0

Returns the previous position of the mouse cursor, relative to the widget that received the event. If there is no previous position,  will return the same position as .

On :sip:ref:`~PyQt6.QtCore.QEvent.Type.HoverEnter` events, this position will always be :sip:ref:`~PyQt6.QtCore.QPointF`\ (-1, -1).

.. seealso:: posF().
