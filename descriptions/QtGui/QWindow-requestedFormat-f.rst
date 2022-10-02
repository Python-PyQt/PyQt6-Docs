.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: () const
    :digest: d243b251cbfb8826d9e3e99ad1eca1bc

Returns the requested surface format of this window.

If the requested format was not supported by the platform implementation, the requestedFormat will differ from the actual window format.

This is the value set with :sip:ref:`~PyQt6.QtGui.QWindow.setFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setFormat`, :sip:ref:`~PyQt6.QtGui.QWindow.format`.
