.. sip:method-description::
    :status: todo
    :pysig: 4486e066c9b7df6f6178aefd175318ca
    :realsig: (Qt::GestureType)
    :digest: 445cacff38a1c91020b24d2012d6c781

Clears the accept flag parameter of the given *gestureType*, the equivalent of calling :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.setAccepted`.

Clearing the accept flag indicates that the event receiver does not want the gesture. Unwanted gestures may be propagated to the parent widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureEvent.accept`.
