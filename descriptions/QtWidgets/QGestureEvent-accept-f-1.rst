.. sip:method-description::
    :status: todo
    :pysig: 0fb2059ab3e864b364165f3633e81d6d
    :realsig: (QGesture*)
    :digest: d2d79fe90a725d6e7d9fe34f80f18000

Sets the accept flag of the given *gesture* object, the equivalent of calling :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.setAccepted`.

Setting the accept flag indicates that the event receiver wants the gesture. Unwanted gestures may be propagated to the parent widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.ignore`.
