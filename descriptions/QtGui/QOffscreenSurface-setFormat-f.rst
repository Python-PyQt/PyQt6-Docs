.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: (const QSurfaceFormat&)
    :digest: 2a34e4ab58df3417d96d1bd091ee30d9

Sets the offscreen surface *format*.

The surface format will be resolved in the :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.create` function. Calling this function after :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.create` will not re-resolve the surface format of the native surface.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.format`, :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.create`, :sip:ref:`~PyQt6.QtGui.QOffscreenSurface.destroy`.
