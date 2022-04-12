.. sip:method-description::
    :status: todo
    :pysig: ef28cd4918afbdb4cc477edbf9e707a8
    :realsig: (QGestureRecognizer*)
    :digest: d8d8437a11981f8d0a2dc43aaa4da6fb

Registers the given *recognizer* in the gesture framework and returns a gesture ID for it.

The application takes ownership of the *recognizer* and returns the gesture type ID associated with it. For gesture recognizers which handle custom :sip:ref:`~PyQt6.QtWidgets.QGesture` objects (i.e., those which return :sip:ref:`~PyQt6.QtCore.Qt.GestureType.CustomGesture` in a :sip:ref:`~PyQt6.QtWidgets.QGesture.gestureType` function) the return value is a generated gesture ID with the :sip:ref:`~PyQt6.QtCore.Qt.GestureType.CustomGesture` flag set.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.unregisterRecognizer`, :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.create`, :sip:ref:`~PyQt6.QtWidgets.QGesture`.
