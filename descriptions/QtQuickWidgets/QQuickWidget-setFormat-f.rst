.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: (const QSurfaceFormat&)
    :digest: 48c3b660a9091845c881a5e1e8d5e368

Sets the surface *format* for the context and offscreen surface used by this widget.

Call this function when there is a need to request a context for a given OpenGL version or profile. The sizes for depth, stencil and alpha buffers are taken care of automatically and there is no need to request those explicitly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setFormat`, :sip:ref:`~PyQt6.QtGui.QWindow.format`, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.format`.
