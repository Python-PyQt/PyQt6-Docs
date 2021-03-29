.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realsig: (bool)
    :digest: e7a24f96d68b1bc81ee0905c94e5e37e

Sets whether keyboard grab should be enabled or not (\ *grab*).

If the return value is true, the window receives all key events until (false) is called; other windows get no key events at all. Mouse events are not affected. Use :sip:ref:`~PyQt6.QtGui.QWindow.setMouseGrabEnabled` if you want to grab that.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setMouseGrabEnabled`.
