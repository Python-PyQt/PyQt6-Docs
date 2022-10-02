.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: ()
    :digest: c7796cb94cde3aacca677d7760f21af0

Gets the timeout, in milliseconds, before the gesture triggers.

The recognizer will detect a touch down and if timeout() later the touch is still down, it will trigger the :sip:ref:`~PyQt6.QtWidgets.QTapAndHoldGesture`. The default value is 700 milliseconds.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTapAndHoldGesture.setTimeout`.
