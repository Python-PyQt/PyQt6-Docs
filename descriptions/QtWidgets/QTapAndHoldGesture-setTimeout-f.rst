.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (int)
    :digest: 0c2297d56ff09fdc45cbe9e0d375c2e4

Set the timeout, in milliseconds, before the gesture triggers.

The recognizer will detect a touch down and if *msecs* later the touch is still down, it will trigger the :sip:ref:`~PyQt6.QtWidgets.QTapAndHoldGesture`. The default value is 700 milliseconds.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTapAndHoldGesture.timeout`.
