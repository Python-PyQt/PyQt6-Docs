.. sip:method-description::
    :status: todo
    :pysig: 9da1c309eac6b1bbf01e6d0a74ba76de
    :realsig: ()
    :digest: c6a49f45a6561f5ba81f3e634ba8d46f

Returns the current state of the buttons on the mouse. The current state is updated synchronously as the event queue is emptied of events that will spontaneously change the mouse state (\ :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonPress` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonRelease` events).

It should be noted this may not reflect the actual buttons held on the input device at the time of calling but rather the mouse buttons as last reported in one of the above events. If no mouse buttons are being held :sip:ref:`~PyQt6.QtCore.Qt.MouseButton.NoButton` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.keyboardModifiers`.
