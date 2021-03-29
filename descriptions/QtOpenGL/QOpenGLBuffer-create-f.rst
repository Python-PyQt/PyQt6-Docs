.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: db4cd3461060139e22c0b88cd11f0012

Creates the buffer object in the OpenGL server. Returns ``true`` if the object was created; false otherwise.

This function must be called with a current `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_. The buffer will be bound to and can only be used in that context (or any other context that is shared with it).

This function will return false if the OpenGL implementation does not support buffers, or there is no current `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.isCreated`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.allocate`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.write`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.destroy`.
