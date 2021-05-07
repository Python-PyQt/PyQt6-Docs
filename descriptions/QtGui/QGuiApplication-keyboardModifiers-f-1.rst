.. sip:method-description::
    :status: todo
    :pysig: 03e4d442d9642f898f386cc81094eb19
    :realsig: ()
    :digest: 30645bb250777dd6a22fd21094810a6b

Returns the current state of the modifier keys on the keyboard. The current state is updated sychronously as the event queue is emptied of events that will spontaneously change the keyboard state (\ :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyPress` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyRelease` events).

It should be noted this may not reflect the actual keys held on the input device at the time of calling but rather the modifiers as last reported in one of the above events. If no keys are being held :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.NoModifier` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.mouseButtons`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.queryKeyboardModifiers`.
