.. sip:method-description::
    :status: todo
    :pysig: e8d648144ea87240b76e168a0239c8c7
    :realsig: ()
    :digest: c6a49f45a6561f5ba81f3e634ba8d46f

Returns the current state of the buttons on the mouse. The current state is updated synchronously as the event queue is emptied of events that will spontaneously change the mouse state (\ :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonPress` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseButtonRelease` events).

It should be noted this may not reflect the actual buttons held on the input device at the time of calling but rather the mouse buttons as last reported in one of the above events. If no mouse buttons are being held :sip:ref:`~PyQt6.QtCore.Qt.MouseButtons.NoButton` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.keyboardModifiers`.
