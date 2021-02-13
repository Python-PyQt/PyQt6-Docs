.. sip:method-description::
    :status: todo
    :pysig: 4486e066c9b7df6f6178aefd175318ca
    :realsig: (Qt::GestureType)
    :digest: a36a599ff11788f1b591a609072332e2

Sets the accept flag of the given *gestureType*, the equivalent of calling :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.setAccepted`.

Setting the accept flag indicates that the event receiver wants the gesture. Unwanted gestures may be propagated to the parent widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.ignore`.
