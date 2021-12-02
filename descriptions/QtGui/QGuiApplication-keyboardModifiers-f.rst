.. sip:method-description::
    :status: todo
    :pysig: 3a2e4a7e20160eac100e1688beddd51f
    :realsig: ()
    :digest: 555dd23fd5728f976994785e8ac54359

Returns the current state of the modifier keys on the keyboard. The current state is updated synchronously as the event queue is emptied of events that will spontaneously change the keyboard state (\ :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyPress` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.KeyRelease` events).

It should be noted this may not reflect the actual keys held on the input device at the time of calling but rather the modifiers as last reported in one of the above events. If no keys are being held :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier.NoModifier` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.mouseButtons`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.queryKeyboardModifiers`.
