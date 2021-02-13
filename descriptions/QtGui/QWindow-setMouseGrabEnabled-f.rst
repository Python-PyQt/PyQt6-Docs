.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realsig: (bool)
    :digest: 5c0e6027d2076ae7e7bf90f94fff83c9

Sets whether mouse grab should be enabled or not (\ *grab*).

If the return value is true, the window receives all mouse events until (false) is called; other windows get no mouse events at all. Keyboard events are not affected. Use :sip:ref:`~PyQt6.QtGui.QWindow.setKeyboardGrabEnabled` if you want to grab that.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setKeyboardGrabEnabled`.
