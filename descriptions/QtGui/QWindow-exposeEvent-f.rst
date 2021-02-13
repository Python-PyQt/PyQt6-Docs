.. sip:method-description::
    :status: todo
    :pysig: a60ac9bae9204419024da5e0d72c4bb5
    :realsig: (QExposeEvent*)
    :digest: 7ee133d088386a2a855185a5d1e9398c

The expose event (\ *ev*) is sent by the window system when a window moves between the un-exposed and exposed states.

An exposed window is potentially visible to the user. If the window is moved off screen, is made totally obscured by another window, is minimized, or similar, this function might be called and the value of :sip:ref:`~PyQt6.QtGui.QWindow.isExposed` might change to false. You may use this event to limit expensive operations such as animations to only run when the window is exposed.

This event should not be used to paint. To handle painting implement :sip:ref:`~PyQt6.QtGui.QWindow.paintEvent` instead.

A resize event will always be sent before the expose event the first time a window is shown.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.paintEvent`, :sip:ref:`~PyQt6.QtGui.QWindow.isExposed`.
