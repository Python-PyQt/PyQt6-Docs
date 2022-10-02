.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realsig: (bool)
    :digest: c5d362307ead8bcf51d42e1946ef699e

Sets whether mouse grab should be enabled or not (\ *grab*).

If the return value is true, the window receives all mouse events until setMouseGrabEnabled(false) is called; other windows get no mouse events at all. Keyboard events are not affected. Use :sip:ref:`~PyQt6.QtGui.QWindow.setKeyboardGrabEnabled` if you want to grab that.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setKeyboardGrabEnabled`.
