.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 2838157ac49eace10a04934a4aee95d3

Attempts to create the OpenGL context with the current configuration.

The current configuration includes the format, the share context, and the screen.

If the OpenGL implementation on your system does not support the requested version of OpenGL context, then `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ will try to create the closest matching version. The actual created context properties can be queried using the :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` returned by the :sip:ref:`~PyQt6.QtGui.QOpenGLContext.format` function. For example, if you request a context that supports OpenGL 4.3 Core profile but the driver and/or hardware only supports version 3.2 Core profile contexts then you will get a 3.2 Core profile context.

Returns ``true`` if the native context was successfully created and is ready to be used with :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent`, :sip:ref:`~PyQt6.QtGui.QOpenGLContext.swapBuffers`, etc.

**Note:** If the context already exists, this function destroys the existing context first, and then creates a new one.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent`, :sip:ref:`~PyQt6.QtGui.QOpenGLContext.format`.
