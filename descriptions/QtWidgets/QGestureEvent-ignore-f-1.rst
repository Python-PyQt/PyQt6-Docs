.. sip:method-description::
    :status: todo
    :pysig: 0fb2059ab3e864b364165f3633e81d6d
    :realsig: (QGesture*)
    :digest: 8b85dc86fc50a4b64fc09cfeb12eefc3

Clears the accept flag parameter of the given *gesture* object, the equivalent of calling :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.setAccepted`.

Clearing the accept flag indicates that the event receiver does not want the gesture. Unwanted gestures may be propagated to the parent widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.accept`.
