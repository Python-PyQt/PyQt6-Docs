.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: (const QSurfaceFormat&)
    :digest: 8e135d05c094dece471c44b1dee6a1d6

Sets the window's surface *format*.

The format determines properties such as color depth, alpha, depth and stencil buffer size, etc. For example, to give a window a transparent background (provided that the window system supports compositing, and provided that other content in the window does not make it opaque again):

::

    QSurfaceFormat format;
    format.setAlphaBufferSize(8);
    window.setFormat(format);

The surface format will be resolved in the :sip:ref:`~PyQt6.QtGui.QWindow.create` function. Calling this function after :sip:ref:`~PyQt6.QtGui.QWindow.create` has been called will not re-resolve the surface format of the native surface.

When the format is not explicitly set via this function, the format returned by :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.defaultFormat` will be used. This means that when having multiple windows, individual calls to this function can be replaced by one single call to :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` before creating the first window.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.format`, :sip:ref:`~PyQt6.QtGui.QWindow.create`, :sip:ref:`~PyQt6.QtGui.QWindow.destroy`, :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat`.
