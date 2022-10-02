.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: () const
    :digest: 007afb1f2f4fce960eca8b536bfca278

Returns the requested surfaceformat of this offscreen surface.

If the requested format was not supported by the platform implementation, the requestedFormat will differ from the actual offscreen surface format.

This is the value set with :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.setFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.setFormat`, :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.format`.
