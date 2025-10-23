.. sip:method-description::
    :status: todo
    :pysig: 5417adcee9b2c956a74cf44b8edefebb
    :realsig: (QGestureRecognizer*)
    :digest: 9ef2a94d11e5db527ac9beef7cf75e56

Registers the given *recognizer* in the gesture framework and returns a gesture ID for it.

:sip:ref:`~PyQt6.QtWidgets.QApplication` takes ownership of the *recognizer*, and this function returns the gesture type ID associated with it. For gesture recognizers that handle custom :sip:ref:`~PyQt6.QtWidgets.QGesture` objects (those that return :sip:ref:`~PyQt6.QtCore.Qt.GestureType.CustomGesture` in a :sip:ref:`~PyQt6.QtWidgets.QGesture.gestureType` function), the return value is a generated gesture ID with the :sip:ref:`~PyQt6.QtCore.Qt.GestureType.CustomGesture` flag set.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.unregisterRecognizer`, :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.create`, :sip:ref:`~PyQt6.QtWidgets.QGesture`.
