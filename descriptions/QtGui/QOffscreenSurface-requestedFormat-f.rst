.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: () const
    :digest: 56ea2efc8504a876b839a95d3802ea4b

Returns the requested surfaceformat of this offscreen surface.

If the requested format was not supported by the platform implementation, the  will differ from the actual offscreen surface format.

This is the value set with :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.setFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.setFormat`, :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.format`.
