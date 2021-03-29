.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: () const
    :digest: 8c679110f38cd91d31783a4bbeaf1ef4

Returns the requested surface format of this window.

If the requested format was not supported by the platform implementation, the  will differ from the actual window format.

This is the value set with :sip:ref:`~PyQt6.QtGui.QWindow.setFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setFormat`, :sip:ref:`~PyQt6.QtGui.QWindow.format`.
